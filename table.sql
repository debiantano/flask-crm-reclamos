CREATE TABLE reclamos(
    id_reclamo int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fecha varchar(50),
    dni varchar(50),
    nombre varchar(50),
    apellido varchar(50),
    ciudad varchar(50),
    correo varchar(50),
    telefono varchar(50),
    direccion varchar(50),
    departamento varchar(50),
    tipo_reclamo varchar(50),
    subtipo varchar(50),
    mensaje varchar(255),
    estado varchar(50)
)
