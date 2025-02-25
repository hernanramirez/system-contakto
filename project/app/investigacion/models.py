# -*- coding: utf-8 -*-

import datetime

from app.agente.models import GestorInfo, Labels
from app.clientes.models import (
    ClienteSolicitud,
    ClienteSolicitudCandidato,
    ClienteTipoInvestigacion,
)
from app.compania.models import Compania, Contacto, Sucursales
from app.persona.models import File, Persona
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum

ACTIVO_OPCIONES = (
    (0, "Sí/No"),
    (1, "Sí"),
    (2, "No"),
)


def parse_string_to_date(string, fuzzy=False):
    if not string:
        return False

    try:
        return datetime.datetime.strptime(string, "%d/%m/%Y")

    except ValueError:
        return False


class Investigacion(models.Model):
    TIPO_INVESTIGACION_OPCIONES = (
        (1, "Laboral"),
        (2, "Socioeconómico"),
        (4, "Psicometrías"),
        (5, "Visita Domiciliaria"),
        (7, "Visita Domiciliaria con demandas"),
        (6, "Validación de Demandas"),
        (3, "Otro"),
    )
    RESULTADO_OPCIONES = (
        ("0", "Por evaluar"),
        ("1", "Viable"),
        ("2", "No viable"),
        ("3", "Con reservas"),
        ("4", "Cancelado"),
    )
    STATUS_OPCIONES = (
        ("0", "En Investigación"),
        ("1", "Pdt. por Cliente"),
        ("2", "Inv. Terminada"),
    )
    STATUS_GRAL_OPCIONES = (
        ("0", "Abierto"),
        ("1", "Pdt. por Cliente"),
        ("2", "Cerrada"),
        ("3", "Abierto + Pdt. por Cliente"),
        ("4", "Cerrado + Pdt. por Cliente"),
    )

    agente = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    ejecutivo_de_cuentas = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="ejecutivo_de_cuentas",
    )
    coordinador_visitas = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="coordinador_visitas",
    )
    ejecutivo_visitas = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="ejecutivo_visitas",
    )
    coordinador_psicometrico = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="coordinador_psometrico",
    )

    cliente_solicitud = models.ForeignKey(
        ClienteSolicitud, on_delete=models.CASCADE, blank=True, null=True
    )
    cliente_solicitud_candidato = models.ForeignKey(
        ClienteSolicitudCandidato, on_delete=models.CASCADE, blank=True, null=True
    )
    candidato = models.ForeignKey(Persona, on_delete=models.CASCADE)
    compania = models.ForeignKey(Compania, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursales, models.SET_NULL, blank=True, null=True)
    contacto = models.ForeignKey(
        Contacto, on_delete=models.CASCADE, blank=True, null=True
    )
    # Tenerla como fecha de asignacion del agente tomarla del sistema
    fecha_recibido = models.DateField(blank=True, null=True)
    hora_recibido = models.CharField(max_length=30, blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    puesto = models.CharField(max_length=140)
    #Fecha en que se asigna el ejecutivo laboral
    fecha_asignacion = models.DateTimeField(blank=True, null=True)

    observaciones = models.TextField(max_length=200, blank=True, null=True)
    entrevista = models.DateTimeField(blank=True, null=True)
    fecha_registro = models.DateField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

	conclusiones = models.TextField(max_length=16000, blank=True, null=True)
	resultado = models.CharField(max_length=30, choices=RESULTADO_OPCIONES, blank=True, null=True, default='0')
	archivo = models.ForeignKey(File, blank=True, null=True, on_delete=models.CASCADE)
	folio = models.CharField(max_length=50, blank=True, null=True)
	presupuesto = models.CharField(max_length=50, blank=True, null=True)
	
	status = models.CharField(max_length=140, choices=STATUS_OPCIONES, null=True, blank=True, default='0') #En template: "Estatus de Inv. Laboral"
	status_active = models.BooleanField(default=True) # revisar si es necesario, si no borrarlo
	status_general = models.CharField(max_length=140, choices=STATUS_GRAL_OPCIONES, null=True, blank=True, default='0')
	observaciones_generales = models.TextField(max_length=160000, blank=True, null=True)
	
	tipo_investigacion_status = models.IntegerField(choices=TIPO_INVESTIGACION_OPCIONES, null=True, blank=True)
	tipo_investigacion_texto = models.TextField(max_length=16000, blank=True, null=True)

    # Historia en empresa
    laboro_anteriormente = models.IntegerField(
        default=0, choices=ACTIVO_OPCIONES, blank=True, null=True
    )
    familiar_laborando = models.IntegerField(
        default=0, choices=ACTIVO_OPCIONES, blank=True, null=True
    )
    label = models.ForeignKey(Labels, blank=True, null=True, on_delete=models.CASCADE)

    # Secuencia de investigaciones
    candidato_validado = models.BooleanField(default=False)
    ejecutivo_de_cuentas_asignado = models.BooleanField(default=False)
    coord_psicometrico_asignadado = models.BooleanField(default=False)
    coord_visitas_asignado = models.BooleanField(default=False)
    entrevista = models.BooleanField(default=False)
    entrevista_asignacion_visita_domiciliaria = models.BooleanField(default=False)
    entrevista_from_completado = models.BooleanField(default=False)
    entrevista_app_ejecutivo_asignado = models.BooleanField(default=False)
    entrevista_app_completado = models.BooleanField(default=False)
    laboral = models.BooleanField(default=True)
    laboral_completado = models.BooleanField(default=False)
    psicometrico = models.BooleanField(default=False)
    psicometrico_ejecutivo_asignado = models.BooleanField(default=False)
    psicometrico_completado = models.BooleanField(default=False)

    investigacion_completada = models.BooleanField(default=False)

    # seguimiento de facturas
    investigacion_factura_enviada_al_cliente = models.BooleanField(default=False)
    investigacion_factura_completada = models.BooleanField(default=False)
    investigacion_factura_pago_completado = models.BooleanField(default=False)
    investigacion_factura_pago_verificado = models.BooleanField(default=False)

    def __str__(self):
        return "%s / %s" % (self.candidato, self.compania)

    def print_status_general(self):
        for status in self.STATUS_GRAL_OPCIONES:
            if status[0] == self.status_general:
                return status[1]

        return ""

    def get_trayectorias_laborales(self, use_status=None):
        trayectorias = self.candidato.trayectorialaboral_set.filter(status=True)
        if use_status:
            trayectorias = trayectorias.filter(visible_en_status=True)

        data = []
        for trayectoria in trayectorias:
            data.append(trayectoria)

        for i in range(len(data)):
            date_a = parse_string_to_date(data[i].periodo_alta)
            if not date_a:
                continue

            for j in range(len(data)):
                date_b = parse_string_to_date(data[j].periodo_alta)
                if not date_b:
                    continue

                if date_a > date_b:
                    tmp = data[i]
                    data[i] = data[j]
                    data[j] = tmp

        return data

    @property
    def get_total_facturado(self):

        total = 0

        cliente_solicitud_facturas = InvestigacionFactura.objects.filter(
            investigacion_id=self.pk
        )

        for f in cliente_solicitud_facturas:
            total += (f.monto * f.cantidad) - f.descuento

        return total

    @property
    def get_total_pagado(self):
        total = 0
        cliente_solicitud_facturas = InvestigacionFacturaClienteArchivo.objects.filter(
            investigacion_id=self.pk
        ).aggregate(total=Sum("monto"))

        if cliente_solicitud_facturas["total"]:
            total = cliente_solicitud_facturas["total"]
        
        return total

    @property
    def get_total_pendiente(self):
        total = 0
        if self.get_total_facturado and self.get_total_pagado:
            total = self.get_total_facturado - self.get_total_pagado
        return total


class InvestigacionExtra(models.Model):
    investigacion = models.ForeignKey(Investigacion, on_delete=models.CASCADE)
    nombre = models.TextField(max_length=200, blank=True, null=True)
    apellido = models.TextField(max_length=200, blank=True, null=True)


class GestorInvestigacion(models.Model):
    ESTATUS = ((1, "ASIGNADA"), (2, "EN ATENCIÓN"), (3, "CONCLUIDA"))
    investigacion = models.ForeignKey(Investigacion, on_delete=models.CASCADE)
    gestor = models.ForeignKey(GestorInfo, on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField(null=True, blank=True)
    fecha_registro = models.DateTimeField(null=True, blank=True)
    fecha_atencion = models.DateTimeField(null=True, blank=True)
    estatus = models.PositiveSmallIntegerField(choices=ESTATUS, default=1)
    completado = models.BooleanField(default=False)
    pagado = models.BooleanField(default=False)

    @property
    def get_gestor_name(self):
        sc = User.objects.get(pk=self.gestor.usuario.id)
        return sc

    # def __str__(self):
    #     return '{} / {} / {}'.format(self.investigacion,self.gestor, self.get_estatus_display())

    def __str__(self):
        return "{}".format(self.gestor)


class GestorInvestigacionPago(models.Model):
    gestor = models.ForeignKey(GestorInfo, on_delete=models.CASCADE)

    pagado = models.BooleanField(default=False)
    fecha_de_pago = models.DateTimeField(null=True, blank=True)
    comprobante = models.FileField(
        upload_to="gestor_investigacion_pago", blank=True, null=True
    )

    created = models.DateTimeField(auto_now=True, blank=True)
    modificated = models.DateTimeField(auto_now_add=True, blank=True)


class GestorInvestigacionPagoInv(models.Model):
    gestor_investigacion_pago = models.ForeignKey(
        GestorInvestigacionPago, on_delete=models.CASCADE
    )
    investigacion = models.ForeignKey(Investigacion, on_delete=models.CASCADE)


class InvestigacionBitacora(models.Model):
    investigacion = models.ForeignKey(Investigacion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    servicio = models.CharField(max_length=120, default="")
    observaciones = models.TextField(default="")
    datetime = models.DateTimeField(auto_now_add=True)


class PsicometricoUser(User):

    telefono = models.CharField(max_length=20, blank=True)

    created = models.DateTimeField(auto_now=True, blank=True)
    modificated = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = "Usuario Psicometrico"
        verbose_name_plural = "Usuarios Psicometricos"

    def __str__(self):
        return "%s, %s" % (self.first_name, self.last_name)


class Psicometrico(models.Model):
    investigacion = models.OneToOneField(
        Investigacion,
        on_delete=models.CASCADE,
        related_name="investigacion_psicometrico",
    )
    user = models.ForeignKey(
        PsicometricoUser, on_delete=models.CASCADE, blank=True, null=True
    )
    observaciones = models.TextField(default="")
    archivo = models.FileField(upload_to="archivo_psicometrico/", blank=True, null=True)
    completado = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now=True, blank=True)
    modificated = models.DateTimeField(auto_now_add=True, blank=True)


class InvestigacionFactura(models.Model):
    investigacion = models.ForeignKey(
        Investigacion, on_delete=models.CASCADE, related_name="investigacion_factura"
    )

    cantidad = models.PositiveSmallIntegerField(default=0)
    descripcion = models.CharField(max_length=140)
    monto = models.FloatField(default=0)
    descuento = models.FloatField(default=0)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    @property
    def get_subtotal(self):
        return (self.monto * self.cantidad) - self.descuento


class InvestigacionFacturaArchivos(models.Model):
    investigacion = models.OneToOneField(
        Investigacion,
        on_delete=models.CASCADE,
        related_name="investigacion_factura_archivos",
    )
    archivo_pdf = models.FileField(
        upload_to="archivo_factura/pdf/", blank=True, null=True
    )
    archivo_xml = models.FileField(
        upload_to="archivo_factura/pdf/", blank=True, null=True
    )

    created = models.DateTimeField(auto_now=True, blank=True)
    modificated = models.DateTimeField(auto_now_add=True, blank=True)

    property

    def get_subtotal(self):
        return (self.monto * self.cantidad) - self.descuento


class InvestigacionFacturaClienteArchivo(models.Model):
    investigacion = models.ForeignKey(
        Investigacion,
        on_delete=models.CASCADE,
        related_name="investigacion_factura_archivo",
    )
    fecha = models.DateField()
    notas = models.TextField(blank=True, null=True)
    monto = models.FloatField(default=0)
    comprobante = models.FileField(
        "Archivo en formato PDF o JPG",
        upload_to="comprobantes/pago/clientes",
        blank=True,
        null=True,
    )
    verificado_por_cobranzas = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now=True, blank=True)
    modificated = models.DateTimeField(auto_now_add=True, blank=True)
