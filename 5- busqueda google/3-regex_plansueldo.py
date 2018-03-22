  

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
from unidecode import unidecode

#en convenios se lee tambien el regex, para dar luz verde si en el cuerpo de la pagina se encuentra el nombre de la empresa 

#########################################################################################################
# BLOQUE 1
####### Comieza Lee convenios, empresas, o nombres

directorio = 'C:\\Users\\LAC40641\\Desktop\\plan_sueldo\\kiperszmid\\'

convenios_lista= []
convenios = open(directorio+'2-convenios.csv', 'r')
reader = csv.reader(convenios, delimiter='~')
for i in reader:
    dup=[]
    dup.append(i[0])
    dup.append(i[1])
    convenios_lista.append(dup)

for empresa in convenios_lista:
    print(empresa[1])

####### Termina Lee convenios, empresas, o nombres
#########################################################################################################


#########################################################################################################
# BLOQUE 2
####### Comieza Lee palabras de alerta
coincidir=[]
my_file = open(directorio+'1-palabras_alertas.csv', 'r')
reader = csv.reader(my_file, delimiter=',')
for i in reader:
    du=[]
    du.append(i[0])
    du.append(i[1])
    coincidir.append(du)

####### Termina Lee palabras de alerta
#########################################################################################################


  

# estas son variables para la busquda, agregarlas dependiendo si se tiene en cuenta el tiempo, en este caso
# estamos buscando la totalidad, no en un periodo por eso no nos sirve
#la variable pais indica el pais de origen de la pagina
ultsemana = '&tbs=qdr:m'
pais = '&cr=countryAR'     

###########################################################################################
#comienza busqueda por rango de dia mes anio
dia_min,mes_min,anio_min = 1,1,2012
dia_max,mes_max,anio_max = 27,10,2017


pagina = 'issel+Kiperszmid+argentina'

busqueda_dia_mes_anio = 'tbs=cdr:1,cd_min:'+str(mes_min)+'/'+str(dia_min)+'/'+str(anio_min)+',cd_max:'+str(mes_max)+'/'+str(dia_max)+'/'+str(anio_max)

    
#termina busqueda por rango de dia mes anio
###########################################################################################
        
