import web
import config as config 

class Delete:

	def __init__(self):
		pass

	def GET(self, nombre):
		clientes = config.model_clientes.select_nombre(nombre)
		return config.render.delete(clientes)

	def POST(self, nombre):
		formulario = web.input() 
		nombre = formulario['nombre']
		config.model_clientes.delete_cliente(nombre)
		raise web.seeother('/') 