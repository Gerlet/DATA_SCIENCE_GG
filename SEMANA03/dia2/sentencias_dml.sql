-- sentencias DML
-- CRUD
-- CREAR REGISTROS
insert into alumno(nombre,email,celular,nota)
values ('Cesar','cesar@gmail.com','8979879879',12);

insert into alumno(nombre,email,nota)
values
('ana','ana@gmail.com',15),
('luis','ana@gmail.com',11),
('jose','ana@gmail.com',20),
('pedro','ana@gmail.com',13),
('carmen','ana@gmail.com',18);
-- LEER DATOS
select * from alumno;
select nombre,email from alumno;
select nombre,nota from alumno order by nota desc;
select nombre,nota from alumno
where nota >= 15;
select nombre from alumno
where nombre like 'c%'
select * from alumno where id = 1;
-- ACTUALIZAR DATOS
update alumno
set celular = '888888'
where nota >= 15
update alumno
set nombre = 'Cesar Mayta',email='cesarmayta@codigo.edu.pe'
where id = 1;
-- ELIMINAR DATOS
delete from alumno 
where id = 3;








