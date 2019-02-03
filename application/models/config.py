import web 



db = web.database(
	dbn = 'mysql',  # motor de base de datos
	host = 'localhost',
	db = 'ria_iniciales2',
	user = 'oscar_user',
	pw = 'oscar.2019', # contrasena
	port = 3306 #puerto de mariadb
	)
