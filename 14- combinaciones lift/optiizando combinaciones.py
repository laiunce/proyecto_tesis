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


directorio = '/Users/laiunce/Google Drive/scraping/prueba busqueda lift/'
datos=pd.read_csv(directorio+'dataset3.csv',encoding='latin-1',low_memory=False)



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


#list(itertools.combinations(a[0],5))


#calcula ratios y cantidades generales

agg_total =datos['monto'].groupby(datos['no pago']).sum()
agg_qty_total =sum(datos['monto'].groupby(datos['no pago']).count())
ratio_gral= agg_total[1]/(sum(agg_total))


#estas son las variables del dataset, menos la objetio
valores_itera = list(datos)[0:-2]

dataframe_nuevas_col = datos[['monto','no pago']].copy()


lista_variables_datos = []
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
            

    
    for i in lista_combinaciones:
        lis_tmp = []
        lis_tmp.append(ev+'_'+'_'.join(i))
        lis_tmp.append(i)   
        lista_variables_datos.append(lis_tmp)
        #dataframe_nuevas_col[ev+'_'+'_'.join(i)] = datos[ev].apply(lambda x: coincide(x,i))


     
#ahora hace combinaciones con demas variables, si es la misma,nola toma en cuenta

#por cada variable se hace una lista, para que la cominacion entre variables no tenga en cuenta masde una posibilidad de cada subdivision de la variable
array_bina=[]
for var in valores_itera:
    lista2=[]
    for v2 in lista_variables_datos:
        if var in v2[0]:
            lista2.append(v2[0])
    array_bina.append(lista2)


#---------> CUELLO de botella!!!!!
# Aca calcula todas las combinaciones posible tomando de a 1 subdivision de cada variable, tomadas de a 1, 2...etc respecto de la cantidad de variables que haya inicialmente
producto_array_bina = list(itertools.product(*array_bina))

producto_array_bina[3]

#ahora combinaciones tomadas de a 1,2,3 etc por cada fila y eliminar duplicados

with open(directorio+'salida_filtros.txt','w') as f:
    f.write('filtro;ratio;lift;qty;share_qty;monto;share_monto'+'\n')
    #hace todas las combinaciones posibiles dentro de cada grupo y elimina duplicados ya que es un algoritmo redundante
    lista_combinaciones_gral = []
    #filtros = []
    contador= 0
    for ab in producto_array_bina:  
        contador+=1
        print (contador)
        for num in range(1,len(ab)+1):
            apen=list(itertools.combinations(ab,num))
            for b in range(0,len(apen)):
                if list(apen[b]) not in lista_combinaciones_gral:
                    com=list(apen[b])
                    lista_combinaciones_gral.append(com)
                    #impre filtros en archivo on streaming
                    texto_filtro=''
                    for i in com:
                        for v in valores_itera:
                            if v in i:
                                texto_filtro+=(v +' in (\''+(i.replace(v,'')[1:]).replace('_','\',\'')+'\') and ')
                    texto_filtro_app = texto_filtro[:-5]
                    
                    #calcula metricas

                    df_filtered = datos.query(texto_filtro_app)    
                    agg =df_filtered['monto'].groupby(datos['no pago']).sum()
                    agg_qty =df_filtered['monto'].groupby(datos['no pago']).count()
                    ratio=9999
                    try:
                        ratio= agg[1]/(sum(agg))
                                               
                    except:
                        pass                    
                    
                    
                    #filtros.append(texto_filtro_app)  
                    
                    f.write(texto_filtro_app+';'+str(round(ratio,3))+';'+str(round(ratio/ratio_gral,3))+';'+str(round(sum(agg_qty),3))+';'+str(round(sum(agg_qty)/agg_qty_total,3))+';'+str(round(sum(agg),3))+';'+str(round(sum(agg)/sum(agg_total),3))+'\n')
    
    
    #if contador == 1000:
    #print(str(len(lista_combinaciones_gral))+' - '+str(contador))    


#modifcar para que lea archivo y vaya calculando o que la funcion anterior
#devuelva real time para quevaya calculando y guardando metricas


#imprime metricas 

#control

i="var_e in ('S') and var_h in ('g')"
df_filtered = datos.query(i)    
agg =df_filtered['monto'].groupby(datos['no pago']).sum()
agg_qty =df_filtered['monto'].groupby(datos['no pago']).count()
ratio=9999
ratio= agg[1]/(sum(agg))
    
    print(i+' '+str(ratio)+' lift: '+str(ratio/ratio_gral)+' qty: '+str(sum(agg_qty))+' share: '+str(sum(agg_qty)/agg_qty_total))  
except:
    pass
'''    