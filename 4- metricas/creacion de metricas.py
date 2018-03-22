#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 12:12:09 2018

@author: laiunce
"""
import pandas as pd
import math
import numpy as np



def calcula_promedios(fecha_ultimo,index,dias_atras):
    if index < dias_atras-1:
        valor=math.nan
    else:        
        try:
            valor= np.mean(fecha_ultimo[index-dias_atras:index]['ULTIMO'])
        except:
            valor=math.nan            
    return (valor)


def calcula_maximos(fecha_ultimo,index,dias_atras):
    if index < dias_atras-1:
        valor=math.nan
    else:        
        try:
            valor= np.max(fecha_ultimo[index-dias_atras:index]['ULTIMO'])
        except:
            valor=math.nan            
    return (valor)

def calcula_minimos(fecha_ultimo,index,dias_atras):
    if index < dias_atras-1:
        valor=math.nan
    else:        
        try:
            valor= np.max(fecha_ultimo[index-dias_atras:index]['ULTIMO'])
        except:
            valor=math.nan            
    return (valor)


def calcula_perentiles(fecha_ultimo,index,dias_atras):
    if index < dias_atras-1:
        valor=math.nan
    else:        
        try:
            valor= np.percentile(fecha_ultimo[index-dias_atras:index]['ULTIMO'], dias_atras)
        except:
            valor=math.nan  
    return (valor)




data=pd.read_csv('/Users/laiunce/Google Drive/scraping/2 - lee datos empresas/datasets/PAM.N.csv')


fecha_ultimo = data[['FECHA','ULTIMO']]


#calculo del valor siguiente

#creo columna dia_siguiente donde guardamos el valor de cierre del dia siguiente al observado


################################################################################################
##### INICIO
#------------------------------------------------------------------------------------------------
lista_siguiente1 = []
lista_siguiente2 = []
lista_siguiente3 = []
lista_siguiente4 = []
lista_siguiente5 = []


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
    
    ##### CREO DIA SIGUIENTE
    try:
        valor= fecha_ultimo.loc[index+1]['ULTIMO']
    except:
        valor=math.nan
    lista_siguiente1.append(valor)
    
    ##### CREO DIA+2 SIGUIENTE
    try:
        valor= fecha_ultimo.loc[index+2]['ULTIMO']
    except:
        valor=math.nan
    lista_siguiente2.append(valor)    
    
    ##### CREO DIA+3 SIGUIENTE
    try:
        valor= fecha_ultimo.loc[index+3]['ULTIMO']
    except:
        valor=math.nan
    lista_siguiente3.append(valor) 

    ##### CREO DIA+4 SIGUIENTE
    try:
        valor= fecha_ultimo.loc[index+4]['ULTIMO']
    except:
        valor=math.nan
    lista_siguiente4.append(valor) 

    ##### CREO DIA+5 SIGUIENTE
    try:
        valor= fecha_ultimo.loc[index+5]['ULTIMO']
    except:
        valor=math.nan
    lista_siguiente5.append(valor) 
    

    ##### CREO DIA ANTERIOR
    try:
        valor= fecha_ultimo.loc[index-1]['ULTIMO']
    except:
        valor=math.nan
    lista_anterior.append(valor)

    
    ##### Promedios
    lista_prom3dias.append(calcula_promedios(fecha_ultimo,index,3))
    lista_prom5dias.append(calcula_promedios(fecha_ultimo,index,5))
    lista_prom10dias.append(calcula_promedios(fecha_ultimo,index,10))
    lista_prom15dias.append(calcula_promedios(fecha_ultimo,index,15))
    lista_prom20dias.append(calcula_promedios(fecha_ultimo,index,20))
    lista_prom25dias.append(calcula_promedios(fecha_ultimo,index,25))
    lista_prom30dias.append(calcula_promedios(fecha_ultimo,index,30))
    lista_prom60dias.append(calcula_promedios(fecha_ultimo,index,60))
    lista_prom90dias.append(calcula_promedios(fecha_ultimo,index,90))    
    
    ##### Percentiles
    lista_percentil10_90dias.append(calcula_perentiles(fecha_ultimo,index,10))
    lista_percentil20_90dias.append(calcula_perentiles(fecha_ultimo,index,20))
    lista_percentil30_90dias.append(calcula_perentiles(fecha_ultimo,index,30))
    lista_percentil40_90dias.append(calcula_perentiles(fecha_ultimo,index,40))
    lista_percentil50_90dias.append(calcula_perentiles(fecha_ultimo,index,50))
    lista_percentil60_90dias.append(calcula_perentiles(fecha_ultimo,index,60))
    lista_percentil70_90dias.append(calcula_perentiles(fecha_ultimo,index,70))
    lista_percentil80_90dias.append(calcula_perentiles(fecha_ultimo,index,80))
    lista_percentil90_90dias.append(calcula_perentiles(fecha_ultimo,index,90))
    
    lista_percentil10_60dias.append(calcula_perentiles(fecha_ultimo,index,10))
    lista_percentil20_60dias.append(calcula_perentiles(fecha_ultimo,index,20))
    lista_percentil30_60dias.append(calcula_perentiles(fecha_ultimo,index,30))
    lista_percentil40_60dias.append(calcula_perentiles(fecha_ultimo,index,40))
    lista_percentil50_60dias.append(calcula_perentiles(fecha_ultimo,index,50))
    lista_percentil60_60dias.append(calcula_perentiles(fecha_ultimo,index,60))
    lista_percentil70_60dias.append(calcula_perentiles(fecha_ultimo,index,70))
    lista_percentil80_60dias.append(calcula_perentiles(fecha_ultimo,index,80))
    lista_percentil90_60dias.append(calcula_perentiles(fecha_ultimo,index,90))

    lista_percentil10_30dias.append(calcula_perentiles(fecha_ultimo,index,10))
    lista_percentil20_30dias.append(calcula_perentiles(fecha_ultimo,index,20))
    lista_percentil30_30dias.append(calcula_perentiles(fecha_ultimo,index,30))
    lista_percentil40_30dias.append(calcula_perentiles(fecha_ultimo,index,40))
    lista_percentil50_30dias.append(calcula_perentiles(fecha_ultimo,index,50))
    lista_percentil60_30dias.append(calcula_perentiles(fecha_ultimo,index,60))
    lista_percentil70_30dias.append(calcula_perentiles(fecha_ultimo,index,70))
    lista_percentil80_30dias.append(calcula_perentiles(fecha_ultimo,index,80))
    lista_percentil90_30dias.append(calcula_perentiles(fecha_ultimo,index,90))
    
    lista_percentil10_20dias.append(calcula_perentiles(fecha_ultimo,index,10))
    lista_percentil20_20dias.append(calcula_perentiles(fecha_ultimo,index,20))
    lista_percentil30_20dias.append(calcula_perentiles(fecha_ultimo,index,30))
    lista_percentil40_20dias.append(calcula_perentiles(fecha_ultimo,index,40))
    lista_percentil50_20dias.append(calcula_perentiles(fecha_ultimo,index,50))
    lista_percentil60_20dias.append(calcula_perentiles(fecha_ultimo,index,60))
    lista_percentil70_20dias.append(calcula_perentiles(fecha_ultimo,index,70))
    lista_percentil80_20dias.append(calcula_perentiles(fecha_ultimo,index,80))
    lista_percentil90_20dias.append(calcula_perentiles(fecha_ultimo,index,90))    

    lista_percentil10_15dias.append(calcula_perentiles(fecha_ultimo,index,10))
    lista_percentil20_15dias.append(calcula_perentiles(fecha_ultimo,index,20))
    lista_percentil30_15dias.append(calcula_perentiles(fecha_ultimo,index,30))
    lista_percentil40_15dias.append(calcula_perentiles(fecha_ultimo,index,40))
    lista_percentil50_15dias.append(calcula_perentiles(fecha_ultimo,index,50))
    lista_percentil60_15dias.append(calcula_perentiles(fecha_ultimo,index,60))
    lista_percentil70_15dias.append(calcula_perentiles(fecha_ultimo,index,70))
    lista_percentil80_15dias.append(calcula_perentiles(fecha_ultimo,index,80))
    lista_percentil90_15dias.append(calcula_perentiles(fecha_ultimo,index,90))

    lista_percentil10_10dias.append(calcula_perentiles(fecha_ultimo,index,10))
    lista_percentil20_10dias.append(calcula_perentiles(fecha_ultimo,index,20))
    lista_percentil30_10dias.append(calcula_perentiles(fecha_ultimo,index,30))
    lista_percentil40_10dias.append(calcula_perentiles(fecha_ultimo,index,40))
    lista_percentil50_10dias.append(calcula_perentiles(fecha_ultimo,index,50))
    lista_percentil60_10dias.append(calcula_perentiles(fecha_ultimo,index,60))
    lista_percentil70_10dias.append(calcula_perentiles(fecha_ultimo,index,70))
    lista_percentil80_10dias.append(calcula_perentiles(fecha_ultimo,index,80))
    lista_percentil90_10dias.append(calcula_perentiles(fecha_ultimo,index,90))    
    
    lista_percentil10_05dias.append(calcula_perentiles(fecha_ultimo,index,10))
    lista_percentil20_05dias.append(calcula_perentiles(fecha_ultimo,index,20))
    lista_percentil30_05dias.append(calcula_perentiles(fecha_ultimo,index,30))
    lista_percentil40_05dias.append(calcula_perentiles(fecha_ultimo,index,40))
    lista_percentil50_05dias.append(calcula_perentiles(fecha_ultimo,index,50))
    lista_percentil60_05dias.append(calcula_perentiles(fecha_ultimo,index,60))
    lista_percentil70_05dias.append(calcula_perentiles(fecha_ultimo,index,70))
    lista_percentil80_05dias.append(calcula_perentiles(fecha_ultimo,index,80))
    lista_percentil90_05dias.append(calcula_perentiles(fecha_ultimo,index,90))    
    
    ##### minimos
    lista_minimos03dias.append(calcula_minimos(fecha_ultimo,index,3))
    lista_minimos05dias.append(calcula_minimos(fecha_ultimo,index,5))
    lista_minimos10dias.append(calcula_minimos(fecha_ultimo,index,10))
    lista_minimos15dias.append(calcula_minimos(fecha_ultimo,index,15))
    lista_minimos20dias.append(calcula_minimos(fecha_ultimo,index,20))
    lista_minimos25dias.append(calcula_minimos(fecha_ultimo,index,25))
    lista_minimos30dias.append(calcula_minimos(fecha_ultimo,index,30))
    lista_minimos60dias.append(calcula_minimos(fecha_ultimo,index,60))
    lista_minimos90dias.append(calcula_minimos(fecha_ultimo,index,90))  
    
    ##### maximos
    lista_maximos03dias.append(calcula_maximos(fecha_ultimo,index,3))
    lista_maximos05dias.append(calcula_maximos(fecha_ultimo,index,5))
    lista_maximos10dias.append(calcula_maximos(fecha_ultimo,index,10))
    lista_maximos15dias.append(calcula_maximos(fecha_ultimo,index,15))
    lista_maximos20dias.append(calcula_maximos(fecha_ultimo,index,20))
    lista_maximos25dias.append(calcula_maximos(fecha_ultimo,index,25))
    lista_maximos30dias.append(calcula_maximos(fecha_ultimo,index,30))
    lista_maximos60dias.append(calcula_maximos(fecha_ultimo,index,60))
    lista_maximos90dias.append(calcula_maximos(fecha_ultimo,index,90))    

    
#index=0
#fecha_ultimo[index-dias_atras-1:index]['ULTIMO']

fecha_ultimo['dia_siguiente1']=lista_siguiente1
fecha_ultimo['dia_siguiente2']=lista_siguiente2
fecha_ultimo['dia_siguiente3']=lista_siguiente3
fecha_ultimo['dia_siguiente4']=lista_siguiente4
fecha_ultimo['dia_siguiente5']=lista_siguiente5

fecha_ultimo['dia_anterior']=lista_anterior

fecha_ultimo['prom3dias']=lista_prom3dias
fecha_ultimo['prom5dias']=lista_prom5dias
fecha_ultimo['prom10dias']=lista_prom10dias
fecha_ultimo['prom15dias']=lista_prom15dias
fecha_ultimo['prom20dias']=lista_prom20dias
fecha_ultimo['prom25dias']=lista_prom25dias
fecha_ultimo['prom30dias']=lista_prom30dias
fecha_ultimo['prom60dias']=lista_prom60dias
fecha_ultimo['prom90dias']=lista_prom90dias

fecha_ultimo['percentil10_90dias']=lista_percentil10_90dias
fecha_ultimo['percentil20_90dias']=lista_percentil20_90dias
fecha_ultimo['percentil30_90dias']=lista_percentil30_90dias
fecha_ultimo['percentil40_90dias']=lista_percentil40_90dias
fecha_ultimo['percentil50_90dias']=lista_percentil50_90dias
fecha_ultimo['percentil60_90dias']=lista_percentil60_90dias
fecha_ultimo['percentil70_90dias']=lista_percentil70_90dias
fecha_ultimo['percentil80_90dias']=lista_percentil80_90dias
fecha_ultimo['percentil90_90dias']=lista_percentil90_90dias

fecha_ultimo['percentil10_60dias']=lista_percentil10_60dias
fecha_ultimo['percentil20_60dias']=lista_percentil20_60dias
fecha_ultimo['percentil30_60dias']=lista_percentil30_60dias
fecha_ultimo['percentil40_60dias']=lista_percentil40_60dias
fecha_ultimo['percentil50_60dias']=lista_percentil50_60dias
fecha_ultimo['percentil60_60dias']=lista_percentil60_60dias
fecha_ultimo['percentil70_60dias']=lista_percentil70_60dias
fecha_ultimo['percentil80_60dias']=lista_percentil80_60dias
fecha_ultimo['percentil90_60dias']=lista_percentil90_60dias

fecha_ultimo['percentil10_30dias']=lista_percentil10_30dias
fecha_ultimo['percentil20_30dias']=lista_percentil20_30dias
fecha_ultimo['percentil30_30dias']=lista_percentil30_30dias
fecha_ultimo['percentil40_30dias']=lista_percentil40_30dias
fecha_ultimo['percentil50_30dias']=lista_percentil50_30dias
fecha_ultimo['percentil60_30dias']=lista_percentil60_30dias
fecha_ultimo['percentil70_30dias']=lista_percentil70_30dias
fecha_ultimo['percentil80_30dias']=lista_percentil80_30dias
fecha_ultimo['percentil90_30dias']=lista_percentil90_30dias

fecha_ultimo['percentil10_20dias']=lista_percentil10_20dias
fecha_ultimo['percentil20_20dias']=lista_percentil20_20dias
fecha_ultimo['percentil30_20dias']=lista_percentil30_20dias
fecha_ultimo['percentil40_20dias']=lista_percentil40_20dias
fecha_ultimo['percentil50_20dias']=lista_percentil50_20dias
fecha_ultimo['percentil60_20dias']=lista_percentil60_20dias
fecha_ultimo['percentil70_20dias']=lista_percentil70_20dias
fecha_ultimo['percentil80_20dias']=lista_percentil80_20dias
fecha_ultimo['percentil90_20dias']=lista_percentil90_20dias

fecha_ultimo['percentil10_15dias']=lista_percentil10_15dias
fecha_ultimo['percentil20_15dias']=lista_percentil20_15dias
fecha_ultimo['percentil30_15dias']=lista_percentil30_15dias
fecha_ultimo['percentil40_15dias']=lista_percentil40_15dias
fecha_ultimo['percentil50_15dias']=lista_percentil50_15dias
fecha_ultimo['percentil60_15dias']=lista_percentil60_15dias
fecha_ultimo['percentil70_15dias']=lista_percentil70_15dias
fecha_ultimo['percentil80_15dias']=lista_percentil80_15dias
fecha_ultimo['percentil90_15dias']=lista_percentil90_15dias

fecha_ultimo['percentil10_10dias']=lista_percentil10_10dias
fecha_ultimo['percentil20_10dias']=lista_percentil20_10dias
fecha_ultimo['percentil30_10dias']=lista_percentil30_10dias
fecha_ultimo['percentil40_10dias']=lista_percentil40_10dias
fecha_ultimo['percentil50_10dias']=lista_percentil50_10dias
fecha_ultimo['percentil60_10dias']=lista_percentil60_10dias
fecha_ultimo['percentil70_10dias']=lista_percentil70_10dias
fecha_ultimo['percentil80_10dias']=lista_percentil80_10dias
fecha_ultimo['percentil90_10dias']=lista_percentil90_10dias

fecha_ultimo['percentil10_05dias']=lista_percentil10_05dias
fecha_ultimo['percentil20_05dias']=lista_percentil20_05dias
fecha_ultimo['percentil30_05dias']=lista_percentil30_05dias
fecha_ultimo['percentil40_05dias']=lista_percentil40_05dias
fecha_ultimo['percentil50_05dias']=lista_percentil50_05dias
fecha_ultimo['percentil60_05dias']=lista_percentil60_05dias
fecha_ultimo['percentil70_05dias']=lista_percentil70_05dias
fecha_ultimo['percentil80_05dias']=lista_percentil80_05dias
fecha_ultimo['percentil90_05dias']=lista_percentil90_05dias

fecha_ultimo['minimos_03dias']=lista_minimos03dias
fecha_ultimo['minimos_05dias']=lista_minimos05dias
fecha_ultimo['minimos_10dias']=lista_minimos10dias
fecha_ultimo['minimos_15dias']=lista_minimos15dias
fecha_ultimo['minimos_20dias']=lista_minimos20dias
fecha_ultimo['minimos_25dias']=lista_minimos25dias
fecha_ultimo['minimos_30dias']=lista_minimos30dias
fecha_ultimo['minimos_60dias']=lista_minimos60dias
fecha_ultimo['minimos_90dias']=lista_minimos90dias

fecha_ultimo['maximos_03dias']=lista_maximos03dias
fecha_ultimo['maximos_05dias']=lista_maximos05dias
fecha_ultimo['maximos_10dias']=lista_maximos10dias
fecha_ultimo['maximos_15dias']=lista_maximos15dias
fecha_ultimo['maximos_20dias']=lista_maximos20dias
fecha_ultimo['maximos_25dias']=lista_maximos25dias
fecha_ultimo['maximos_30dias']=lista_maximos30dias
fecha_ultimo['maximos_60dias']=lista_maximos60dias
fecha_ultimo['maximos_90dias']=lista_maximos90dias

#------------------------------------------------------------------------------------------------
##### FINALIZA 
################################################################################################


fecha_ultimo.to_csv('/Users/laiunce/Google Drive/scraping/4 - metricas/salida_metricas.csv')


mayor_menor = []
for index, row in fecha_ultimo.iterrows():
    
    try:
        if fecha_ultimo.loc[index]['ULTIMO']<fecha_ultimo.loc[index]['dia_siguiente1']:
            valor = 1
        else:
            valor = 0 
    except:
        valor=math.nan
    mayor_menor.append(valor)
fecha_ultimo['mayor_menor']=mayor_menor
    

mayor_menor_percentil50_20dias = []
for index, row in fecha_ultimo.iterrows():
    
    try:
        if fecha_ultimo.loc[index]['ULTIMO']<fecha_ultimo.loc[index]['percentil50_20dias']:
            valor = 1
        else:
            valor = 0 
    except:
        valor=math.nan
    mayor_menor_percentil50_20dias.append(valor)    
    
fecha_ultimo['mayor_menor_percentil50_20dias']=mayor_menor_percentil50_20dias

