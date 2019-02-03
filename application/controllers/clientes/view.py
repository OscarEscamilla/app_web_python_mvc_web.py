import web

import config as config

class View:
	
	def __init__(self):
		pass

	def GET(self, nombre):

		cliente = config.model_clientes.select_nombre(nombre)
		return config.render.view(cliente)