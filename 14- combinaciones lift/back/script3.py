#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 00:31:24 2018

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



datos=pd.read_csv('/Users/laiunce/Desktop/prueba busqueda lift/dataset.csv',encoding='latin-1',low_memory=False)

calc_ratio_df = datos
agg =calc_ratio_df['monto'].groupby(calc_ratio_df['no pago']).sum()
ratio_gral= agg[1]/(sum(agg))


valores_itera = list(datos)[0:3]


#de cada columna hacer combinaciones entre si
#luego recorrer tomados de a tantas columnas como tenga el dataset

df_llenar = pd.DataFrame( columns=list(datos)[0:3])

lista_combinaciones=[]
for num in range(1,len(valores_itera)+1):
    apen=list(itertools.combinations(valores_itera,num))
    for b in range(0,len(apen)):
        print(b)
        lista_combinaciones.append(list(apen[b]))


for combi in lista_combinaciones:
    text_eval = ''
    for ev in combi:
        text_eval+='datos.'+ev+'.unique(),'
    a=eval('['+text_eval[:-1]+']')
    lista_pos=list(itertools.product(*a))
    tmp_df = pd.DataFrame(lista_pos)
    tmp_df.columns = combi
    print(tmp_df)

    df_llenar = pd.concat([df_llenar,tmp_df])


 ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####  



filtros = []
for index, row in df_llenar.iterrows():
    texto_filtro=''
    for nom in valores_itera:
        if pd.isnull(row[nom]) == False:
            texto_filtro+=nom+" == '"+row[nom]+"' and "
    print(texto_filtro[:-5])
    filtros.append(texto_filtro[:-5])
    

# AGREGAR MONTO Y CANTIDAD!!!!1 HACER LISTAS Y AGREGARLOS AL FINAL DEL DATAFRAME, AGREGAR POR PERIODO DE TIEMPO UNA TENDENCIA
for i in filtros:
    df_filtered = datos.query(i)    
    calc_ratio_df = df_filtered
    agg =calc_ratio_df['monto'].groupby(calc_ratio_df['no pago']).sum()
    ratio=9999
    try:
        ratio= agg[1]/(sum(agg))
        print(i+' '+str(ratio)+' lift: '+str(ratio/ratio_gral))
    except:
        pass
    


    
   
   
   
   
   
   