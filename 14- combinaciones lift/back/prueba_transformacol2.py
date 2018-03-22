#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 20:35:43 2018

@author: laiunce
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import plotly.plotly as py
from sklearn import datasets, linear_model
import itertools

def coincide(x,lista):
    if x in lista:
        return 1
    else:
        return 0


datos=pd.read_csv('/Users/laiunce/Google Drive/scraping/prueba busqueda lift/dataset.csv',encoding='latin-1',low_memory=False)


#identifica variables continuas
lista_continuos=[]
for var in list(datos)[0:-2]:
    try:
        sum(np.unique(datos[var]))
        lista_continuos.append(var)
    except:
        pass




calc_ratio_df = datos




agg =calc_ratio_df['monto'].groupby(calc_ratio_df['no pago']).sum()
agg_qty_total =sum(calc_ratio_df['monto'].groupby(calc_ratio_df['no pago']).count())
ratio_gral= agg[1]/(sum(agg))

valores_itera = list(datos)[0:-2]



dataframe_nuevas_col = datos[['monto','no pago']]


#por cada columna binariza combinaciones posible dentro de cada variable
for ev in valores_itera:

    text_eval = ''
    text_eval+='datos.'+ev+'.unique(),'
    a=eval('['+text_eval[:-1]+']')
    
    
    #combinaciones tomadas del total menos uno para no hacer una columna que contenga todas las posibilidades
    lista_combinaciones=[]
    for num in range(1,len(a[0])):
        apen=list(itertools.combinations(a[0],num))
        for b in range(0,len(apen)):
            lista_combinaciones.append(list(apen[b]))
            
    
    for i in lista_combinaciones:
        dataframe_nuevas_col[ev+'_'+'_'.join(i)] = datos[ev].apply(lambda x: coincide(x,i))

     
#ahora hace combinaciones con demas variables, si es la misma,nola toma en cuenta


array_bina=[]
for var in valores_itera:
    lista2=[]
    for v2 in list(dataframe_nuevas_col):
        if var in v2:
            lista2.append(v2)
    array_bina.append(lista2)

producto_array_bina = list(itertools.product(*array_bina))

#ahora combinaciones tomadas de a 1,2,3 etc por cada fila y eliminar duplicados


lista_combinaciones_gral  =[]

for ab in producto_array_bina:    
    for num in range(1,len(ab)+1):
        apen=list(itertools.combinations(ab,num))
        for b in range(0,len(apen)):
            lista_combinaciones_gral.append(list(apen[b]))



#lista de combinaciones a realizar
unicos = np.unique(lista_combinaciones_gral)

#for u in unicos:
#    print (u)


filtros = []
for u in unicos:
    texto_filtro=''
    for i in u:
        texto_filtro+=i+" == 1 and "
    filtros.append(texto_filtro[:-5])
    
  
for i in filtros:
    df_filtered = dataframe_nuevas_col.query(i)    
    calc_ratio_df = df_filtered
    agg =calc_ratio_df['monto'].groupby(calc_ratio_df['no pago']).sum()
    agg_qty =calc_ratio_df['monto'].groupby(calc_ratio_df['no pago']).count()
    ratio=9999
    try:
        ratio= agg[1]/(sum(agg))
        if ratio/ratio_gral > 2:
            print(i+' '+str(ratio)+' lift: '+str(ratio/ratio_gral)+' qty: '+str(sum(agg_qty))+' share: '+str(sum(agg_qty)/agg_qty_total))  
    except:
        pass
    