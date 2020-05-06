use proyecto_visitas;

select * from user;

UPDATE user SET name='Ruben Alonso Hernandez Chavez' WHERE id=2;

insert into user (id, name, email, access, image_file, password) values  (1, 'Angelica Garcia Yañez', 'profesor@blog.com', 0, 'default.png', '$2b$12$MzHHAnISelRydIRCwBUwI.LnU0PBTDSsAVTOOwGOQWSh/8X2wJJoK');

insert into user (id, name, email, access, image_file, password) values  (6, 'Bassanetti Villalobos Alonso', 'profesor2@blog.com', 0, 'default.png', '$2b$12$MzHHAnISelRydIRCwBUwI.LnU0PBTDSsAVTOOwGOQWSh/8X2wJJoK');

insert into user (id, name, email, access, image_file, password) values  (2, 'Ruben Alonso Hernandez Chavez', 'jefe@blog.com', 1, 'default.png', '$2b$12$MzHHAnISelRydIRCwBUwI.LnU0PBTDSsAVTOOwGOQWSh/8X2wJJoK');

insert into user (id, name, email, access, image_file, password) values  (3, 'Pedro Garcia Chavez', 'subdirector@blog.com', 2, 'default.png', '$2b$12$MzHHAnISelRydIRCwBUwI.LnU0PBTDSsAVTOOwGOQWSh/8X2wJJoK');

insert into user (id, name, email, access, image_file, password) values  (4, 'Susana Maldonado Pedroza', 'gestion@blog.com', 3, 'default.png', '$2b$12$MzHHAnISelRydIRCwBUwI.LnU0PBTDSsAVTOOwGOQWSh/8X2wJJoK');

insert into user (id, name, email, access, image_file, password) values  (5, 'David Aaron Banda Gutierrez', 'admin@blog.com', 4, 'default.png', '$2b$12$MzHHAnISelRydIRCwBUwI.LnU0PBTDSsAVTOOwGOQWSh/8X2wJJoK');
