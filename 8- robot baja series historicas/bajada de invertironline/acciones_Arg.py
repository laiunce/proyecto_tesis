#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:43:42 2018

@author: laiunce
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 20:46:55 2017

@author: laiunce
"""
from selenium.webdriver.support.ui import Select
import bs4
import requests
import re
import csv
import pandas as pd
import numpy as np
import time
import urllib.request 
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import pyautogui
from datetime import datetime
from time import sleep

#lista_acc = ['PAMP','AGRO','ALUA','APBR','AUSO','BHIP','BMA','BOLT','BPAT','BRIO','BYMA','CADO','CAPU','CAPX','CECO2','CELU','CEPU','CGPA2','COME','CRES','CTIO','CVH','DGCU2','DYCA','EDN','ERAR','FERR','FIPL','FRAN','GARO','GBAN','GCLA','GGAL','GRIM','INDU','INVJ','IRCP','IRSA','JMIN','LEDE','LOMA','LONG','MERA','METR','MIRG','MOLA','MOLI','MORI','OEST','PATA','PATY','PESA','PETR','PGR','REP','RICH','ROSE','SAMI','SEMI','STD','SUPV','TECO2','TEF','TGLT','TGNO4','TGSU2','TRAN','TS','VALO','YPFD']
lista_acc = ['PAMP']

driver = webdriver.Chrome('/Users/laiunce/anaconda/selenium/webdriver/chromedriver')

directorio = '/Users/laiunce/Google Drive/scraping/8- robot baja series historicas/bajada de invertironline/'



valor_registros=200

for pag_act in lista_acc:
    
    try:
    
        #obtiene pagina
        pagina = 'https://www.invertironline.com/Titulo/DatosHistoricos?simbolo='+pag_act+'&mercado=BCBA'
        driver.get(pagina)
        
        
        #define rango de inicio y fin de busqueda, el inicial se lo deja fijo 2001 y el hasta se calcula con la fecha de hoy
        rango = '01-01-2001 - '+str(datetime.today().strftime('%d/%m/%Y'))
        
        #se llena campo de filtro fecha
        element = driver.find_element_by_id("DesdeHasta")
        element.clear()
        element.send_keys(rango)
        
        sleep(1)
        
        element = driver.find_element_by_id("aplicarbusqueda")
        element.click()
         
        sleep(2)
        #copia todo lo de la pagina para buscar la canidad de paginas a recorrer y de la pagina inicial ya copia los datos
        #el tema es q esta pagina deja cacheado los valores pero hay que clickear el boton de siguiente para que vaya mostrando los datos de a 20
        
        select = Select(driver.find_element_by_name('tbcotizaciones_length'))
        select.select_by_visible_text(str(valor_registros))
        
        pyautogui.keyDown("command")
        pyautogui.keyDown('a')
        
        sleep(1)
        
        text = driver.execute_script('return window.getSelection().toString()')
        

        
        #obtiene cantidad de click a pagina siguientes hay que hacer para recobrar todos los datos
        cant =str(re.findall('1 - 200 de .*Anterior', text)[0]).replace('1 - 200 de ','').replace('Anterior','').replace(',','')
        paginas = int(int(cant)/valor_registros)+1
        
        #obten y guarda datos
        contexto = re.findall('\d\d/\d\d/\d\d\d\d\s\d*\.\d*\s\d*\.\d*\s\d*\.\d*\s\d*\.\d*', text)
        data= []
        for i in contexto:
            data.append(i.split('\t'))
        
        
        #aca recorre todos los datos, pagina por pagina hace lo mismo, hace click en la siguiente pagina copia los valores y parsea la ingo
        for i in range(1,paginas):    
        
            #pagina siguiente
            element = driver.find_element_by_id("tbcotizaciones_next")
            element.click()    
            
            sleep(1)
            
            pyautogui.keyDown("command")
            pyautogui.keyDown('a')   
            
            text = driver.execute_script('return window.getSelection().toString()')
            
        
            contexto = re.findall('\d\d/\d\d/\d\d\d\d\s\d*\.\d*\s\d*\.\d*\s\d*\.\d*\s\d*\.\d*', text)
            
            
            for i in contexto:
                data.append(i.split('\t'))    
            
        
            
        df = pd.DataFrame(data)
        
        
        #transforma fecha
        df[0]= df.apply(lambda x: x[0][6:10]+x[0][0:2]+x[0][3:5], axis=1)
        
        #df.columns = ['fecha','ultima','apertura','maximo','minimo','vol','varianza']
        
        df.columns = ['fecha','apertura','maximo','minimo','ultima']
        
        
        df.to_csv(directorio+'/bajada/'+pag_act+'.csv', index=False)
    except:
        pass    
