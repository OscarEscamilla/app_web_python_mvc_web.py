import web 
import config as config

class Index:

	def __init__(self):
		pass


	def GET(self):
		productos = config.model_clientes.select_clientes().list() # selecciona todos los registros usando el archivo importado config
		return config.render.index(productos)




