#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 22:51:09 2018

@author: laiunce
"""

directorio ='/Users/laiunce/Google Drive/scraping/8- robot baja series historicas/acciones_arg'


import os
import glob

os.chdir(directorio)
result = glob.glob( '**.csv' )

archivo_salida = '/Users/laiunce/Google Drive/scraping/9-carga tablas/salida_script.csv'

fd = open(archivo_salida ,'a')


for a in result:
        
    nom_csv = a[:-4]
    nom_tabla = nom_csv.replace('-','_').replace('.','')
    
    fd.write('drop table IF EXISTS merval.'+nom_tabla+';')
    fd.write('\n')    
    fd.write('CREATE TABLE merval.'+nom_tabla+' (fecha int(20), ultima float(20),apertura float(20),maximo float(20),minimo float(20),vol float(20),varianza float(20));')
    fd.write('\n')
    fd.write('LOAD DATA LOCAL INFILE')
    fd.write('\n')
    fd.write('\'/Users/laiunce/Google Drive/scraping/8- robot baja series historicas/acciones_arg/'+nom_csv+'.csv\'')
    fd.write('\n')
    fd.write('INTO TABLE merval.'+nom_tabla+'')
    fd.write('\n')
    fd.write('FIELDS TERMINATED BY \',\' ')
    fd.write('\n')
    fd.write('ENCLOSED BY \'"\' LINES TERMINATED BY \'\n\'')
    fd.write('\n')
    fd.write('IGNORE 1 LINES')
    fd.write('\n')
    fd.write('(fecha,ultima,apertura,maximo,minimo,vol,varianza)')
    fd.write('\n')
    fd.write(';')
    fd.write('\n')
    fd.write('CREATE INDEX fecha ON merval.'+nom_tabla+'  (fecha) USING BTREE;')
    fd.write('\n')
    fd.write('delete from merval.'+nom_tabla+' where length(fecha) = 4;')
    fd.write('\n')
    fd.write('\n')
    fd.write('\n')

fd.close()