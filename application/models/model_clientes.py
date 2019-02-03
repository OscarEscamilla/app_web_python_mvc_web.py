import config as config 

db = config.db

def select_clientes():
    try:
        return db.select('clientes') # Selecciona todos los registros de la tabla clientes
    except Exception as e:
        print "Model select_clientes Error {}".format(e.args)
        print "Model select_clientes Message {}".format(e.message)
        return


def select_nombre(nombre):
	try:
		return db.select('clientes', where = 'nombre=$nombre', vars=locals())[0] #selecciona el primer registro que coincida con el nombre dado en el parametro
	except Exception as e:
		print "Model select_nombre Error ()".format(e.args)
		print "Model select_nombre Message {}".format(e.message)
		return None


""" 
metodo para insertar productos
"""

def insert_cliente(nombre, direccion, sexo,  correo):
	try:
		return db.insert('clientes', 
			nombre = nombre,
			direccion = direccion,
			sexo = sexo,
			correo = correo)
	except Exception as e:
		print "Model insert_cliente Error ()".format(e.args)
		print "Model insert_cliente Message {}".format(e.message)
		return None

"""
metodo para eliminar productos
"""

def delete_cliente(nombre):
	try:
		return db.delete('clientes', where = 'nombre=$nombre', vars=locals())
	except Exception as e:
		print "Model delete_cliente Error ()".format(e.args)
		print "Model delete_cliente Message {}".format(e.message)
		return None

def update_cliente(nombre, direccion, sexo, correo):
	try:
		return db.update('clientes',
			direccion = direccion,
			sexo = sexo,
			correo = correo,
			where = 'nombre=$nombre',
			vars=locals())
	except Exception as e:
		print "Model update_clientes Error ()".format(e.args)
		print "Model update_clientes Message {}".format(e.message)
		return None

def update_clientes(nombre, direccion, sexo,correo): # actualiza los datos de la tabla clientes que coincidan con el nombre
    try:
        return db.update('clientes',
            direccion=direccion,
            sexo=sexo,
            correo=correo, 
            where='nombre=$nombre',
            vars=locals())
    except Exception as e:
        print "Model update_clientes Error {}".format(e.args)
        print "Model update_clientes Message {}".format(e.message)
        return None

