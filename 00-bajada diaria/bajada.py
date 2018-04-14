#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 12:32:49 2018

@author: laiunce
"""


import requests
import re
import pandas as pd

server_dir = '0.0.0.0'
server_dir = '52.14.67.113'

def limpia_texto(text):
    text=text.lower()
    text = text.replace("ñ", "n")
    text = text.replace("á", "a")
    text = text.replace("é", "e")
    text = text.replace("í", "i")
    text = text.replace("ó", "o")
    text = text.replace("ú", "u") 
    text = text.replace(".", " ")
    text = text.replace(",", " ")
    text = text.replace(";", " ")        
    text = text.replace("[", " ")
    text = text.replace("]", " ")
    text = text.replace("(", " ")
    text = text.replace(")", " ")        
    text = text.replace("{", " ")
    text = text.replace("}", " ")
    text = text.replace("?", " ")        
    text = text.replace("¿", " ")        
    text = text.replace("!", " ")        
    text = text.replace("¡", " ")    
    text = text.replace(":", " ")  
    return(re.sub('[^a-zA-Z\s]', '', text))


#pagina='https://www.revistavirtualpro.com/noticias/energia'    

def obtiene_texto_palabras_metricas(pagina,fechaini,fechafin):

    path = "http://"+server_dir+":5000/api/v1/resources/get?webpage={}".format(pagina)
    r = requests.get(path) 
    te = (r.json().replace('\n',' '))      
    limp = limpia_texto(te)
    merge=''
    for rx in regex.split('|'):
        contexto = re.findall(r"(?s).{0,500}%s.{0,500}"%rx, limp)
        for t in contexto:
            merge=merge + ' '+t
            
    palabras_pagina = re.findall(r"[a-zA-Z]{4,20}", merge)
    
    df=pd.DataFrame(palabras_pagina)
    df.columns = ['palabra']
    df['pagina'] =pagina
    df['cantidad'] = 1
    df['fechaini'] = fechaini
    df['fechafin'] = fechafin 
    
    return df


def crea_metricas_palabras(df1):
    #cantidad de veces aparecida
    palabras_count = pd.DataFrame(df1.groupby(['palabra'])['cantidad'].agg('sum'))
    #cantidad de veces aparecida en paginas distintas
    palabras_paginas_dif = pd.DataFrame(df1.groupby('palabra').pagina.nunique())
    #Se conviernte dataframe a json
    
    union = pd.merge(palabras_count, palabras_paginas_dif, left_index=True, right_index=True)
    union.columns = ['aparece_qty','paginas_diferentes_qty']
    union['fechaini'] = fechaini
    union['fechafin'] = fechafin
    union['palabra'] = union.index
    data_out.index
    
    return union



def devuelve_palabras_cantidades(busqueda,fechaini,fechafin,regex):
    print('obtiene paginas')
    #obtiene busquedas
    path = "http://"+server_dir+":5000/api/v1/resources/get_google?busqueda={}&fechaini={}&fechafin={}".format(busqueda,fechaini,fechafin)
    r = requests.get(path) 
    json = r.json()
    
    #por cada pagina obiene el texto
    
    print('cantidad de paginas: '+str(len(json)))
    
    df1 = pd.DataFrame()

    
    contador = 0
    for pagina in json:
        contador +=1
        print('va por pagina: '+str(contador))
        try:
            df = obtiene_texto_palabras_metricas(pagina,fechaini,fechafin)
            df1= pd.concat([df1, df], ignore_index=True) 
        except:
            pass
    
    
    #crea dataframe con
    #palabra, cantidad de paginas, cantidad palabras
    
    #transformar a json
    #out = union.to_json(orient='records')[1:-1].replace('},{', '} {')
    
    return df1



#busqueda = 'pampa+energia+argentina'
#fechaini = '20170401'
#fechafin = '20170401'
#regex= 'energia pampa|petrolera pampa|pampa energia'

#directorio_salida='/Users/laiunce/Desktop/bajada_paginas/'

directorio_salida=''

#data_out = devuelve_palabras_cantidades(busqueda,fechaini,fechafin,regex)   

data_out_merged = pd.DataFrame()
#fechas = ['20180320','20180321','20180322','20180323','20180324','20180325','20180326','20180327','20180328','20180329','20180330','20180331','20180401','20180402','20180403','20180404','20180405','20180406','20180408']
fechas = ['20180301','20180302','20180303','20180304','20180305','20180306','20180307','20180308','20180309','20180310','20180311','20180312','20180313','20180314','20180315','20180316','20180317','20180318','20180319','20180320','20180321','20180322','20180323','20180324','20180325','20180326','20180327','20180328','20180329','20180330','20180331','20180201','20180202','20180203','20180204','20180205','20180206','20180207','20180208','20180209','20180210','20180211','20180212','20180213','20180214','20180215','20180216','20180217','20180218','20180219','20180220','20180221','20180222','20180223','20180224','20180225','20180226','20180227','20180228','20180101','20180102','20180103','20180104','20180105','20180106','20180107','20180108','20180109','20180110','20180111','20180112','20180113','20180114','20180115','20180116','20180117','20180118','20180119','20180120','20180121','20180122','20180123','20180124','20180125','20180126','20180127','20180128','20180129','20180130','20180131',]
for i in fechas:
    try:
        busqueda = 'pampa+energia+argentina'
        fechaini = i
        fechafin = i
        regex= 'energia pampa|petrolera pampa|pampa energia'
        data_out = devuelve_palabras_cantidades(busqueda,fechaini,fechafin,regex)   
        #data_out_merged= pd.concat([data_out_merged, data_out], ignore_index=True)
        data_out.to_csv(directorio_salida+'bajadas/'+i+'.csv',index=False)
    except:
        pass














    
    