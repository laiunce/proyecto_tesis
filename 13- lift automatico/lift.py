import csv
import pandas as pd
import numpy as np

#https://www.dataquest.io/blog/pandas-pivot-table/

directorio = '/Users/laiunce/Google Drive/scraping/lift automatico deteccion/'
data=pd.read_csv(directorio+'titanic.csv')



def calcula_metrica_lift(data,var_analizar,target):

    data_set = data[[var_analizar,target]]
    agrupado_cantidad = data_set[var_analizar].groupby(data_set[target]).count()
    
    '''
    lista_share=[]
    for i in range(0,len(agrupado_cantidad)):
        lista_valores = []
        lista_valores.append(agrupado_cantidad.index[i])
        lista_valores.append(agrupado_cantidad[i]/sum(agrupado_cantidad))
        lista_share.append(lista_valores)
    '''    
    
    lista_share=[]
    for i in range(0,len(agrupado_cantidad)):
        lista_share.append(list(agrupado_cantidad)[i]/sum(agrupado_cantidad))
        
    frecuencia_pivot= data_set.pivot_table(index=var_analizar, columns=target, aggfunc=len, fill_value=0)
    lista_totales = list(data_set[var_analizar].groupby(data_set[var_analizar]).count())    
    porcentaje_categoria = (frecuencia_pivot.T/lista_totales).T
    
    #calculo de lifts
    
    lifts_relativos = (porcentaje_categoria/lista_share)-1
    
    #share por target
    
    lista_totales_target = list(data_set[target].groupby(data_set[target]).count())
    pivote_share_target = frecuencia_pivot/lista_totales_target
    
    ##
    salida_lifts_shares = pivote_share_target*abs(lifts_relativos)
    maximo = np.matrix(salida_lifts_shares).max()
    
    return maximo


#'Embarked'
#'Sex'

var_analizar = 'Pclass'
target= 'Survived'


maximo = calcula_metrica_lift(data,var_analizar,target)

if maximo > 0.10:
    print('candidata')








