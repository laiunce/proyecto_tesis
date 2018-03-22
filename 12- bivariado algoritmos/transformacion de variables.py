#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 19:44:22 2018

@author: laiunce
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 17:37:08 2018

@author: LAC40641
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 17:11:14 2018

@author: LAC40641
"""
import pandas as pd
from sklearn.cross_validation import cross_val_score
import numpy as np

import pandas as pd
import numpy as np
import itertools
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report,confusion_matrix

def plot_desicion_boundary(X, y, clf, title = None):
    '''
    Helper function to plot the decision boundary for the SVM
    '''
    
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    plt.figure(figsize = (10, 8))
    plt.contourf(xx, yy, Z, alpha=0.4)
    plt.scatter(X[:, 0], X[:, 1], c=y, alpha=0.8)
    
    if title is not None:
        plt.title(title)
    
    # highlight the support vectors
    #plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=80,
    #            facecolors='none', zorder=10)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()




def plotea_valores(X,n_class):
    n_class = 2
    # let's have a look of the data first
    plt.figure(figsize = (10,8))
    for i, c, s in (zip(range(n_class), ['b', 'g'], ['o', '^'])):
        ix = y == i
        plt.scatter(X[:, 0][ix], X[:, 1][ix], color = c, marker = s, s = 60)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
    
def dev_transf_pred(X,y,nombre):
    
    lista_kern_acc = []
    ker= ['rbf','sigmoid','linear']
    #ker= ['linear']
    
    for k in ker:
        l=[]
        clf = svm.SVC(kernel=k)
        scores = cross_val_score(clf, X, y, cv=10, scoring='accuracy')
        print(np.mean(scores))
        l.append(k)
        l.append(np.mean(scores))
        lista_kern_acc.append(l)
         
    
    #encuentra registros con mayor accuracy
    pds= pd.DataFrame(lista_kern_acc)
    kernel_ent= list(pds[pds[1] == np.max(pds[1])][0])[0]
    
    
    clf2 = svm.SVC(kernel=kernel_ent, probability=True)
    clf2.fit(X,y)
    #plot_desicion_boundary(X, y, clf2)  
    
    #predicciones
    
      
    
    return(list(pd.DataFrame(clf2.predict_proba(X))[0]),clf2,nombre)


def get_rid_of_nulls(value):
    if pd.isnull(value):
        return 0
    else:
        return value


# let's construct a dataset that not linearly separatable
X1, y1 = datasets.make_gaussian_quantiles(cov=2.,
                                 n_samples=400, n_features=2,
                                 n_classes=2, random_state=1)

X2, y2 = datasets.make_gaussian_quantiles(mean=(3, 3), cov=1.5,
                                 n_samples=400, n_features=2,
                                 n_classes=2, random_state=1)



directorio_ruta = '/Users/laiunce/Google Drive/scraping/12 - bivariado algoritmos/'

data_titanic=pd.read_csv(directorio_ruta+'titanic2.csv',encoding='latin-1',low_memory=False)


#variables_iterar = ['Pclass','Age','SibSp','Parch','Fare']
variables_iterar = ['Pclass','Age','SibSp','Parch']
target='Survived'


subset_var = variables_iterar.copy()
subset_var.append(target)
data_titanic[subset_var]


#crea lista de variables tomadas de a dos


lista_combinaciones = list(itertools.combinations(variables_iterar,2))

lista_combinaciones[0][0]
            

#
lista_modelos = []


for i in lista_combinaciones:
    var1= i[0]
    var2= i[1]
    
    
    
    df= data_titanic[[var1,var2]]
    df[var1] = df[var1].apply(get_rid_of_nulls)
    df[var2] = df[var2].apply(get_rid_of_nulls)
    
    
    pred = dev_transf_pred(df.as_matrix(),data_titanic[target].as_matrix(),var1+'_'+var2)
    
    lista_modelos.append(pred)
    
    clf2 = pred[1]
    clf2.fit(df.as_matrix(),data_titanic[target].as_matrix())
    #plot_desicion_boundary(df.as_matrix(), data_titanic[target].as_matrix(), clf2)
    

#agrega variables de probabilidad al dataset
for v in lista_modelos:
    data_titanic[v[2]] = v[0]
    
    
    
###### evaluacion del modelo cortanto linealmete por probailidades devueltas

#'rbf','sigmoid','linear'

df= data_titanic[['Pclass_Age','Pclass_SibSp','Pclass_Parch','Age_SibSp','Age_Parch','SibSp_Parch']]
clf = svm.SVC(kernel='linear')
scores = cross_val_score(clf, df.as_matrix(), data_titanic[target].as_matrix(), cv=10, scoring='accuracy')
print('acc: '+str(np.mean(scores)))



#plotea bivariado de probabilidades con target
import seaborn as sns
sns.lmplot(x="Age_SibSp", y="SibSp_Parch", hue=target, data=data_titanic,fit_reg=False)




