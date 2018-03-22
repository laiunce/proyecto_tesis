#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 23:54:39 2017

@author: laiunce
"""

#http://www.bcra.gob.ar/PublicacionesEstadisticas/Principales_variables.asp?FechaCons=03/01/2018


from bs4 import BeautifulSoup
import requests
import bs4
import re
import pandas as pd
import numpy as np

directorio = '/Users/laiunce/Desktop/scraping/'


generica = []

# itera
#for a in ['2017']:
    
for a in ['2014','2015','2016','2017','2018']:
    for m in ['01','02','03','04','05','06','07','08','09','10','11','12']:
        for d in ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']:

            
#for a in ['2017']:
#    for m in ['01']:
#        for d in ['01','02','03','04']:
            
            fecha = (a+m+d)
            print(fecha)
            try:
                
                
                str(fecha)[6:8]
                
                fecha_format = str(fecha)[6:8]+'/'+str(fecha)[4:6]+'/'+str(fecha)[0:4]
                
                page = requests.get('http://www.bcra.gob.ar/PublicacionesEstadisticas/Principales_variables.asp?FechaCons='+fecha_format)
                soup = bs4.BeautifulSoup(page.text)
                
                #obtiene el nro de pagina maximo para iterar de 1 hasta el nro maximo de paginas y asi traer toda la info
                
                paginas=[]
                paginas= re.findall(r'<td style="text-align:right">.*<' ,str(soup))
                
                lista=[]
                lista.append(fecha)
                for i in paginas:
                    p =re.findall(r'>.*<' ,i)
                    b = (p[0].replace("\xa0<", "").replace("<", "").replace(">", "").replace(".", "").replace(",", ".").replace("N/D", ""))
                    lista.append(b)
                
                generica.append(lista)
            except:
                pass


# fin itera

df = pd.DataFrame(generica)
df.columns = ['fecha','uva','uvi','reservas_internacionales','base_monetaria','circulacion_monetaria','billetes_monedas_poder_publico','efectivo_entidades_financieras','deposito_bancos_cta_cte_pesos','lebac_efectivo','lebac_nominal','deposito_efectivo_entidades_financieras','en_cte_fuco','caja_ahorro','a_plazo','m2_privado_prom_movil_30_dias_var_internanual','tasas_interes_lebac_35_dias','tasas_interes_activas_bcra_1_dia_plazo','tasas_interes_pasivas_bcra_1_dia_plazo','prestamos_entidades_financieras_sector_privado','tasas_interes_por_prestamos_entidades_financieras_privadas','tasas_interes_deposito_30_dias_entidades_financieras','badlar_pesos_bancos_privados','tm20_pesos_bancos_privados','tipo_cambio_referencia','cer_base_222002_igual_1']


