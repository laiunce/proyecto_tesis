#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 20:46:55 2017

@author: laiunce
"""
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

 
pagina = 'pampa+energia'
regex= '(pampa energia|energia pampa|petrolera pampa)'
    
def convierte_numero_texto(numero):
    if numero < 10:
        return '0'+str(numero)
    else:
        return str(numero)
    

###########################################################################################
#comienza busqueda por rango de dia mes anio

for d in range(1,2):
                        
    dia_min,mes_min,anio_min = 2,4,2017
    dia_max,mes_max,anio_max = 2,4,2017
    
    dia_min=d
    dia_max=d
    
    nom_directorio_fecha =convierte_numero_texto(anio_min)+convierte_numero_texto(mes_min)+convierte_numero_texto(dia_min)  
    print(nom_directorio_fecha)
    
    busqueda_dia_mes_anio = 'tbs=cdr:1,cd_min:'+str(mes_min)+'/'+str(dia_min)+'/'+str(anio_min)+',cd_max:'+str(mes_max)+'/'+str(dia_max)+'/'+str(anio_max)
    
    palabras=[]
#    itera=["0","10","20","30","40"]
    itera=["0"]
    urls=[]
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }
        
        
    
    
    try:
        for cant_pag in itera:
            try:
                time.sleep(5)
                r = requests.get('https://www.google.com.ar/search?q='+pagina+'&'+busqueda_dia_mes_anio+'&start='+cant_pag, headers=headers)
                soup = bs4.BeautifulSoup(r.content, 'html5lib')
                links = soup.find_all('a', href=True)
                count=0
                for i in links:
                    try:
                        if str(i)[0:13] == '<a href="http' and str(i)[17:35] != 'support.google.com':
                            urls.append(i.get('href'))
                    except:
                        print('error en devolver links')
            except:
                print('error '+str(cant_pag))
    except:
        print('error cantidad de paginas en itera')   
        
        
    
    
    
    salidas_dir = '/Users/laiunce/Desktop/scraping/5- busqueda google/salidas/'
    
    #crea directiorio nombre
    


    
    #crea directorio por fecha de busquedas
    if not os.path.exists(salidas_dir+nom_directorio_fecha):
        os.makedirs(salidas_dir+nom_directorio_fecha)
    
    
    #bajarse el chromedriver.exe y pegarlo en el directorio correspondiente
    
    
    
    
    driver = webdriver.Chrome('/Users/laiunce/anaconda/selenium/webdriver/chromedriver')
    contador = 0
    for url in urls:
        try:
            contador +=1
            driver.get(url)
            time.sleep(5)
            
            file = salidas_dir+nom_directorio_fecha+'/'+str(contador)+'.html'
            
            with open(file+'.html', "a", encoding='utf-8') as myfile:
                text = driver.execute_script('return document.documentElement.innerHTML;')
                myfile.write(text)

            #HtmlFile = open(file+'.html', 'r', encoding='utf-8')
            #text = HtmlFile.read()

            pyautogui.keyDown("command")
            pyautogui.keyDown('a')
            pyautogui.keyUp("command")
            pyautogui.keyUp("a")
            
            text = driver.execute_script('return window.getSelection().toString()')
            
            text=text.lower()
            text = text.replace("ñ", "n")
            text = text.replace("á", "a")
            text = text.replace("é", "e")
            text = text.replace("í", "i")
            text = text.replace("ó", "o")
            text = text.replace("ú", "u")
            
            
            contexto = re.findall('(?s).{0,500}%s.{0,500}' %regex.lower(), text)
            if len(contexto) > 0:
                            
                palabras_pagina = re.findall(r"[a-zA-ZáéíóúÁÉÍÓÚ]{4,15}", contexto)
            
                with open(file+'.txt', "a", encoding='utf-8') as myfile:
                    for p in palabras_pagina:
                        myfile.write(p+'\n')
        except:
            print('error en guardado de html')
            
    driver.close()
    driver.quit()
    
    
    
    

            
            #espera 5 segundos para que la pagina se cargue por completo
            







