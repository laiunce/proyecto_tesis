#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 23:23:14 2017

@author: laiunce
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot
from matplotlib import pyplot


def normalizar(lista):
    for i in range(0,len(lista)):
        lista[i] =(round((lista[i]-min(lista))/(max(lista)-min(lista)),5))
    return lista



directorio = '/Users/laiunce/Desktop/scraping/'

accion ='PAM.N'

df = pd.read_csv(directorio+'2 - lee datos empresas/datasets/'+accion+'.csv')

df = df.sort_values(['FECHA'])



#df[1972:1988]

lista_apertura = df['APERTURA'].values.tolist()
lista_cierre = df['ULTIMO'].values.tolist()
lista_promedio_dia = []

#crea lista con promedio de apertura y cierre de la accion del dia
for i in range(0,len(lista_apertura)):
    lista_promedio_dia.append((round(((lista_apertura[i]+lista_cierre[i])/2),5)))




#si el valoar es cero lo reemplaza por la media entre los valores anterior y posterior
for i in range(0,len(lista_promedio_dia)):
    if lista_promedio_dia[i] == 0:
        lista_promedio_dia[i] = (round((lista_promedio_dia[i-1]+lista_promedio_dia[i+1])/2,5))
        


lista_promedio_dia_normalizada = normalizar(lista_promedio_dia)
#lista_apertura_normalizada = lista_apertura


#hace lista de pendientes normalizadas haciendo regresgion con los siguientes 5 valores
lista_pendiente_tendencias = []
for i in range(0,len(lista_promedio_dia_normalizada)-5):
    lista_tendencia = [lista_promedio_dia_normalizada[i+1],lista_promedio_dia_normalizada[i+2],lista_promedio_dia_normalizada[i+3],lista_promedio_dia_normalizada[i+4],lista_promedio_dia_normalizada[i+5]]

    X = [i for i in range(0, len(lista_tendencia))]
    X = np.reshape(X, (len(X), 1))
    y = lista_tendencia
    model = LinearRegression()
    model.fit(X, y)
    # calculate trend
    trend = model.predict(X)
    
    ordenada = trend[0]
    
    pendiente = (trend[1]-ordenada)
    
    if abs(pendiente) < 0.0001:
        pendiente=0
    #para sacarle el exponencial
    
    lista_pendiente_tendencias.append(round(pendiente,5))
    
max(lista_pendiente_tendencias)    

#completa ultmios 5 con 0 para que machee por cantidad

for i in range(0,5):
    lista_pendiente_tendencias.append(0.0)



df_tendencias = pd.DataFrame(lista_pendiente_tendencias)
df_tendencias.columns = ['tendencia']

df_prom_ap_cierre=pd.DataFrame(lista_promedio_dia_normalizada)
df_prom_ap_cierre.columns = ['prom_ap_cierre']


#se pasa a lista y a df por tema index, queda el original ymachea cualquier cosa or orden de fechas

bigdata = pd.concat([pd.DataFrame(df['FECHA'].values.tolist()),df_prom_ap_cierre,df_tendencias], axis=1)

bigdata.to_csv(directorio+'3 - tendencia futura/dataset/'+accion+'.csv',index = False)





