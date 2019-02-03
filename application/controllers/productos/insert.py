import web
import config as config

class Insert:
	def __init__(self):
		pass

	def GET(self):
		return config.render.insert()

	def POST(self):
		formulario = web.input()
		nombre = formulario['nombre']
		marca = formulario['marca']
		precio = formulario['precio']
		descripcion = formulario['descripcion']
		config.model_productos.insert_producto(nombre, marca, precio, descripcion)
		raise web.seeother('/')