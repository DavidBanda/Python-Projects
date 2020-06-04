use proyecto_visitas;

select * from user;

select * from visitas;

delete from visitas where id = 7;

delete from user where id = 7;

UPDATE user SET name='Ruben Alonso Hernandez Chavez' WHERE id=2;

# Profesores

insert into user (id, name, email, access, image_file, password, department) values  (1, 'Angelica Garcia Yañez', 'profesor@blog.com', 0, 'default.png', '$2b$12$MzHHAnISelRydIRCwBUwI.LnU0PBTDSsAVTOOwGOQWSh/8X2wJJoK', 6);

insert into user (id, name, email, access, image_file, password, department) values  (6, 'Bassanetti Villalobos Alonso', 'profesor2@blog.com', 0, 'default.png', '$2b$12$MzHHAnISelRydIRCwBUwI.LnU0PBTDSsAVTOOwGOQWSh/8X2wJJoK', 1);

# Jefes de departamentos

insert into user (id, name, email, access, image_file, password, department) values  (2, 'Ruben Alonso Hernandez Chavez', 'jefe@blog.com', 1, 'default.png', '$2b$12$MzHHAnISelRydIRCwBUwI.LnU0PBTDSsAVTOOwGOQWSh/8X2wJJoK', 0);

insert into user (id, name, email, access, image_file, password, department) values  (7, 'Jose Hernandez Chavez', 'jefe2@blog.com', 1, 'default.png', '$2b$12$MzHHAnISelRydIRCwBUwI.LnU0PBTDSsAVTOOwGOQWSh/8X2wJJoK', 0);

# subdirector

insert into user (id, name, email, access, image_file, password, department) values  (3, 'Pedro Garcia Chavez', 'subdirector@blog.com', 2, 'default.png', '$2b$12$MzHHAnISelRydIRCwBUwI.LnU0PBTDSsAVTOOwGOQWSh/8X2wJJoK', 2);

# gestion

insert into user (id, name, email, access, image_file, password, department) values  (4, 'Susana Maldonado Pedroza', 'gestion@blog.com', 3, 'default.png', '$2b$12$MzHHAnISelRydIRCwBUwI.LnU0PBTDSsAVTOOwGOQWSh/8X2wJJoK', 4);

# admin

insert into user (id, name, email, access, image_file, password, department) values  (5, 'David Aaron Banda Gutierrez', 'admin@blog.com', 4, 'default.png', '$2b$12$MzHHAnISelRydIRCwBUwI.LnU0PBTDSsAVTOOwGOQWSh/8X2wJJoK', 3);
