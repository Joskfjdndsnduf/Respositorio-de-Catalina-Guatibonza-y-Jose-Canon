#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 23:20:25 2023

@author: katedremur
"""

import pandas as pd
import matplotlib.pyplot as plt


from expansiontermicamineral import  ExpansionTermicaMineral


olivino = pd.read_csv('olivine_angel_2017.csv')
grafito = pd.read_csv('graphite_mceligot_2016.csv')

def alfas():
    
    alfa_oliv=ExpansionTermicaMineral.alfa(olivino)

    volol = olivino['volume_cc'].tolist()
    alfa_graf=ExpansionTermicaMineral.alfa(grafito)
  
    volgra = grafito['volume_cc'].tolist()
    
    plt.plot(alfa_oliv, volol)
    plt.plot(alfa_graf,volgra)