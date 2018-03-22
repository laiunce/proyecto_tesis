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
from time import sleep

driver = webdriver.Chrome('/Users/laiunce/anaconda/selenium/webdriver/chromedriver')
directorio = '/Users/laiunce/Google Drive/scraping/8- robot baja series historicas/series/'



indices_recorrer = ['germany-30','tasi','merv','aus-200','atx','bax','dhaka-stock-exchange-30','bel-20','birs','bse-domestic-company','bovespa','bse-sofia','s-p-tsx-composite','ipsa','shanghai-composite','cyprus-main-market','colcap','kospi','brvm-10','costa-rica-indice-accionario','crobex','omx-copenhagen-20','guayaquil-select','egx30','adx-general','sax','blue-chip-sbitop','spain-35','us-30','tallinn-se-general','psei-composite','omx-helsinki-25','france-40','athens-general-composite','netherlands-25','hang-sen-40','hungary-stock-market','sensex','idx-composite','isx-main-60','iseq-overall','omx-iceland-all-share','ta25','it-mib-40','jse-market','japan-ni225','amgnrlx','kase','kenya-nse-20','kwse','riga-general','blom-stk-idx','vilnius-se-general','ftse-malaysia-klci','domestic-share','mse','masi','semdex','ipc','mne-top-20','mnse-10','ftse-namibian-overall','nse-30','ose-benchamrk','dow-jones-new-zealand','msi','karachi-100','ple','lima-stock-exchange-general','wig-20','psi-20','qsi','uk-100','px','rwanda-all-share','bet','mcx','belex-15','singapore-straits-time','cse-all-share','ftse-jse-top-40','omx-stockholm-30','switzerland-20','thailand-set','taiwan-weighted','tanzania-all-share','tunindex','ise-100','pfts','uganda-all-share','bursatil','hnx-30','lse-all-share','zimbabwe-industrial','spain-35-chart','dax-software-price']


for pag_actual in indices_recorrer:
    
    pagina = 'https://es.investing.com/indices/'+pag_actual+'-historical-data'
    
    driver.get(pagina)
    
    sleep(1)
    
    #pyautogui.click(x=411, y=487, clicks=1, interval=0.5, button='left')
    
    #pyautogui.click(x=872, y=829, clicks=1, interval=0.5, button='left')
    
    #pyautogui.click(x=479, y=757, clicks=1, interval=0.5, button='left')
    
    element = driver.find_element_by_id("widgetFieldDateRange")
    element.click()
    
    
    pyautogui.typewrite(['backspace','backspace', '0', '1','enter'], interval=1)
    
    sleep(5)
    
    pyautogui.keyDown("command")
    pyautogui.keyDown('a')
    pyautogui.keyUp("command")
    pyautogui.keyUp("a")
    
    text = driver.execute_script('return window.getSelection().toString()')
                
    text=text.lower()
    
    
    contexto = re.findall('\d\d\.\d\d\.\d\d\d\d.*', text)
    
    #reemplaza %, y puntos por nada y comas por puntos
    
    data= []
    for i in contexto:
        limpio = i.replace('%','').replace('.','').replace(',','.').replace('m','').replace('k','')
        data.append(limpio.split('\t'))
    
    
    
    df = pd.DataFrame(data)
    
    #transforma fecha
    df[0]= df.apply(lambda x: x[0][4:10]+x[0][2:4]+x[0][0:2], axis=1)
    
    df.columns = ['fecha','ultima','apertura','maximo','minimo','vol','varianza']
    
    df.to_csv(directorio+pag_actual+'.csv', index=False)
    
    
