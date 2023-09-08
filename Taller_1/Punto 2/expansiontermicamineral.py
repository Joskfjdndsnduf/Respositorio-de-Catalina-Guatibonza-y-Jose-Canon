#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 20:12:27 2023

@author: katedremur
"""

import matplotlib.pyplot as plt
import pandas as pd




class ExpansionTermicaMineral ():
    
    def __init__(self, nombre, dureza, rompimiento_por_fractura, color, composicion, lustre, specific_gravity, sistema_cristalino, temp, vol):
        
        super().__init__(self, nombre, dureza, rompimiento_por_fractura, color, composicion, lustre, specific_gravity, sistema_cristalino)
       
        self.temp= temp
        self.vol=vol
        
        
    def alfa():
        
        
        valores = pd.read_csv('graphite_mceligot_2016.csv')
        temp = valores['celsius_temperature'].tolist()
        vol = valores['volume_cc'].tolist()
        i=0
        coeficientes = []
        for i in range(len(vol)):
            
            coeficientes.append ( 1/vol[i]*((max(vol)-min(vol))/(max(temp)-min(temp))))
            
            return coeficientes
        plt.plot(vol,coeficientes)
            
            
            
            
            
        
        
            
    
   

        
        
        
        
        
        
        
        
       