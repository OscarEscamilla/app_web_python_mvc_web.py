import config as config

db = config.db #accede al archivo config y al objeto db

"""
metodo para seleccionar todos los registros
"""
 

def select_productos():
    try:
        return db.select('productos') # Selecciona todos los registros de la tabla clientes
    except Exception as e:
        print "Model select_productos Error {}".format(e.args)
        print "Model select_productos Message {}".format(e.message)
        return None


"""
metodo para seleccionar solo el registro que coicida con el nombre
"""

def select_nombre(nombre):
	try:
		return db.select('productos', where = 'nombre=$nombre', vars=locals())[0] #selecciona el primer registro que coincida con el nombre dado en el parametro
	except Exception as e:
		print "Model select_nombre Error ()".format(e.args)
		print "Model select_nombre Message {}".format(e.message)
		return None

""" 
metodo para insertar productos
"""

def insert_producto(nombre, marca, precio,  descripcion):
	try:
		return db.insert('productos', 
			nombre = nombre,
			marca = marca,
			precio = precio,
			descripcion = descripcion)
	except Exception as e:
		print "Model insert_producto Error ()".format(e.args)
		print "Model insert_producto Message {}".format(e.message)
		return None

"""
metodo para eliminar productos
"""

def delete_producto(nombre):
	try:
		return db.delete('productos', where = 'nombre=$nombre', vars=locals())
	except Exception as e:
		print "Model delete_producto Error ()".format(e.args)
		print "Model delete_producto Message {}".format(e.message)
		return None

"""
Metodo para actualizar productos

"""

def update_producto(nombre, marca, precio,  descripcion):
	try:
		return db.update('productos',
			precio = precio,
			marca = marca,
			descripcion = descripcion,
			where = 'nombre=$nombre',
			vars=locals())
	except Exception as e:
		print "Model update_producto Error ()".format(e.args)
		print "Model update_producto Message {}".format(e.message)
		return None




		

