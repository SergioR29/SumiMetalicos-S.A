BEGIN TRANSACTION;
DROP TABLE IF EXISTS "articulos";
CREATE TABLE `articulos` (
  `Id_articulo` INTEGER PRIMARY KEY AUTOINCREMENT,
  `Descripcion` varchar(45) NOT NULL,
  `Precio` decimal(10,2) NOT NULL);
DROP TABLE IF EXISTS "clientes";
CREATE TABLE `clientes` (
  `ID_Cliente` INTEGER PRIMARY KEY AUTOINCREMENT,
  `Nombre` varchar(80) NOT NULL,
  `Direccion` varchar(80) NOT NULL,
  `Ciudad` varchar(80) NOT NULL);
DROP TABLE IF EXISTS "detalle_pedidos";
CREATE TABLE `detalle_pedidos` (
  `ID_Venta` INTEGER PRIMARY KEY AUTOINCREMENT,
  `ID_Articulo` INTEGER NOT NULL,
  `Precio` decimal(10,2) NOT NULL,
  `Unidades` INTEGER NOT NULL,
  `ID_Pedido` INTEGER NOT NULL,
   CONSTRAINT `ID_ARTICULO_FK` FOREIGN KEY (`ID_Articulo`) REFERENCES `articulos` (`Id_articulo`) ON UPDATE CASCADE,
   CONSTRAINT `ID_PEDIDO_FK` FOREIGN KEY (`ID_Pedido`)   REFERENCES `pedidos` (`ID_Pedido`) ON UPDATE CASCADE);
CREATE INDEX `ID_PEDIDO_FK` ON `detalle_pedidos` (`ID_Pedido`);
CREATE INDEX `ID_ARTICULO_FK` ON `detalle_pedidos` (`ID_Articulo`) ;
DROP TABLE IF EXISTS "emails";
CREATE TABLE `emails` (
  `Id_cliente` INTEGER NOT NULL,
  `Email` varchar(200) NOT NULL,
  PRIMARY KEY (`Id_cliente`,`Email`),
  CONSTRAINT `ID_cliente_email_FK` FOREIGN KEY (`Id_cliente`) REFERENCES `clientes` (`ID_Cliente`));
DROP TABLE IF EXISTS "pedidos";
CREATE TABLE `pedidos` (
  `ID_Pedido` INTEGER PRIMARY KEY AUTOINCREMENT,
  `ID_Cliente` INTEGER DEFAULT NULL,
  `Fecha_Pedido` datetime NOT NULL,
   CONSTRAINT `ID_CLIENTES_FK` FOREIGN KEY (`ID_Cliente`) REFERENCES `clientes` (`ID_Cliente`) ON UPDATE CASCADE);
  
CREATE INDEX `ID_Cliente` ON `pedidos` (`ID_Cliente`);

DROP TABLE IF EXISTS "telefonos";
CREATE TABLE `telefonos` (
  `Id_Cliente` INTEGER NOT NULL,
  `Telefono` varchar(12) NOT NULL,
  `Persona_Contacto` varchar(80) NOT NULL,
   PRIMARY KEY (`Id_Cliente`,`Telefono`),
   CONSTRAINT `ID_Cliente_FK` FOREIGN KEY (`Id_Cliente`) REFERENCES `clientes` (`ID_Cliente`) ON UPDATE CASCADE

);
INSERT INTO "articulos" ("Id_articulo","Descripcion","Precio") VALUES (1,'Anclaje andamios',16),
 (2,'Angulo PVC Negro 15mm x 15mm 1M ',15.75),
 (3,'Taco clavo',2.57),
 (4,'Taco con tornillo 100 Piezas',24.81),
 (5,'Taco 6x50 100 Piezas',9.32),
 (6,'Clavo 65mm x 200 mm',1),
 (7,'Tubo Hierro Forjado 70 x 105',1.54);
INSERT INTO "clientes" ("ID_Cliente","Nombre","Direccion","Ciudad") VALUES (1,'Ferretería Almendralejo S.L','Carretera de Badajoz, nº 181','Almendralejo'),
 (2,'Ferretería La Madrila S.L','Parque del Príncipe, nº 18','Cáceres'),
 (3,'Ferretería Lavapies','Calle Canarias, Nº 89','Madrid'),
 (4,'Ferretería Ramirez','Calle Pizarro, nº 78','Sevilla'),
 (5,'Bricos Hierro','Calle La Piedad, nº 5','Salamanca'),
 (6,'Hierros Salmantina','Calle Gran Vía, nº 13','Madrid'),
 (7,'Armaduras de Hierro','Avenida Almonte, nº 59','Santander');
INSERT INTO "detalle_pedidos" ("ID_Venta","ID_Articulo","Precio","Unidades","ID_Pedido") VALUES (1,1,16,102,1),
 (2,2,15.75,405,1),
 (3,7,1.54,1080,1),
 (4,1,16,395,2),
 (5,3,2.57,99,2),
 (6,6,1,125,2),
 (7,4,24,580,3),
 (8,5,9.32,76,3),
 (9,6,3,87,4),
 (10,7,1.54,8,4),
 (11,7,1.54,10,5),
 (12,3,2.57,6,5),
 (13,1,1,5,4),
 (14,7,1.54,5,4);
INSERT INTO "emails" ("Id_cliente","Email") VALUES (1,'piedad.coranado@almenfer.es'),
 (2,'madrila.caceres@lamadrilacaceres,es'),
 (3,'ferlava@lavapiesferr.es'),
 (4,'triana@ferramirez.es'),
 (6,'ana.tejuan@salmantina.es'),
 (6,'misabel.tejuan@salmantina.es'),
 (7,'manuel.roldan@armadurashierro.com'),
 (7,'rrhh@armadurashierro.com');
INSERT INTO "pedidos" ("ID_Pedido","ID_Cliente","Fecha_Pedido") VALUES (1,1,'2019-12-09 10:17:00'),
 (2,1,'2019-01-01 08:06:00'),
 (3,2,'2019-11-12 13:13:00'),
 (4,2,'2018-01-02 17:09:00'),
 (5,3,'2018-11-04 10:09:00'),
 (6,4,'2017-11-04 15:05:00');
INSERT INTO "telefonos" ("Id_Cliente","Telefono","Persona_Contacto") VALUES (1,'924660001','Piedad Espronceda '),
 (2,'924314959','David Rodríguez'),
 (3,'91333444','José Luis Pérez'),
 (4,'955123987','Ramón Montero'),
 (4,'955123988','Francisco Ramírez'),
 (6,'91340340','María Isabel Tejuán'),
 (6,'91341341','Ana María Tejuán'),
 (7,'942661570','Manuel Roldán'),
 (7,'942661571','Ana Roldán');
COMMIT;
