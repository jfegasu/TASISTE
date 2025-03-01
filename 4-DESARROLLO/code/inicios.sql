USE HR
create user if not exists 'prueba'@'localhost' identified by 'prueba';
create user if not exists 'juanchotv123'@'localhost' identified by '123';
create user if not exists 'admin'@'localhost' identified by 'admin';

grant select,insert,update,delete ON hr.* TO 'admin'@'localhost';

--set password for 'admin'@'localhost'=PASSWORD('123');






