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
		direccion = formulario['direccion']
		sexo = formulario['sexo']
		correo = formulario['correo']
		config.model_clientes.insert_cliente(nombre, direccion, sexo, correo)
		raise web.seeother('/')