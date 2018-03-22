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
directorio = '/Users/laiunce/Google Drive/scraping/8- robot baja series historicas/acciones_arg/'



indices_recorrer = ['ypf-sociedad','gp-fin-galicia','macro','b-santander-ri','mirgor','frances','pampa-energia','siderar','telecom','central-puerto','loma-negra-ba?cid=1055994','loma-negra-ba','petrobras-arg','bco-patagonia','aluar','ferrum','grupo-supervielle-sa','juan-minetti','tran-gas-del-s','alto-palermo','irsa','camuzzi','edenor','consultatio-s.','bolsas-y-mercados-argentinos-sa','cresud','capex','metrogas','central-costan','i-y-e-de-la-pa','transener','comer-del-plat','molinos','gas-natural-sdg?cid=13343','bco-hipotecari','molinos-agro','boldt','grupo-financiero-valores','indupa','ledesma','con-del-oeste','inversora-juramento','bodegas-esmeralda-sa','san-miguel','ecogas','grupo-clarin','rigolleau','autopistas-sol','caputo','quickfood','grimoldi','nortel-inversora-sa','agrometal','celulosa','tglt-sa','dycasa','empresa-distribuidora-electrica','carlos-casado','compania-introductora-buenos-aires','longvie','insumos-agroquimicos-sa','moli-juan-semi','garovaglio','carboclor','fiplasto','pet.del-conosu','inst-rosembusc','morixe','domec-compania-de-artefactos-domest','colorin','polledo','caterpillar-inc-ar','microsoft-corp-ar','alcoa-inc.','walt-disney-company','cisco-systems','kimberly-clark-corp.','royal-dutch-shell-a-ar','koninklijke-philips-electronics','novartis-drc','total-cedear','banco-bilbao-vizcaya-argentaria','nokia','sap-ag-ads-exch?cid=30096','apple-inc.','rio-tinto-plc-exch?cid=30170','national-grid-ar','unilever-cert?cid=30183','pfizer-inc.-ar','bristol-myers-squibb-co.','yamana-gold-drc','hewlett-packard','china-mobile-ar','gazprom?cid=30359','barrick-gold','repsol-ypf?cid=13360','andes-energia-plc?cid=992998','petrobras-pn?cid=962554','american-express-co-ba','banco-santander-brasil-sa-ba','lockheed-martin-corp','mercadolibre-inc','banco-santander-rio-sa','ternium-s.a.?cid=962568','american-international-group-inc','alphabet-inc','honda?cid=962560','coca-cola-co-ba','petrolera-pampa-sa','tenaris?cid=13302','petrobras-on?cid=13303','banco-santander?cid=13369','telefonica?cid=13370','tran-gas-norte','chevron-corp-ar','citigroup-incorporated','bank-of-america-corp','at-t-inc.','intel-ar','jpmorgan-chase---co.','mcdonald-corp','merck---co-inc.','3m-co-drc','siemens-a.g.','bhp-ltd','colgate-palmolive-company','du-pont-de-nemours---company','wal-mart-stores-inc','home-depot-inc.','international-business-machines','sony?cid=30229','verizon-communications-inc.','newmont-mining-drc','johnson---johnson-co','general-electric-co.','toyota?cid=30284','pepsico-inc','petrochina-co','nike-inc','procter---gamble','vale-s.a.--americ?cid=30353','banco-bradesco-adr?cid=30418','goldcorp','ovoprot-international-sa','havanna-sa','meranol-saci','cablevision','laboratorios-richmond']

indices_recorrer = ['unilever-cert?cid=30183','pfizer-inc.-ar','bristol-myers-squibb-co.','yamana-gold-drc','hewlett-packard','china-mobile-ar','gazprom?cid=30359','barrick-gold','repsol-ypf?cid=13360','andes-energia-plc?cid=992998','petrobras-pn?cid=962554','american-express-co-ba','banco-santander-brasil-sa-ba','lockheed-martin-corp','mercadolibre-inc','banco-santander-rio-sa','ternium-s.a.?cid=962568','american-international-group-inc','alphabet-inc','honda?cid=962560','coca-cola-co-ba','petrolera-pampa-sa','tenaris?cid=13302','petrobras-on?cid=13303','banco-santander?cid=13369','telefonica?cid=13370','tran-gas-norte','chevron-corp-ar','citigroup-incorporated','bank-of-america-corp','at-t-inc.','intel-ar','jpmorgan-chase---co.','mcdonald-corp','merck---co-inc.','3m-co-drc','siemens-a.g.','bhp-ltd','colgate-palmolive-company','du-pont-de-nemours---company','wal-mart-stores-inc','home-depot-inc.','international-business-machines','sony?cid=30229','verizon-communications-inc.','newmont-mining-drc','johnson---johnson-co','general-electric-co.','toyota?cid=30284','pepsico-inc','petrochina-co','nike-inc','procter---gamble','vale-s.a.--americ?cid=30353','banco-bradesco-adr?cid=30418','goldcorp','ovoprot-international-sa','havanna-sa','meranol-saci','cablevision','laboratorios-richmond']
for pag_actual in indices_recorrer:
    try:
      
        pagina = 'https://es.investing.com/equities/'+pag_actual+'-historical-data'
        
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
    except:
        pass     
