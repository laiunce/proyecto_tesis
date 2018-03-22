#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 01:00:34 2018

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
from time import sleep
import glob

driver = webdriver.Chrome('/Users/laiunce/anaconda/selenium/webdriver/chromedriver')
directorio = '/Users/laiunce/Google Drive/scraping/8- robot baja series historicas/bajada ravaonline/bajada/'


lista_emp = ['BPAT','BRIO','CADO','CAPU','CAPX','CARC','CELU','CGPA2','COLO','CVH','DYCA','EDLH','FERR','FIPL','GARO','GBAN','GCLA','GRIM','HAVA','INDU','INVJ','IRSA','LEDE','LOMA','LONG','METR','MOLA','MOLI','MORI','PATA','PATY','PESA','PETR','PSUR','REP','RICH','SEMI','STD','TEF','TGLT','VALO']

pag_actual='BPAT'

for pag_actual in lista_emp:
    #obtiene pagina
    try:

        pagina = 'http://www.ravaonline.com/v2/empresas/precioshistoricos.php?e='+pag_actual+'&csv=1'
        driver.get(pagina)
        sleep(2)
        
        #leer csv y cambiar formato fecha a aaaammdd
        
        
    
        
        path = '/Users/laiunce/Downloads/'
        extension = 'csv'
        os.chdir(path)
        result = [i for i in glob.glob('*.{}'.format(extension))]
        
        
        archivo=''
        for i in result:
            if pag_actual in i:
                archivo = i
            
        df = pd.read_csv(path+archivo)
        
        df['fecha']= df.apply(lambda x: x[0][0:4]+x[0][5:7]+x[0][8:10], axis=1)
        
        df2 = df[['fecha', 'cierre','apertura','maximo','minimo']].copy()
        df2.columns = ['fecha','ultima','apertura','maximo','minimo']
        
        df2.to_csv(directorio+pag_actual+'.csv', index=False)

    except:
        pass

