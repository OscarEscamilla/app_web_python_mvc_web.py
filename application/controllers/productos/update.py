import web
import config as config


class Update:
	
	def __init__(self):
		pass


	def GET(self, nombre):

		producto = config.model_productos.select_nombre(nombre)
		return config.render.update(producto)

	def POST(self, nombre):
		formulario = web.input()
		nombre = formulario['nombre']
		marca = formulario['marca']
		precio = formulario['precio']
		descripcion = ['descripcion']
		config.model_productos.update_producto(nombre, marca, precio,  descripcion)
		raise web.seeother('/productos')