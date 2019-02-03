import web 

urls = (
	'/','application.controllers.productos.home.Home',
	'/productos', 'application.controllers.productos.index.Index',
	'/insert', 'application.controllers.productos.insert.Insert',
	'/update/(.*)', 'application.controllers.productos.update.Update',
	'/delete/(.*)', 'application.controllers.productos.delete.Delete',
	'/view/(.*)', 'application.controllers.productos.view.View',

	'/clientes', 'application.controllers.clientes.index.Index',
	'/insertcli', 'application.controllers.clientes.insert.Insert',
	'/updatecli/(.*)', 'application.controllers.clientes.update.Update',
	'/deletecli/(.*)', 'application.controllers.clientes.delete.Delete',
	'/viewcli/(.*)', 'application.controllers.clientes.view.View',



	)


if __name__ == "__main__":
	web.config.debug = False
	app = web.application(urls, globals())
	app.run()