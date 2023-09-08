#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 20:12:27 2023

@author: katedremur
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

valores = pd.read_csv('graphite_mceligot_2016.csv')

class ExpansionTermicaMineral:
    
    def __init__(self, nombre, dureza, rompimiento_por_fractura, color, composicion, lustre, specific_gravity, sistema_cristalino, exp_termica):
        
        super().__init__(self, nombre, dureza, rompimiento_por_fractura, color, composicion, lustre, specific_gravity, sistema_cristalino)
       
        self.exp_termica= exp_termica
        
    
    def coeficiente_exp(self):
        
        temp = valores['celsius_temperature'].tolist()
        vol = valores['volume_cc'].tolist()
        
     
        
        N = 20
        x = np.linspace(0,2*np.pi,N)
        h = x[1] - x[0]
        
        def DerivadaCentral(f,x,h):
    
            d = 0.
            
            if h != 0:
                d = (f(x+h) - f(x-h))/(2*h)
                
            return d
        
        
        
        
        
        
        
        
        
        
       