#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 23:36:44 2018

@author: laiunce
"""
from math import sqrt
from numpy import concatenate
from matplotlib import pyplot
from pandas import read_csv
import pandas as pd
import pylab as pylb


directorio = '/Users/laiunce/Google Drive/scraping/8- robot baja series historicas/acciones_arg'

lista_emp = ['3m-co-drc.csv','agrometal.csv','alcoa-inc..csv','alphabet-inc.csv','alto-palermo.csv','aluar.csv','american-express-co-ba.csv','american-international-group-inc.csv','apple-inc..csv','at-t-inc..csv','autopistas-sol.csv','b-santander-ri.csv','banco-bilbao-vizcaya-argentaria.csv','banco-santander-brasil-sa-ba.csv','banco-santander-rio-sa.csv','bank-of-america-corp.csv','barrick-gold.csv','bco-hipotecari.csv','bco-patagonia.csv','bhp-ltd.csv','bodegas-esmeralda-sa.csv','boldt.csv','bolsas-y-mercados-argentinos-sa.csv','bristol-myers-squibb-co..csv','cablevision.csv','camuzzi.csv','capex.csv','caputo.csv','carboclor.csv','carlos-casado.csv','caterpillar-inc-ar.csv','celulosa.csv','central-costan.csv','central-puerto.csv','chevron-corp-ar.csv','china-mobile-ar.csv','cisco-systems.csv','citigroup-incorporated.csv','coca-cola-co-ba.csv','colgate-palmolive-company.csv','colorin.csv','comer-del-plat.csv','compania-introductora-buenos-aires.csv','con-del-oeste.csv','consultatio-s..csv','cresud.csv','domec-compania-de-artefactos-domest.csv','du-pont-de-nemours---company.csv','dycasa.csv','ecogas.csv','edenor.csv','empresa-distribuidora-electrica.csv','ferrum.csv','fiplasto.csv','frances.csv','garovaglio.csv','general-electric-co..csv','goldcorp.csv','gp-fin-galicia.csv','grimoldi.csv','grupo-clarin.csv','grupo-financiero-valores.csv','grupo-supervielle-sa.csv','havanna-sa.csv','hewlett-packard.csv','home-depot-inc..csv','i-y-e-de-la-pa.csv','indupa.csv','inst-rosembusc.csv','insumos-agroquimicos-sa.csv','intel-ar.csv','international-business-machines.csv','inversora-juramento.csv','irsa.csv','johnson---johnson-co.csv','jpmorgan-chase---co..csv','juan-minetti.csv','kimberly-clark-corp..csv','koninklijke-philips-electronics.csv','laboratorios-richmond.csv','ledesma.csv','lockheed-martin-corp.csv','loma-negra-ba.csv','longvie.csv','macro.csv','mcdonald-corp.csv','meranol-saci.csv','mercadolibre-inc.csv','merck---co-inc..csv','metrogas.csv','microsoft-corp-ar.csv','mirgor.csv','moli-juan-semi.csv','molinos-agro.csv','molinos.csv','morixe.csv','national-grid-ar.csv','newmont-mining-drc.csv','nike-inc.csv','nokia.csv','nortel-inversora-sa.csv','novartis-drc.csv','ovoprot-international-sa.csv','pampa-energia.csv','pepsico-inc.csv','pet.del-conosu.csv','petrobras-arg.csv','petrochina-co.csv','petrolera-pampa-sa.csv','pfizer-inc.-ar.csv','polledo.csv','procter---gamble.csv','quickfood.csv','rigolleau.csv','royal-dutch-shell-a-ar.csv','san-miguel.csv','siderar.csv','siemens-a.g..csv','telecom.csv','tglt-sa.csv','total-cedear.csv','tran-gas-del-s.csv','tran-gas-norte.csv','transener.csv','verizon-communications-inc..csv','wal-mart-stores-inc.csv','walt-disney-company.csv','yamana-gold-drc.csv','ypf-sociedad.csv']

for i in lista_emp:
    
    try:

    
        df = pd.read_csv(directorio+'/'+i )
#filtro de fecha
        df = df[df['fecha']>20160000]
        df=df.sort_values(['fecha'], ascending=[1])
        
         
        lista =list(df['ultima'])
        
        pyplot.clf()
        # grafico realidad vs predicho
        pyplot.plot(lista, label='serie')
        pyplot.legend()
        pyplot.savefig(directorio+'_graficos/'+i+'.png')    

    except:
        pass    