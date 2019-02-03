import web
import config as config 

class Delete:

	def __init__(self):
		pass

	def GET(self, nombre):
		productos = config.model_productos.select_nombre(nombre)
		return config.render.delete(productos)

	def POST(self, nombre):
		formulario = web.input() 
		nombre = formulario['nombre']
		config.model_productos.delete_producto(nombre)
		raise web.seeother('/') 