# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 20:19:32 2023

@author: HP
"""

import numpy as np

def monedas(N):
    ev=0
    for i in range(N):
        secuencia = np.random.choice([1, -1], size=4)
        if np.sum(secuencia)==0:
    
            ev+=1
    prob=ev/N
    return prob
   
print(monedas(10**5))