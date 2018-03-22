#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 21:51:45 2018

@author: laiunce
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier


#directorio_ruta = '/Users/laiunce/Google Drive/scraping/12 - bivariado algoritmos/'
#data_titanic=pd.read_csv(directorio_ruta+'titanic2.csv',encoding='latin-1',low_memory=False)

df= data_titanic[['Pclass_Age','Pclass_SibSp','Pclass_Parch','Age_SibSp','Age_Parch','SibSp_Parch']]
#df= data_titanic[['Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']]

target='Survived'

clf = DecisionTreeClassifier()
scores = cross_val_score(clf, df.as_matrix(), data_titanic[target].as_matrix(), cv=10, scoring='accuracy')
print('acc: '+str(np.mean(scores)))



