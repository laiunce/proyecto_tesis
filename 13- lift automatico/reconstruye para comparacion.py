import csv
import pandas as pd
import numpy as np

#https://www.dataquest.io/blog/pandas-pivot-table/

directorio = '/Users/laiunce/Google Drive/scraping/lift automatico deteccion/'
data=pd.read_csv(directorio+'comparacion_cable.csv')

with open(r'/Users/laiunce/Google Drive/scraping/lift automatico deteccion/salida_comparacion.csv', 'a') as f:
    f.write('AGREEMENT_TYPE,categoria\n') 
    for i in data.iterrows():
        for c in range(1,i[1][2]+1):
            print (str(i[1][0])+','+str(i[1][1])+'\n')
            f.write(str(i[1][0])+','+str(i[1][1])+'\n') 