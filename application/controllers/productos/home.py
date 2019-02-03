import web
import config as config

class Home:
	def __init__(self):
		pass

	def GET(self):
		return config.render.home()