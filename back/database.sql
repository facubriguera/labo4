CREATE DATABASE tpi;
USE tpi;
CREATE TABLE inscriptions (inscrip_id INT, event_id INT, user_id INT, fecha_inscripcion DATE, PRIMARY KEY(inscrip_id));
CREATE TABLE users (user_id INT AUTO_INCREMENT, name VARCHAR(50), email VARCHAR(50) UNIQUE, password VARCHAR(40), rol ENUM('Cliente','Administrador'), PRIMARY KEY(user_id));
CREATE TABLE categories (cat_id INT AUTO_INCREMENT;, nombre VARCHAR(50) UNIQUE, descripcion VARCHAR(100), PRIMARY KEY(cat_id));
CREATE TABLE events (event_id INT, name VARCHAR(50), description VARCHAR(200), fecha_inicio DATE, fecha_fin DATE, lugar VARCHAR(50), cupos INT, cat_id INT, PRIMARY KEY(event_id));
ALTER TABLE inscriptions ADD CONSTRAINT fk_event FOREIGN KEY(event_id) REFERENCES events(event_id);
ALTER TABLE inscriptions ADD CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES users(user_id);
ALTER TABLE events ADD CONSTRAINT fk_cat FOREIGN KEY(cat_id) REFERENCES categories(cat_id);
