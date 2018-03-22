CREATE SCHEMA `merval` DEFAULT CHARACTER SET utf8 ;

SET SQL_SAFE_UPDATES = 0;

quitar limite 1000 lineas

opcion de que continue a pesar de warnings

SET GLOBAL LOG_WARNINGS = 1
################################################################################


drop table IF EXISTS merval.invertironline_pampa_energia;
CREATE TABLE merval.invertironline_pampa_energia (fecha int(20), ultima float(20),apertura float(20),maximo float(20),minimo float(20));


LOAD DATA LOCAL INFILE 
'/Users/laiunce/Google Drive/scraping/8- robot baja series historicas/bajada de invertironline/bajada/PAMP.csv' 
INTO TABLE merval.invertironline_pampa_energia 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' LINES TERMINATED BY '\n'
IGNORE 1 LINES
(fecha,apertura,maximo,minimo,ultima)
;

CREATE INDEX fecha ON merval.invertironline_pampa_energia  (fecha) USING BTREE;


#delete from merval.pampa_energia where length(fecha) = 4;


nom_csv =
nom_tabla =