#el archivo es un csv separado por el firulete, el primer elemento es el nombre de la empresa buscada y el segundo elemeneto el regex        
for empresa_regex in convenios_lista:
    try:
        empresa=empresa_regex[0]
        emp_regex=empresa_regex[1]
        print('--------------------------------------------------------------------')
        print(empresa)
        busqueda=empresa+' argentina'
        pagina = busqueda.replace(" ", "+")

        #hacer iterador por combinacion de lugares y sumando sector economico
        #donde encuentre palabra clave por regex traerse solo el texto que rodea
        #jugar con busquedas delcontexto por ejemnplo buscando las tres palabras que aparecen con mas frecuencia
        
        #en itera esta las paginas devueltas por la busqueda de google, 0 es al primer pagina, 10 la seguna y asi
        #itera=["0"]

        #########################################################################################################
        # BLOQUE 3
        ####### Comieza obtiene paginas de google

        #itera=["0","10","20","30","40","50","60"]
          
        headers = {
                "User-Agent":
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
                }
        palabras=[]
        
        itera=["0","10","20","30","40","50","60"]
        urls=[]
        
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
        
        ####### Termina obtiene paginas de google
        #########################################################################################################


        #urls=[]
        #urls.append('http://www.enredando.org.ar/2017/02/10/la-destruccion-del-trabajo-en-tiempos-de-macri/')
        print(urls)

        #########################################################################################################
        # BLOQUE 4
        ####### Comieza reocrre paginas y obtiene palabras minimizando basura por expresion regular
        
        #urls = ['https://www.defrentealcampo.com.ar/2017/08/24/suspension-de-tres-establecimientos-frigorificos-en-rio-negro-y-neuquen/']
        #urls = ['http://200monos.blogspot.com.ar/2013/09/cristina-inauguro-en-2009-un.html']
        driver = webdriver.Chrome('C:\\Users\\LAC40641\\Desktop\\plan_sueldo\kiperszmid\\chromedriver.exe')
        for url in urls:
            print(url)
            try:
                
                driver.get(url)
                #le da 5 segundos a la pagina para que la pagina se acomode por completo
                time.sleep(5)

                text = driver.execute_script('return document.documentElement.innerHTML;')
               
              
                #siguientes lineas forma antigua que devuelte la estructura no el html, esto puede perder informacion por ejemplo en
                #la pagina http://200monos.blogspot.com.ar/2013/09/cristina-inauguro-en-2009-un.html
                
                #page_ext = requests.get(url)
                #soup_ext = BeautifulSoup(page_ext.content)
                #text=soup_ext.get_text()
                
                text=text.lower()
                
                text = text.replace("ñ", "n")
                text = text.replace("á", "a")
                text = text.replace("é", "e")
                text = text.replace("í", "i")
                text = text.replace("ó", "o")
                text = text.replace("ú", "u")
                text = text.replace("Á", "A")
                text = text.replace("É", "E")
                text = text.replace("Í", "I")
                text = text.replace("Ó", "O")
                text = text.replace("Ú", "U")
                text = text.replace('"', " ")
                text = text.replace(',', " ")
                text = text.replace(';', " ")                
                text = text.replace("[", " ")
                text = text.replace("]", " ")
                text = text.replace("´", " ")
                text = text.replace(".", " ")
                text = text.replace("'", " ")
                text = text.replace("^", " ")

                #with open('C:\\Users\\LAC40641\\Desktop\\plan_sueldo\kiperszmid\\pagina.html', "a") as myfile:
                #    myfile.write(text)
                
                try:
                    palabra_buscada=[]
                    #aca se fija si esta el regex en esta pagina
                    palabra_buscada =re.findall('%s' %emp_regex.lower(), text)
                    #aca se queda con el contexto del regex
                    texo_300_caracteres = re.findall('(?s).{0,800}%s.{0,800}' %emp_regex.lower(), text)
                    
                    texto_unido = ''
                    for i in texo_300_caracteres:
                        texto_unido= texto_unido+' '+i
                        
                    #para hacer coincidr con frases en lugar de separar todas las palabras y comparar 1 a 1,
                    #hacer un regex con la frase buscada y buscar en el texto_300_caracteres si coincide
                    
                    if len(palabra_buscada) > 0:
                        tmp = re.findall(r"[a-zA-ZáéíóúÁÉÍÓÚ]{4,}", texto_unido)
                        for a in tmp:
                            tupla=[]
                            if len(a)>3:
                                tupla.append(a)
                                tupla.append(url)
                                palabras.append(tupla)
                except:
                    print('error regex que lee'+ url)      
            except:
                print('error en parseo de pagina'+ url)
            
        driver.close()
        driver.quit()
                
        ####### Termina reocrre paginas y obtiene palabras minimizando basura por expresion regularar
        #########################################################################################################

      
        #########################################################################################################
        # BLOQUE 5
        ####### Comieza obtiene coincidencias compararon con palabras de alerta
        
                            
        if len(palabras) > 0:
            coincidencias = []
            for c in coincidir:
                agrega=0
                contador = 0
                for p in palabras:
                        
                    if c[1] == p[0]:
                        print(c[1])
                        agrega=1
                        contador += 1
                if agrega ==1:
                    coincidencias.append(c[1])
                #if contador > 0:
                    #print(c[1]+' '+str(contador))
                    
        ####### Termina Comieza obtiene coincidencias compararon con palabras de alerta
        #########################################################################################################
                 
     
      
        #########################################################################################################
        # BLOQUE 6
        ####### Comieza crea dupla de palabra de alerta y pagina web

            dupla_coincidencia = []
            for pal in palabras:
                if pal[0] in coincidencias:
                    agg = []
                    agg.append(pal[0])
                    agg.append(pal[1])
                    dupla_coincidencia.append(agg)
      


            salida=pd.DataFrame(dupla_coincidencia)
            salida.columns= ['palabra','url']
            p=salida.drop_duplicates()
            group=p.groupby('palabra').agg({'url': np.size})


            print('-----')
            print(group)

        ####### Termina crea dupla de palabra de alerta y pagina web
        #########################################################################################################            
            
        #########################################################################################################
        # BLOQUE 7
        ####### Comieza crea flag por pesos 
                
            valores= [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0]]
            flag_imprime = 0
            for row in group.iterrows():
                valor=0
                for i in coincidir:
                    if i[1] == row[0]:
                        valor=int(i[0])
                for v in valores:
                    if v[0] == valor:
                        v[1]=v[1]+row[1][0]
                        
        ####### Termina crea flag por pesos 
        #########################################################################################################      
            
            print('valores: ')
            print(valores)
                    
        #########################################################################################################
        # BLOQUE 8
        ####### Comienza Imprime resultados en csv

                #por un lado salida sin reptir
            directorio = 'C:\\Users\\LAC40641\\Desktop\\plan_sueldo\\kiperszmid\\'
            salida_sinduplicados = salida.drop_duplicates()
            salida_sinduplicados.to_csv(directorio+'salidas\\'+empresa+'_salida.csv',index=False)
            salida.to_csv(directorio+'salidas\\'+empresa+'_salida_dinamica.csv',index=False)
                #por otro lado salida para hacer dinamica con colores
        
        ####### Termina Imprime resultados en csv 
        #########################################################################################################      

    except:
        print('error')
    

#en salida estan las coincidencias con la url



