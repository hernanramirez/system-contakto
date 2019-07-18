from app.investigacion.models import Investigacion
from app.util.timer import timethis
from django.db.models import Q
import datetime

class PersonaService:
	'''
	'''
	STATUS_GRAL_OPCIONES_SIDEBAR = (
			('3', 'Abierto + Pdt. por Cliente'),
	    ('0', 'Abierto'),
	    ('1', 'Pdt. por Cliente'),
	    ('2', 'Cerrada'),
	)

	nombre = ''
	compania_id = ''
	compania_nombre = ''
	agente_id = ''
	status_id = ''
	fecha_inicio = ''
	fecha_final = ''
	is_superuser = is_staff = is_usuario_contacto = False
	user = ''
	num_per_list = 20

	def __init__(self, request):
		'''
		'''
		self.nombre = request.POST.get('nombre', '')
		self.compania_id = request.POST.get('compania_id', '')
		self.compania_nombre = request.POST.get('compania_nombre', '')		
		self.agente_id = request.POST.get('agente_id', '')
		self.status_id = request.POST.get('status_id', '')
		self.fecha_inicio = request.POST.get('fecha_inicio', '')
		self.fecha_final = request.POST.get('fecha_final', '')
		if request.user.is_superuser:
			self.is_superuser = True
		elif request.user.is_staff:
			self.is_staff = True
		self.is_usuario_contacto = True if any("contactos" in s for s in request.user.groups.values_list('name',flat=True)) else False
		self.user = request.user
		self.setCandidatoSession(request)


	def setCandidatoSession(self, request):
		'''
		'''
		request.session['filtros_search'] = {
			'nombre': self.nombre,
			'compania_id': self.compania_id,
			'compania_nombre': self.compania_nombre,			
			'agente_id': self.agente_id, 
			'status_id': self.status_id, 
			'fecha_inicio': self.fecha_inicio,
			'fecha_final': self.fecha_final
		}
	
	def getCandidatosList(self):
		'''
		'''
		candidatos = Investigacion.objects.select_related('candidato', 'compania').filter(status_active=True) 
		response = []
		#Si el usuario es agente, filtrar por default las inv. que no tiene asignadas
		if not self.is_superuser and self.is_staff:
			candidatos = candidatos.filter(agente=self.user)
		#Si es un usario de contacto, filtrar por default las inv. que no le corresponden
		elif self.is_usuario_contacto:
			candidatos = candidatos.filter(contacto__email=self.user.email)
		if len(self.fecha_inicio) and len(self.fecha_final):
			fecha_inicio_format = datetime.datetime.strptime(self.fecha_inicio, '%d/%m/%y').strftime('%Y-%m-%d')
			fecha_final_format = datetime.datetime.strptime(self.fecha_final, '%d/%m/%y').strftime('%Y-%m-%d')
			candidatos = candidatos.filter(fecha_recibido__range=(fecha_inicio_format, fecha_final_format))
		if len(self.nombre):
			candidatos = candidatos.filter(Q(candidato__nombre__contains=self.nombre))
		if len(self.compania_id):
			candidatos = candidatos.filter(Q(compania__id=self.compania_id))
		if len(self.agente_id):
			candidatos = candidatos.filter(Q(agente__id=self.agente_id))

		if len(self.status_id):
			# status = 3, es el ultimo status agregado que engloba activo + pendiente por el cliente,
			# por tanto en caso de no ser 3 se considera el status que tenemos tal cual, de lo contrario
			# debido a que status es un integer, se realizar el OR usando valor de activo=0 y ptexcliente=1c,
			# estos valores estan definidos en este archivo en la parte de arriba (STATUS_GRAL_OPCIONES_SIDEBAR)
			if self.status_id != '3':
				candidatos = candidatos.filter(Q(status_general=self.status_id))
			elif self.status_id == '3':
				candidatos = candidatos.filter(Q(status_general=0)|Q(status_general=1))
		
		candidatos = candidatos.order_by('fecha_recibido')[:self.num_per_list]

		for c in candidatos:
			response.append({
				'id': c.id,
				'nombre': c.candidato.nombre,
				'puesto': c.puesto,
				'empresa': c.compania.nombre,
				'fecha': c.fecha_registro.strftime('%d/%m/%Y')
			})

		return response


	@staticmethod
	def get_status_list(investigacion_id):
		'''
		'''		
		investigacion = Investigacion.objects.get(id=investigacion_id)		
		status_list = {}
		status_list['investigacion'] = investigacion.status
		status_list['investigacion_resultado'] = investigacion.resultado
		status_list['entrevista_autorizada'] = investigacion.entrevistacita_set.all()[0].autorizada if investigacion.entrevistacita_set.all().count() > 0 else None
		return status_list	
