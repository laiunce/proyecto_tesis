#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 12:12:09 2018

@author: laiunce
"""
import pandas as pd
import math
import numpy as np



def calcula_promedios(fecha_ultimo,index,dias_atras,variable_actual):
    if index < dias_atras-1:
        valor=math.nan
    else:        
        try:
            valor= np.mean(fecha_ultimo[index-dias_atras:index][variable_actual])
        except:
            valor=math.nan            
    return (valor)


def calcula_maximos(fecha_ultimo,index,dias_atras,variable_actual):
    if index < dias_atras-1:
        valor=math.nan
    else:        
        try:
            valor= np.max(fecha_ultimo[index-dias_atras:index][variable_actual])
        except:
            valor=math.nan            
    return (valor)

def calcula_minimos(fecha_ultimo,index,dias_atras,variable_actual):
    if index < dias_atras-1:
        valor=math.nan
    else:        
        try:
            valor= np.max(fecha_ultimo[index-dias_atras:index][variable_actual])
        except:
            valor=math.nan            
    return (valor)


def calcula_perentiles(fecha_ultimo,index,dias_atras,variable_actual):
    if index < dias_atras-1:
        valor=math.nan
    else:        
        try:
            valor= np.percentile(fecha_ultimo[index-dias_atras:index][variable_actual], dias_atras)
        except:
            valor=math.nan  
    return (valor)

directorio = '/Users/laiunce/Google Drive/scraping/11- creacion dataset/'


data=pd.read_csv(directorio+'dataset.csv')


for i in list(data)[1:]:
    print(i)
        
    variable_actual= i
    fecha_ultimo = data[['fecha',variable_actual]]
    
    
    
    
    
    ################################################################################################
    ##### INICIO
    #------------------------------------------------------------------------------------------------
    
    
    
    lista_anterior = []
    lista_prom3dias = []
    lista_prom5dias = []
    lista_prom10dias = []
    lista_prom15dias = []
    lista_prom20dias = []
    lista_prom25dias = []
    lista_prom30dias = []
    lista_prom60dias = []
    lista_prom90dias = []
    
    lista_percentil10_90dias = []
    lista_percentil20_90dias = []
    lista_percentil30_90dias = []
    lista_percentil40_90dias = []
    lista_percentil50_90dias = []
    lista_percentil60_90dias = []
    lista_percentil70_90dias = []
    lista_percentil80_90dias = []
    lista_percentil90_90dias = []
    
    lista_percentil10_60dias = []
    lista_percentil20_60dias = []
    lista_percentil30_60dias = []
    lista_percentil40_60dias = []
    lista_percentil50_60dias = []
    lista_percentil60_60dias = []
    lista_percentil70_60dias = []
    lista_percentil80_60dias = []
    lista_percentil90_60dias = []
    
    lista_percentil10_30dias = []
    lista_percentil20_30dias = []
    lista_percentil30_30dias = []
    lista_percentil40_30dias = []
    lista_percentil50_30dias = []
    lista_percentil60_30dias = []
    lista_percentil70_30dias = []
    lista_percentil80_30dias = []
    lista_percentil90_30dias = []
    
    lista_percentil10_20dias = []
    lista_percentil20_20dias = []
    lista_percentil30_20dias = []
    lista_percentil40_20dias = []
    lista_percentil50_20dias = []
    lista_percentil60_20dias = []
    lista_percentil70_20dias = []
    lista_percentil80_20dias = []
    lista_percentil90_20dias = []
    
    lista_percentil10_15dias = []
    lista_percentil20_15dias = []
    lista_percentil30_15dias = []
    lista_percentil40_15dias = []
    lista_percentil50_15dias = []
    lista_percentil60_15dias = []
    lista_percentil70_15dias = []
    lista_percentil80_15dias = []
    lista_percentil90_15dias = []
    
    lista_percentil10_10dias = []
    lista_percentil20_10dias = []
    lista_percentil30_10dias = []
    lista_percentil40_10dias = []
    lista_percentil50_10dias = []
    lista_percentil60_10dias = []
    lista_percentil70_10dias = []
    lista_percentil80_10dias = []
    lista_percentil90_10dias = []
    
    lista_percentil10_05dias = []
    lista_percentil20_05dias = []
    lista_percentil30_05dias = []
    lista_percentil40_05dias = []
    lista_percentil50_05dias = []
    lista_percentil60_05dias = []
    lista_percentil70_05dias = []
    lista_percentil80_05dias = []
    lista_percentil90_05dias = []
    
    lista_minimos03dias = []
    lista_minimos05dias = []
    lista_minimos10dias = []
    lista_minimos15dias = []
    lista_minimos20dias = []
    lista_minimos25dias = []
    lista_minimos30dias = []
    lista_minimos60dias = []
    lista_minimos90dias = []
    
    lista_maximos03dias = []
    lista_maximos05dias = []
    lista_maximos10dias = []
    lista_maximos15dias = []
    lista_maximos20dias = []
    lista_maximos25dias = []
    lista_maximos30dias = []
    lista_maximos60dias = []
    lista_maximos90dias = []
    
    for index, row in fecha_ultimo.iterrows():
        
        
    
        ##### CREO DIA ANTERIOR
        try:
            valor= fecha_ultimo.loc[index-1][variable_actual]
        except:
            valor=math.nan
        lista_anterior.append(valor)
    
        ##### Promedios
        lista_prom3dias.append(calcula_promedios(fecha_ultimo,index,3,variable_actual))
        lista_prom5dias.append(calcula_promedios(fecha_ultimo,index,5,variable_actual))
        lista_prom10dias.append(calcula_promedios(fecha_ultimo,index,10,variable_actual))
        lista_prom15dias.append(calcula_promedios(fecha_ultimo,index,15,variable_actual))
        lista_prom20dias.append(calcula_promedios(fecha_ultimo,index,20,variable_actual))
        lista_prom25dias.append(calcula_promedios(fecha_ultimo,index,25,variable_actual))
        lista_prom30dias.append(calcula_promedios(fecha_ultimo,index,30,variable_actual))
        lista_prom60dias.append(calcula_promedios(fecha_ultimo,index,60,variable_actual))
        lista_prom90dias.append(calcula_promedios(fecha_ultimo,index,90,variable_actual))    
        
        ##### Percentiles
        lista_percentil10_90dias.append(calcula_perentiles(fecha_ultimo,index,10,variable_actual))
        lista_percentil20_90dias.append(calcula_perentiles(fecha_ultimo,index,20,variable_actual))
        lista_percentil30_90dias.append(calcula_perentiles(fecha_ultimo,index,30,variable_actual))
        lista_percentil40_90dias.append(calcula_perentiles(fecha_ultimo,index,40,variable_actual))
        lista_percentil50_90dias.append(calcula_perentiles(fecha_ultimo,index,50,variable_actual))
        lista_percentil60_90dias.append(calcula_perentiles(fecha_ultimo,index,60,variable_actual))
        lista_percentil70_90dias.append(calcula_perentiles(fecha_ultimo,index,70,variable_actual))
        lista_percentil80_90dias.append(calcula_perentiles(fecha_ultimo,index,80,variable_actual))
        lista_percentil90_90dias.append(calcula_perentiles(fecha_ultimo,index,90,variable_actual))
        
        lista_percentil10_60dias.append(calcula_perentiles(fecha_ultimo,index,10,variable_actual))
        lista_percentil20_60dias.append(calcula_perentiles(fecha_ultimo,index,20,variable_actual))
        lista_percentil30_60dias.append(calcula_perentiles(fecha_ultimo,index,30,variable_actual))
        lista_percentil40_60dias.append(calcula_perentiles(fecha_ultimo,index,40,variable_actual))
        lista_percentil50_60dias.append(calcula_perentiles(fecha_ultimo,index,50,variable_actual))
        lista_percentil60_60dias.append(calcula_perentiles(fecha_ultimo,index,60,variable_actual))
        lista_percentil70_60dias.append(calcula_perentiles(fecha_ultimo,index,70,variable_actual))
        lista_percentil80_60dias.append(calcula_perentiles(fecha_ultimo,index,80,variable_actual))
        lista_percentil90_60dias.append(calcula_perentiles(fecha_ultimo,index,90,variable_actual))
    
        lista_percentil10_30dias.append(calcula_perentiles(fecha_ultimo,index,10,variable_actual))
        lista_percentil20_30dias.append(calcula_perentiles(fecha_ultimo,index,20,variable_actual))
        lista_percentil30_30dias.append(calcula_perentiles(fecha_ultimo,index,30,variable_actual))
        lista_percentil40_30dias.append(calcula_perentiles(fecha_ultimo,index,40,variable_actual))
        lista_percentil50_30dias.append(calcula_perentiles(fecha_ultimo,index,50,variable_actual))
        lista_percentil60_30dias.append(calcula_perentiles(fecha_ultimo,index,60,variable_actual))
        lista_percentil70_30dias.append(calcula_perentiles(fecha_ultimo,index,70,variable_actual))
        lista_percentil80_30dias.append(calcula_perentiles(fecha_ultimo,index,80,variable_actual))
        lista_percentil90_30dias.append(calcula_perentiles(fecha_ultimo,index,90,variable_actual))
        
        lista_percentil10_20dias.append(calcula_perentiles(fecha_ultimo,index,10,variable_actual))
        lista_percentil20_20dias.append(calcula_perentiles(fecha_ultimo,index,20,variable_actual))
        lista_percentil30_20dias.append(calcula_perentiles(fecha_ultimo,index,30,variable_actual))
        lista_percentil40_20dias.append(calcula_perentiles(fecha_ultimo,index,40,variable_actual))
        lista_percentil50_20dias.append(calcula_perentiles(fecha_ultimo,index,50,variable_actual))
        lista_percentil60_20dias.append(calcula_perentiles(fecha_ultimo,index,60,variable_actual))
        lista_percentil70_20dias.append(calcula_perentiles(fecha_ultimo,index,70,variable_actual))
        lista_percentil80_20dias.append(calcula_perentiles(fecha_ultimo,index,80,variable_actual))
        lista_percentil90_20dias.append(calcula_perentiles(fecha_ultimo,index,90,variable_actual))    
    
        lista_percentil10_15dias.append(calcula_perentiles(fecha_ultimo,index,10,variable_actual))
        lista_percentil20_15dias.append(calcula_perentiles(fecha_ultimo,index,20,variable_actual))
        lista_percentil30_15dias.append(calcula_perentiles(fecha_ultimo,index,30,variable_actual))
        lista_percentil40_15dias.append(calcula_perentiles(fecha_ultimo,index,40,variable_actual))
        lista_percentil50_15dias.append(calcula_perentiles(fecha_ultimo,index,50,variable_actual))
        lista_percentil60_15dias.append(calcula_perentiles(fecha_ultimo,index,60,variable_actual))
        lista_percentil70_15dias.append(calcula_perentiles(fecha_ultimo,index,70,variable_actual))
        lista_percentil80_15dias.append(calcula_perentiles(fecha_ultimo,index,80,variable_actual))
        lista_percentil90_15dias.append(calcula_perentiles(fecha_ultimo,index,90,variable_actual))
    
        lista_percentil10_10dias.append(calcula_perentiles(fecha_ultimo,index,10,variable_actual))
        lista_percentil20_10dias.append(calcula_perentiles(fecha_ultimo,index,20,variable_actual))
        lista_percentil30_10dias.append(calcula_perentiles(fecha_ultimo,index,30,variable_actual))
        lista_percentil40_10dias.append(calcula_perentiles(fecha_ultimo,index,40,variable_actual))
        lista_percentil50_10dias.append(calcula_perentiles(fecha_ultimo,index,50,variable_actual))
        lista_percentil60_10dias.append(calcula_perentiles(fecha_ultimo,index,60,variable_actual))
        lista_percentil70_10dias.append(calcula_perentiles(fecha_ultimo,index,70,variable_actual))
        lista_percentil80_10dias.append(calcula_perentiles(fecha_ultimo,index,80,variable_actual))
        lista_percentil90_10dias.append(calcula_perentiles(fecha_ultimo,index,90,variable_actual))    
        
        lista_percentil10_05dias.append(calcula_perentiles(fecha_ultimo,index,10,variable_actual))
        lista_percentil20_05dias.append(calcula_perentiles(fecha_ultimo,index,20,variable_actual))
        lista_percentil30_05dias.append(calcula_perentiles(fecha_ultimo,index,30,variable_actual))
        lista_percentil40_05dias.append(calcula_perentiles(fecha_ultimo,index,40,variable_actual))
        lista_percentil50_05dias.append(calcula_perentiles(fecha_ultimo,index,50,variable_actual))
        lista_percentil60_05dias.append(calcula_perentiles(fecha_ultimo,index,60,variable_actual))
        lista_percentil70_05dias.append(calcula_perentiles(fecha_ultimo,index,70,variable_actual))
        lista_percentil80_05dias.append(calcula_perentiles(fecha_ultimo,index,80,variable_actual))
        lista_percentil90_05dias.append(calcula_perentiles(fecha_ultimo,index,90,variable_actual))    
        
        ##### minimos
        lista_minimos03dias.append(calcula_minimos(fecha_ultimo,index,3,variable_actual))
        lista_minimos05dias.append(calcula_minimos(fecha_ultimo,index,5,variable_actual))
        lista_minimos10dias.append(calcula_minimos(fecha_ultimo,index,10,variable_actual))
        lista_minimos15dias.append(calcula_minimos(fecha_ultimo,index,15,variable_actual))
        lista_minimos20dias.append(calcula_minimos(fecha_ultimo,index,20,variable_actual))
        lista_minimos25dias.append(calcula_minimos(fecha_ultimo,index,25,variable_actual))
        lista_minimos30dias.append(calcula_minimos(fecha_ultimo,index,30,variable_actual))
        lista_minimos60dias.append(calcula_minimos(fecha_ultimo,index,60,variable_actual))
        lista_minimos90dias.append(calcula_minimos(fecha_ultimo,index,90,variable_actual))  
        
        ##### maximos
        lista_maximos03dias.append(calcula_maximos(fecha_ultimo,index,3,variable_actual))
        lista_maximos05dias.append(calcula_maximos(fecha_ultimo,index,5,variable_actual))
        lista_maximos10dias.append(calcula_maximos(fecha_ultimo,index,10,variable_actual))
        lista_maximos15dias.append(calcula_maximos(fecha_ultimo,index,15,variable_actual))
        lista_maximos20dias.append(calcula_maximos(fecha_ultimo,index,20,variable_actual))
        lista_maximos25dias.append(calcula_maximos(fecha_ultimo,index,25,variable_actual))
        lista_maximos30dias.append(calcula_maximos(fecha_ultimo,index,30,variable_actual))
        lista_maximos60dias.append(calcula_maximos(fecha_ultimo,index,60,variable_actual))
        lista_maximos90dias.append(calcula_maximos(fecha_ultimo,index,90,variable_actual))  
        
    #index=0
    #fecha_ultimo[index-dias_atras-1:index]['ULTIMO']
    
    
    data[variable_actual+'_dia_anterior']=lista_anterior
    
    data[variable_actual+'_prom3dias']=lista_prom3dias
    data[variable_actual+'_prom5dias']=lista_prom5dias
    data[variable_actual+'_prom10dias']=lista_prom10dias
    data[variable_actual+'_prom15dias']=lista_prom15dias
    data[variable_actual+'_prom20dias']=lista_prom20dias
    data[variable_actual+'_prom25dias']=lista_prom25dias
    data[variable_actual+'_prom30dias']=lista_prom30dias
    data[variable_actual+'_prom60dias']=lista_prom60dias
    data[variable_actual+'_prom90dias']=lista_prom90dias
    
    data[variable_actual+'_percentil10_90dias']=lista_percentil10_90dias
    data[variable_actual+'_percentil20_90dias']=lista_percentil20_90dias
    data[variable_actual+'_percentil30_90dias']=lista_percentil30_90dias
    data[variable_actual+'_percentil40_90dias']=lista_percentil40_90dias
    data[variable_actual+'_percentil50_90dias']=lista_percentil50_90dias
    data[variable_actual+'_percentil60_90dias']=lista_percentil60_90dias
    data[variable_actual+'_percentil70_90dias']=lista_percentil70_90dias
    data[variable_actual+'_percentil80_90dias']=lista_percentil80_90dias
    data[variable_actual+'_percentil90_90dias']=lista_percentil90_90dias
    
    data[variable_actual+'_percentil10_60dias']=lista_percentil10_60dias
    data[variable_actual+'_percentil20_60dias']=lista_percentil20_60dias
    data[variable_actual+'_percentil30_60dias']=lista_percentil30_60dias
    data[variable_actual+'_percentil40_60dias']=lista_percentil40_60dias
    data[variable_actual+'_percentil50_60dias']=lista_percentil50_60dias
    data[variable_actual+'_percentil60_60dias']=lista_percentil60_60dias
    data[variable_actual+'_percentil70_60dias']=lista_percentil70_60dias
    data[variable_actual+'_percentil80_60dias']=lista_percentil80_60dias
    data[variable_actual+'_percentil90_60dias']=lista_percentil90_60dias
    
    data[variable_actual+'_percentil10_30dias']=lista_percentil10_30dias
    data[variable_actual+'_percentil20_30dias']=lista_percentil20_30dias
    data[variable_actual+'_percentil30_30dias']=lista_percentil30_30dias
    data[variable_actual+'_percentil40_30dias']=lista_percentil40_30dias
    data[variable_actual+'_percentil50_30dias']=lista_percentil50_30dias
    data[variable_actual+'_percentil60_30dias']=lista_percentil60_30dias
    data[variable_actual+'_percentil70_30dias']=lista_percentil70_30dias
    data[variable_actual+'_percentil80_30dias']=lista_percentil80_30dias
    data[variable_actual+'_percentil90_30dias']=lista_percentil90_30dias
    
    data[variable_actual+'_percentil10_20dias']=lista_percentil10_20dias
    data[variable_actual+'_percentil20_20dias']=lista_percentil20_20dias
    data[variable_actual+'_percentil30_20dias']=lista_percentil30_20dias
    data[variable_actual+'_percentil40_20dias']=lista_percentil40_20dias
    data[variable_actual+'_percentil50_20dias']=lista_percentil50_20dias
    data[variable_actual+'_percentil60_20dias']=lista_percentil60_20dias
    data[variable_actual+'_percentil70_20dias']=lista_percentil70_20dias
    data[variable_actual+'_percentil80_20dias']=lista_percentil80_20dias
    data[variable_actual+'_percentil90_20dias']=lista_percentil90_20dias
    
    data[variable_actual+'_percentil10_15dias']=lista_percentil10_15dias
    data[variable_actual+'_percentil20_15dias']=lista_percentil20_15dias
    data[variable_actual+'_percentil30_15dias']=lista_percentil30_15dias
    data[variable_actual+'_percentil40_15dias']=lista_percentil40_15dias
    data[variable_actual+'_percentil50_15dias']=lista_percentil50_15dias
    data[variable_actual+'_percentil60_15dias']=lista_percentil60_15dias
    data[variable_actual+'_percentil70_15dias']=lista_percentil70_15dias
    data[variable_actual+'_percentil80_15dias']=lista_percentil80_15dias
    data[variable_actual+'_percentil90_15dias']=lista_percentil90_15dias
    
    data[variable_actual+'_percentil10_10dias']=lista_percentil10_10dias
    data[variable_actual+'_percentil20_10dias']=lista_percentil20_10dias
    data[variable_actual+'_percentil30_10dias']=lista_percentil30_10dias
    data[variable_actual+'_percentil40_10dias']=lista_percentil40_10dias
    data[variable_actual+'_percentil50_10dias']=lista_percentil50_10dias
    data[variable_actual+'_percentil60_10dias']=lista_percentil60_10dias
    data[variable_actual+'_percentil70_10dias']=lista_percentil70_10dias
    data[variable_actual+'_percentil80_10dias']=lista_percentil80_10dias
    data[variable_actual+'_percentil90_10dias']=lista_percentil90_10dias
    
    data[variable_actual+'_percentil10_05dias']=lista_percentil10_05dias
    data[variable_actual+'_percentil20_05dias']=lista_percentil20_05dias
    data[variable_actual+'_percentil30_05dias']=lista_percentil30_05dias
    data[variable_actual+'_percentil40_05dias']=lista_percentil40_05dias
    data[variable_actual+'_percentil50_05dias']=lista_percentil50_05dias
    data[variable_actual+'_percentil60_05dias']=lista_percentil60_05dias
    data[variable_actual+'_percentil70_05dias']=lista_percentil70_05dias
    data[variable_actual+'_percentil80_05dias']=lista_percentil80_05dias
    data[variable_actual+'_percentil90_05dias']=lista_percentil90_05dias
    
    data[variable_actual+'_minimos_03dias']=lista_minimos03dias
    data[variable_actual+'_minimos_05dias']=lista_minimos05dias
    data[variable_actual+'_minimos_10dias']=lista_minimos10dias
    data[variable_actual+'_minimos_15dias']=lista_minimos15dias
    data[variable_actual+'_minimos_20dias']=lista_minimos20dias
    data[variable_actual+'_minimos_25dias']=lista_minimos25dias
    data[variable_actual+'_minimos_30dias']=lista_minimos30dias
    data[variable_actual+'_minimos_60dias']=lista_minimos60dias
    data[variable_actual+'_minimos_90dias']=lista_minimos90dias
    
    data[variable_actual+'_maximos_03dias']=lista_maximos03dias
    data[variable_actual+'_maximos_05dias']=lista_maximos05dias
    data[variable_actual+'_maximos_10dias']=lista_maximos10dias
    data[variable_actual+'_maximos_15dias']=lista_maximos15dias
    data[variable_actual+'_maximos_20dias']=lista_maximos20dias
    data[variable_actual+'_maximos_25dias']=lista_maximos25dias
    data[variable_actual+'_maximos_30dias']=lista_maximos30dias
    data[variable_actual+'_maximos_60dias']=lista_maximos60dias
    data[variable_actual+'_maximos_90dias']=lista_maximos90dias

#------------------------------------------------------------------------------------------------
##### FINALIZA 
################################################################################################


data.to_csv(directorio+'/salida_metricas.csv')





#agregar dia siguiente de target y de apertura