# -*- coding: utf-8 -*-
from models import *
from app.investigacion.models import Investigacion
from app.compania.models import *
from app.entrevista.services import EntrevistaService


class ControllerPersona(object):
	'''
		Clase auxiliar para realizar el guardado en la base de datos sobre la infromación extraida del usuario 
		a través del archivo de excel. La información viene en formato json.
	'''
	errors = []

	def saveAllData(self, investigacion, data, archivo_id, user):
		'''
			Función principal para guardar la información del candidato, esta se encarga de generar el registro.
		'''
		candidato = EntrevistaPersona()
		
		#Asignar datos generales a candidato (modelo Persona)
		self.setGralData(investigacion, candidato, data['candidato']['datos_generales'])
		
		#Salir de la funcion si hubo errores.
		if len(self.errors): 
			return

		#Guardar registro de candidato
		try:
			candidato.save()
		except Exception, e:
			self.errors.append('Error al guardar registro, los datos no fueron almacenados.')
		
		if len(self.errors): #Salir de la funcion si hubo errores.
			return

		#Asignar el resto de los datos generales
		self.setExtraGralData(candidato, data['candidato']['datos_generales'])
		#Asignar iformación personal
		self.setInfoPersonal(candidato, data['candidato']['info_personal'])
		#Asignar información salud
		self.setSalud(candidato, data['candidato']['datos_salud'])
		#Asignar información actividades y hábitos
		self.setActividadesHabitos(candidato, data['candidato']['actividades_habitos'])
		#Asignar información académica
		self.setInfoAcademica(candidato, data['candidato']['info_academica'])
		#Asignar info situacion vivienda
		self.setSituacionVivienda(candidato, data['candidato']['situacion_vivienda'])
		#Asignar info marco familiar
		self.setMarcoFamiliar(candidato, data['candidato']['marco_familiar'])
		#Asignar info economica mensual
		self.setInfoEconomicaMensual(candidato, data['candidato']['info_economica_mensual'])
		#Asignar info situacion económica
		self.setSituacionEconomica(candidato, data['candidato']['situacion_economica'])
		#Asignar info referencias
		self.setReferencias(candidato, data['candidato']['referencias'])
		#Asignar info cuadro evaluación
		self.setCuadroEvaluacion(candidato, data['candidato']['cuadro_evaluacion'])
		#Crear registro de investigacion
		self.setInvestigacion(investigacion, candidato, data['investigacion'], archivo_id, user)

		return candidato.id

	def setGralData(self, investigacion, candidato, datos_generales):
		'''
			Asignar datos generales a candidato
		'''
		try:
			candidato.investigacion = investigacion	
			candidato.nombre = datos_generales['nombre']
			candidato.email = datos_generales['email']
			candidato.edad = datos_generales['edad']
			candidato.rfc = datos_generales['rfc']
			candidato.curp = datos_generales['curp']
			candidato.ife = datos_generales['ife']
			candidato.pasaporte = datos_generales['pasaporte']
			candidato.nss = datos_generales['nss']
			candidato.smn = datos_generales['smn']
			candidato.estado_civil = datos_generales['estado_civil']
			candidato.fecha_matrimonio = datos_generales['fecha_matrimonio']
			candidato.religion = datos_generales['religion']
			candidato.tiempo_radicando = datos_generales['tiempo_radicando']
			candidato.medio_utilizado = datos_generales['medio_utilizado']
			candidato.referencia_vacante = datos_generales['referencia_vacante']
			candidato.tiempo_transporte = datos_generales['tiempo_transporte']
			candidato.dependientes_economicos = datos_generales['dependientes_economicos']
		except Exception, e:
			self.errors.append('Error en registro de datos generales.')

		return

	def setExtraGralData(self, candidato, datos_generales):
		'''
			Asignar datos generales EXTRA a candidato
		'''
		try:
			#Asignar 'teléfonos'
			if datos_generales['telefono']['casa'] :
				EntrevistaTelefono(persona=candidato, categoria='casa', numero=datos_generales['telefono']['casa'], parentesco='').save()
			if datos_generales['telefono']['movil'] :
				EntrevistaTelefono(persona=candidato, categoria='movil', numero=datos_generales['telefono']['movil'], parentesco='').save()
			if datos_generales['telefono']['recados']['numero'] :
				EntrevistaTelefono(persona=candidato, categoria='recado', numero=datos_generales['telefono']['recados']['numero'], parentesco=datos_generales['telefono']['recados']['parentesco']).save()

			#Asignar datos 'domicilio'
			EntrevistaDireccion(	persona=candidato, 
									calle=datos_generales['direccion']['calle'],
									num=datos_generales['direccion']['num'],
									ciudad=datos_generales['direccion']['ciudad'], 
									colonia=datos_generales['direccion']['colonia'],
									cp=datos_generales['direccion']['cp'],
									estado=datos_generales['direccion']['estado']).save()

			#Asignar datos 'origen'
			EntrevistaOrigen( 	persona=candidato,
								lugar=datos_generales['origen']['lugar'],
								nacionalidad=datos_generales['origen']['nacionalidad'],
								fecha=datos_generales['origen']['fecha']).save()


			#Asignar datos 'licencia'
			EntrevistaLicencia(	persona=candidato,
								numero=datos_generales['licencia']['numero'],
								tipo=datos_generales['licencia']['tipo']).save()

			#Asignar datos 'prestaciones de vivienda'
			EntrevistaPrestacionVivienda(	persona=candidato,
											categoria_viv='infonavit',
											activo=datos_generales['infonavit']['activo'],
											fecha_tramite=datos_generales['infonavit']['fecha_tramite'],
											numero_credito=datos_generales['infonavit']['numero'],
											uso=datos_generales['infonavit']['uso']).save()

			EntrevistaPrestacionVivienda(	persona=candidato,
											categoria_viv='fonacot',
											activo=datos_generales['fonacot']['activo'],
											fecha_tramite=datos_generales['fonacot']['fecha_tramite'],
											numero_credito=datos_generales['fonacot']['numero'],
											uso=datos_generales['fonacot']['uso']).save()
		except Exception, e:
			self.errors.append('Error en registro de datos generales.')

		return

	def setInfoPersonal(self, candidato, info_personal):
		'''
			Asignar información personal a candidato 
		'''
		try:
			EntrevistaInfoPersonal(	persona=candidato,
							antecedentes_penales=info_personal['antecedentes_penales'],
							tatuajes=info_personal['tatuajes'] ).save()

			#Historial en empresa
			EntrevistaHistorialEnEmpresa(	persona=candidato,
											categoria='trabajo',
											tiene=info_personal['trabajo_anterior_en_empresa']['tiene'],
											motivo_salida=info_personal['trabajo_anterior_en_empresa']['motivo_salida'],
											puesto=info_personal['trabajo_anterior_en_empresa']['puesto'],
											sucursal=info_personal['trabajo_anterior_en_empresa']['sucursal'],
											periodo=info_personal['trabajo_anterior_en_empresa']['periodo']).save()

			EntrevistaHistorialEnEmpresa(	persona=candidato,
											categoria='familiar',
											tiene=info_personal['familiar_en_empresa']['tiene'],
											puesto=info_personal['familiar_en_empresa']['puesto'],
											sucursal=info_personal['familiar_en_empresa']['sucursal'],
											nombre=info_personal['familiar_en_empresa']['nombre']).save()
		except Exception, e:
			self.errors.append('Error en registro de información personal.')

		return

	def setSalud(self, candidato, datos_salud):
		'''
			Asignar información de salud a candidato
		'''
		try:
			EntrevistaSalud(	persona=candidato,
								peso_kg=datos_salud['peso_kg'],
								estatura_mts=datos_salud['estatura_mts'],
								salud_fisica=datos_salud['salud_fisica'],
								salud_visual=datos_salud['salud_visual'],
								embarazo_meses=datos_salud['embarazo_meses'],
								ejercicio_tipo_frecuencia=datos_salud['ejercicio_tipo_frecuencia'],
								accidentes=datos_salud['accidentes'],
								intervenciones_quirurgicas=datos_salud['intervenciones_quirurgicas'],
								enfermedades_familiares=datos_salud['enfermedades_familiares'],
								tratamiento_medico_psicologico=datos_salud['tratamiento_medico_psicologico'],
								enfermedades_mayor_frecuencia=datos_salud['enfermedades_mayor_frecuencia'],
								institucion_medica=datos_salud['institucion_medica']).save()
		except Exception, e:
			self.errors.append('Error en registro de datos de salud.')

		return

	def setActividadesHabitos(self, candidato, actividades_habitos):
		'''
			Asignar información actividades y hábitos
		'''
		try:
			EntrevistaActividadesHabitos(	persona=candidato,
											tiempo_libre=actividades_habitos['tiempo_libre'],
											extras=actividades_habitos['extras'],
											frecuencia_tabaco=actividades_habitos['frecuencia_tabaco'],
											frecuencia_alcohol=actividades_habitos['frecuencia_alcohol'],
											frecuencia_otras_sust=actividades_habitos['frecuencia_otras_sust']).save()
		except Exception, e:
			self.errors.append('Error en registro de actividades y hábitos.')

		return	

	def setInfoAcademica(self, candidato, info_academica):
		'''
			Asignar información académica
		'''
		try:
			EntrevistaAcademica(	person = candidato,
									cedula_profesional = info_academica['cedula_profesional'],
									cedula_prof_ano_exp = info_academica['cedula_prof_ano_exp'],
									estudios_actuales = info_academica['estudios_actuales']).save()


			for grado in EntrevistaGradoEscolaridad.GRADO_OPCIONES:
				EntrevistaGradoEscolaridad(	person = candidato,
											grado = grado[0],
											institucion = info_academica[grado[0]]['institucion'],
											ciudad = info_academica[grado[0]]['ciudad'],
											anos = info_academica[grado[0]]['anos'],
											certificado = info_academica[grado[0]]['certificado']).save()

			EntrevistaOtroIdioma(	person = candidato,
									porcentaje = info_academica['otro_idioma']['porcentaje'],
									idioma = info_academica['otro_idioma']['idioma']).save()
		except Exception, e:
			self.errors.append('Error en registro de información académica.')

		return

	def setSituacionVivienda(self, candidato, situacion_vivienda):
		'''
			Asignar información situación vivienda
		'''
		try:
			EntrevistaSituacionVivienda( 	person = candidato,
											tiempo_radicando = situacion_vivienda['tiempo_radicando'],
											tipo_mobiliario = situacion_vivienda['tipo_mobiliario'],
											sector_socioeconomico = situacion_vivienda['sector_socioeconomico'],
											personas_viven_con_evaluado = situacion_vivienda['personas_viven_con_evaluado'],
											conservacion = situacion_vivienda['conservacion'],
											tamano_aprox_mts2 = situacion_vivienda['tamano_aprox_mts2']).save()
			
			EntrevistaPropietarioVivienda(	person = candidato,
											nombre = situacion_vivienda['propietario']['nombre'],
											parentesco = situacion_vivienda['propietario']['parentesco']).save()

			EntrevistaCaractaristicasVivienda(	person = candidato,
												propia = situacion_vivienda['caracteristicas_vivienda']['propia'],
												rentada = situacion_vivienda['caracteristicas_vivienda']['rentada'],
												hipotecada = situacion_vivienda['caracteristicas_vivienda']['hipotecada'],
												prestada = situacion_vivienda['caracteristicas_vivienda']['prestada'],
												otra = situacion_vivienda['caracteristicas_vivienda']['otra'],
												valor_aproximado = situacion_vivienda['caracteristicas_vivienda']['valor_aproximado'],
												renta_mensual = situacion_vivienda['caracteristicas_vivienda']['renta_mensual']).save()

			EntrevistaTipoInmueble(	person = candidato,
									casa = situacion_vivienda['tipo_inmueble']['casa'],
									terreno_compartido = situacion_vivienda['tipo_inmueble']['terreno_compartido'],
									departamento = situacion_vivienda['tipo_inmueble']['departamento'],
									vivienda_popular = situacion_vivienda['tipo_inmueble']['vivienda_popular'],
									otro_tipo = situacion_vivienda['tipo_inmueble']['otro_tipo']).save()

			EntrevistaDistribucionDimensiones(	person = candidato,
												habitaciones = situacion_vivienda['distribucion_dimensiones']['habitaciones'],
												banos = situacion_vivienda['distribucion_dimensiones']['banos'],
												salas = situacion_vivienda['distribucion_dimensiones']['salas'],
												comedor = situacion_vivienda['distribucion_dimensiones']['comedor'],
												cocina = situacion_vivienda['distribucion_dimensiones']['cocina'],
												patios = situacion_vivienda['distribucion_dimensiones']['patios'],
												cocheras = situacion_vivienda['distribucion_dimensiones']['cocheras']).save()
		except Exception, e:
			self.errors.append('Error en registro de situación de vivienda.')

		return

	def setMarcoFamiliar(self, candidato, marco_familiar):
		'''
			Asignar información marco familiar
		'''
		srv = EntrevistaService()
		miembros_tipo_array = ['hermano', 'hijo', 'otro']
		try:
			for tipo in EntrevistaMiembroMarcoFamiliar.FAMILIAR_OPCIONES:
				if tipo[0] in miembros_tipo_array:
					for miembro in marco_familiar[tipo[0]]:
						EntrevistaMiembroMarcoFamiliar(	person = candidato,
														tipo = tipo[0],
														nombre = miembro['nombre'],
														edad = miembro['edad'],
														ocupacion = miembro['ocupacion'],
														empresa = miembro['empresa'],
														residencia = miembro['residencia'],
														telefono = srv.clean_telefono(miembro['telefono'])).save()
				else:
						EntrevistaMiembroMarcoFamiliar(	person = candidato,
														tipo = tipo[0],
														nombre = marco_familiar[tipo[0]]['nombre'],
														edad = marco_familiar[tipo[0]]['edad'],
														ocupacion = marco_familiar[tipo[0]]['ocupacion'],
														empresa = marco_familiar[tipo[0]]['empresa'],
														residencia = marco_familiar[tipo[0]]['residencia'],
														telefono = srv.clean_telefono(marco_familiar[tipo[0]]['telefono'])).save()
		except Exception, e:
			self.errors.append('Error en registro de marco familiar.')
		return

	def setInfoEconomicaMensual(self, candidato, info_economica_mensual):
		'''
			Asignar información económica mensual
		'''
		try:
			for ingreso in info_economica_mensual['ingresos']:
				# monto = ingreso['monto'] if isinstance(ingreso['monto'], float) else 0
				EntrevistaEconomica(	person = candidato,
										tipo = 'ingreso',
										concepto = ingreso['concepto'],
										monto = ingreso['monto']).save()

			for egreso in info_economica_mensual['egresos']:
				# monto = egreso['monto'] if isinstance(egreso['monto'], float) else 0	
				EntrevistaEconomica(	person = candidato,
										tipo = 'egreso',
										concepto = egreso['concepto'],
										monto = egreso['monto']).save()
		except Exception, e:
			self.errors.append('Error en registro de información económica mensual.')

		return

	def setSituacionEconomica(self, candidato, situacion_economica):
		'''
			Asignar información situación económica
		'''
		try:
			for tarjeta in situacion_economica['tarjetas_credito_comerciales']:
				EntrevistaTarjetaCreditoComercial(	person = candidato,
													institucion = tarjeta['institucion'],
													limite_credito = tarjeta['limite_credito'],
													pago_minimo = tarjeta['pago_minimo'],
													saldo_actual = tarjeta['saldo_actual']).save()

			for cuenta in situacion_economica['cuentas_debito']:
				EntrevistaCuentaDebito(	person = candidato,
										institucion = cuenta['institucion'],
										saldo_mensual = cuenta['saldo_mensual'],
										antiguedad = cuenta['antiguedad'],
										ahorro = cuenta['ahorro']).save()


			for auto in situacion_economica['automoviles']:
				EntrevistaAutomovil(	person = candidato,
										marca = auto['marca'],
										modelo_ano = auto['modelo_ano'],
										liquidacion = auto['liquidacion'],
										valor_comercial = auto['valor_comercial']).save()

			for br in situacion_economica['bienes_raices']:
				EntrevistaBienesRaices(	person = candidato,
										tipo_inmueble = br['tipo_inmueble'],
										ubicacion = br['ubicacion'],
										liquidacion = br['liquidacion'],
										valor_comercial = br['valor_comercial']).save()

			for seguro in situacion_economica['seguros']:
				EntrevistaSeguro(	person = candidato,
									empresa = seguro['empresa'],
									tipo = seguro['tipo'],
									forma_pago = seguro['forma_pago'],
									vigencia = seguro['vigencia']).save()

			for deuda in situacion_economica['deudas_actuales']:
				EntrevistaDeudaActual(	person = candidato,
										fecha_otorgamiento = deuda['fecha_otorgamiento'],
										tipo = deuda['tipo'],
										institucion = deuda['institucion'],
										cantidad_total = deuda['cantidad_total'],
										saldo_actual = deuda['saldo_actual'],
										pago_mensual = deuda['pago_mensual']).save()
		except Exception, e:
			self.errors.append('Error en registro de información de situación económica.')

		return

	def setReferencias(self, candidato, referencias):
		'''
			Asignar información referencias
		'''
		try:
			for ref in referencias:
				EntrevistaReferencia(	person = candidato,
										nombre = ref['nombre'],
										domicilio = ref['domicilio'],
										telefono = ref['telefono'],
										tiempo_conocido = ref['tiempo_conocido'],
										parentesco = ref['parentesco'],
										ocupacion = ref['ocupacion'],
										lugares_labor_evaluado = ref['lugares_labor_evaluado'],
										opinion = ref['opinion']).save()
		except Exception, e:
			self.errors.append('Error en registro de referencias.')

		return

	def setCuadroEvaluacion(self, candidato, cuadro_evaluacion):
		'''
			Asignar información cuadro evaluación
		'''
		try:
			for doc in cuadro_evaluacion['documentos_cotejados']:
				estatus = True if doc['estatus'] else False
				observaciones = doc['observaciones'] if doc['tipo'] == 'motivos_falta_docs' else ''

				EntrevistaDocumentoCotejado(	person = candidato,
												tipo = doc['tipo'],
												estatus = estatus,
												observaciones = observaciones ).save()

			for aspecto in cuadro_evaluacion['aspectos_hogar']:
				EntrevistaAspectoHogar(	person = candidato,
										tipo = aspecto['tipo'],
										estatus = aspecto['estatus']).save()

			for aspecto in cuadro_evaluacion['aspectos_candidato']:
				EntrevistaAspectoCandidato(	person = candidato,
											tipo = aspecto['tipo'],
											estatus = aspecto['estatus']).save()
		except Exception, e:
			self.errors.append('Error en registro de cuadro de evaluación.')

		return

	def setInvestigacion(self, investigacion, candidato, data_investigacion, archivo_id, user):
		try:
			#Determinar valor de 'resultado'
			resultado = '0'#'por evaluar'
			if data_investigacion['viable']:
				resultado = '1'#'viable' 
			elif data_investigacion['no_viable']:
				resultado = '3' #'no viable'
			elif data_investigacion['reservas']:
				resultado = '2'#'con reservas'

			#Guardar registro Investigación
			EntrevistaInvestigacion(agente=user,
										persona = candidato,
										empresa_contratante = data_investigacion['empresa'],
										puesto = data_investigacion['puesto'],
										fecha_recibido = data_investigacion['fecha'],
										conclusiones = data_investigacion['conclusiones'],
										resultado = resultado,
										archivo = archivo_id
									).save()
			EntrevistaCita(investigacion=investigacion, fecha_entrevista=data_investigacion['fecha'], hora_entrevista=data_investigacion['fecha_hora']).save()
		except Exception, e:
			self.errors.append('Error en registro de investigación.')

		return


	"""docstring for ControllerPersona"""
	def __init__(self):
		super(ControllerPersona, self).__init__()
		self.errors = []
