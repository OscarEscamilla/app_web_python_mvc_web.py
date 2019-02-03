create database ria_iniciales2;

use ria_iniciales2;


create table productos(
id_producto int auto_increment primary key,
nombre varchar(20) not null ,
marca varchar(20) not null ,
precio float(4) not null,
descripcion varchar(20) not null);

insert into productos values
	(null,'Laptop','hp',8000,'Color plata'),
	(null,'Audifonos','sony',200,'Negros'),
	(null,'Router','TP-link',400,'Blanco');

create table clientes(
id_cliente int auto_increment primary key,
nombre varchar(20) not null ,
direccion varchar(20) not null ,
sexo varchar(10) not null,
correo varchar(20) not null);


insert into clientes values
	(null,'Oscar','Jaltepec','M','oscar@gmail.com'),
	(null,'Alondra','Acatlan','F','alondra@gmail.com'),
	(null,'Deniss','Tulanicingo','F','alondra@gmail.com');


select * from productos;
select * from clientes;

CREATE USER 'oscar_user'@'localhost' IDENTIFIED BY 'oscar.2019';
Grant ALL PRIVILEGES ON ria_iniciales2.* TO'oscar_user'@'localhost';
FLUSH PRIVILEGES;
