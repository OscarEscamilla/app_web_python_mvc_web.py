import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, nombre): 
        clientes = config.model_clientes.select_nombre(nombre) # Selecciona el registro que coincida con nombre
        return config.render.update(clientes) 
    
    def POST(self,nombre):
        formulario = web.input() 
        nombre = formulario['nombre'] 
        direccion = formulario['direccion'] 
        sexo = formulario['sexo'] 
        correo = formulario['correo'] 
        config.model_clientes.update_clientes(nombre, direccion, sexo, correo)
        raise web.seeother('/clientes') 
