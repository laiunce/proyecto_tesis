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
fechas = ['20170731','20170801','20170802','20170803','20170804','20170805','20170806','20170807','20170808','20170809','20170810','20170811','20170812','20170813','20170814','20170815','20170816','20170817','20170818','20170819','20170820','20170821','20170822','20170823','20170824','20170825','20170826','20170827','20170828','20170829','20170830','20170831','20170901','20170902','20170903','20170904','20170905','20170906','20170907','20170908','20170909','20170910','20170911','20170912','20170913','20170914','20170915','20170916','20170917','20170918','20170919','20170920','20170921','20170922','20170923','20170924','20170925','20170926','20170927','20170928','20170929','20170930','20171001','20171002','20171003','20171004','20171005','20171006','20171007','20171008','20171009','20171010','20171011','20171012','20171013','20171014','20171015','20171016','20171017','20171018','20171019','20171020','20171021','20171022','20171023','20171024','20171025','20171026','20171027','20171028','20171029','20171030','20171031','20171101','20171102','20171103','20171104','20171105','20171106','20171107','20171108','20171109','20171110','20171111','20171112','20171113','20171114','20171115','20171116','20171117','20171118','20171119','20171120','20171121','20171122','20171123','20171124','20171125','20171126','20171127','20171128','20171129','20171130','20171201','20171202','20171203','20171204','20171205','20171206','20171207','20171208','20171209','20171210','20171211','20171212','20171213','20171214','20171215','20171216','20171217','20171218','20171219','20171220','20171221','20171222','20171223','20171224','20171225','20171226','20171227','20171228','20171229','20171230','20171231']
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














    
    
