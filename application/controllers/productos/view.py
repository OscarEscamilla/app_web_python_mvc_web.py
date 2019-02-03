import web

import config as config

class View:
	
	def __init__(self):
		pass

	def GET(self, nombre):

		productos = config.model_productos.select_nombre(nombre)
		return config.render.view(productos)