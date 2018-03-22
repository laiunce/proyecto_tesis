#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 23:54:39 2017

@author: laiunce
"""

#http://www.ambito.com/economia/mercados/indices/merval/

from bs4 import BeautifulSoup
import requests
import bs4
import re
import pandas as pd
import numpy as np

directorio = '/Users/laiunce/Desktop/scraping/'

#Aca lee todos los nombres delas acciones
df = pd.read_csv(directorio+'1 - Nombres de empresas/nombre_empresas.csv', )
for i in df.iterrows():
    print(i[1][0])


desde = '01/01/2009'
hasta = '14/09/2018'
accion ='PAM.N'



page = requests.get('http://www.ambito.com/economia/mercados/acciones/?ric='+accion+'&desde='+desde+'&hasta='+hasta+'&pag=999')
soup = bs4.BeautifulSoup(page.text)

#obtiene el nro de pagina maximo para iterar de 1 hasta el nro maximo de paginas y asi traer toda la info
paginas=[]
paginas_iterador= re.findall(r'pag=\d*',str(soup))
for i in paginas_iterador:
    paginas.append(int(i.replace('pag=','')))
    

final=[] 
for n in range(1,max(paginas)+1):
    page = requests.get('http://www.ambito.com/economia/mercados/acciones/?ric='+accion+'&desde='+desde+'&hasta='+hasta+'&pag='+str(n))
    response = page

    soup = bs4.BeautifulSoup(response.text)
    links = soup.find_all('tr')
    
    lista=[]
    
    for i in links:
        td=(i.find_all('td'))
        for t in td:
            agg= (t.find_all('div'))
            lista.append(agg)
            

    for i in lista:
        try:
            final.append(re.search('(\d*,\d*|\d\d\s[A-Z]{3,}\s\d\d\d\d)', str(i)).group())
                
        except:
            print('error')
        
        
        
final2=[]        
lista2 = []
contador = 0
for i in final:
    contador +=1
    string = re.search('(\d*,\d*|\d\d\s[A-Z]{3,}\s\d\d\d\d)', str(i)).group()
    if contador == 6:
        contador= 0
        lista2.append(float(string.replace(',','.')))
        final2.append(lista2)
        lista2 = []
    else:
        if contador == 1:   
            tmp=string
            tmp = str(tmp).replace('ENE','01')
            tmp = str(tmp).replace('FEB','02')
            tmp = str(tmp).replace('MAR','03')
            tmp = str(tmp).replace('ABR','04')
            tmp = str(tmp).replace('MAY','05')
            tmp = str(tmp).replace('JUN','06')
            tmp = str(tmp).replace('JUL','07')
            tmp = str(tmp).replace('AGO','08')
            tmp = str(tmp).replace('SEP','09')
            tmp = str(tmp).replace('OCT','10')
            tmp = str(tmp).replace('NOV','11')
            tmp = str(tmp).replace('DIC','12')
            lista2.append(tmp[6:10]+tmp[3:5]+tmp[0:2])
        else:
            lista2.append(float(string.replace(',','.')))
        

#convierte a dataframe

labels = ['FECHA','APERTURA','ULTIMO','VAR%','MAX.','MIN.']
df_evolucion = pd.DataFrame.from_records(final2, columns=labels)


df_evolucion.to_csv(directorio+'2 - lee datos empresas/datasets/'+accion+'.csv',index = False)



