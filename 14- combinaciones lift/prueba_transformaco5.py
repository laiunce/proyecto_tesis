#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 20:35:43 2018

@author: laiunce
"""
import math
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



def asigna_rago(num,lis_bin):
    lis_bin[0][0]
    for i in lis_bin:
        if math.isnan(i[0]) == True and num<i[1]:
            return (i[2])
        
        if math.isnan(i[0]) == False and math.isnan(i[1]) == False and num>=i[0] and num<i[1]:
            return (i[2])
            
        if math.isnan(i[1]) == True and num>=i[0]:
            return (i[2])
        
def asigna_rango_funcion(dataset,variable):   

    #calculo de percentiles
    percentiles = datos[variable].quantile([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    lis_bin=[]
    for i in range(0,len(percentiles)):
        lis_bin2=[]
    
        if i == 0:
            lis_bin2.append(float('nan'))
            lis_bin2.append(percentiles.iloc[i+1])
            var= ('men'+str(percentiles.iloc[i+1]))
        if i == len(percentiles)-1:
            lis_bin2.append(percentiles.iloc[i])
            lis_bin2.append(float('nan'))  
            var= ('may'+str(percentiles.iloc[i]))
        if i >0 and i < len(percentiles)-1:
            var= (str(percentiles.iloc[i])+'_'+str(percentiles.iloc[i+1]))
            lis_bin2.append(percentiles.iloc[i])
            lis_bin2.append(percentiles.iloc[i+1]) 
        var=var.replace('.','')
        lis_bin2.append(var) 
        lis_bin.append(lis_bin2)
         
    return dataset[variable].apply(lambda x: asigna_rago(x,lis_bin))



datos=pd.read_csv('/Users/laiunce/Google Drive/scraping/prueba busqueda lift/dataset3.csv',encoding='latin-1',low_memory=False)



#identifica variables continuas
lista_continuos=[]
for var in list(datos)[0:-2]:
    try:
        sum(np.unique(datos[var]))
        lista_continuos.append(var)
    except:
        pass
    
#por cada variable continua la asigna al dataset transformada
for i in lista_continuos:
    datos[i] = asigna_rango_funcion(datos,i)


list(itertools.combinations(a[0],5))


#calcula ratios y cantidades generales

agg =datos['monto'].groupby(datos['no pago']).sum()
agg_qty_total =sum(datos['monto'].groupby(datos['no pago']).count())
ratio_gral= agg[1]/(sum(agg))


#estas son las variables del dataset, menos la objetio
valores_itera = list(datos)[0:-2]

dataframe_nuevas_col = datos[['monto','no pago']].copy()


#por cada columna binariza combinaciones posible dentro de cada variable
for ev in valores_itera:

    text_eval='datos.'+ev+'.unique(),'
    a=eval('['+text_eval[:-1]+']')
    
    
    #combinaciones tomadas del total menos uno para no hacer una columna que contenga todas las posibilidades
    lista_combinaciones=[]
    for num in range(1,len(a[0])):
        apen=list(itertools.combinations(a[0],num))
        for b in range(0,len(apen)):
            lista_combinaciones.append(list(apen[b]))
            
    #CUELLO DEBOTELLA
    for i in lista_combinaciones:
        dataframe_nuevas_col[ev+'_'+'_'.join(i)] = datos[ev].apply(lambda x: coincide(x,i))

     
#ahora hace combinaciones con demas variables, si es la misma,nola toma en cuenta

#por cada variable se hace una lista, para que la cominacion entre variables no tenga en cuenta masde una posibilidad de cada subdivision de la variable
array_bina=[]
for var in valores_itera:
    lista2=[]
    for v2 in list(dataframe_nuevas_col):
        if var in v2:
            lista2.append(v2)
    array_bina.append(lista2)


#---------> CUELLO de botella!!!!!
# Aca calcula todas las combinaciones posible tomando de a 1 subdivision de cada variable, tomadas de a 1, 2...etc respecto de la cantidad de variables que haya inicialmente
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

#crealos filtros a aplicar
filtros = []
for u in unicos:
    texto_filtro=''
    for i in u:
        texto_filtro+=i+" == 1 and "
    filtros.append(texto_filtro[:-5])
    
    
    
    
 #imprime metricas 
for i in filtros:
    df_filtered = dataframe_nuevas_col.query(i)    
    datos = df_filtered
    agg =datos['monto'].groupby(datos['no pago']).sum()
    agg_qty =datos['monto'].groupby(datos['no pago']).count()
    ratio=9999
    try:
        ratio= agg[1]/(sum(agg))
        if ratio/ratio_gral > 1.1:
            print(i+' '+str(ratio)+' lift: '+str(ratio/ratio_gral)+' qty: '+str(sum(agg_qty))+' share: '+str(sum(agg_qty)/agg_qty_total))  
    except:
        pass
    