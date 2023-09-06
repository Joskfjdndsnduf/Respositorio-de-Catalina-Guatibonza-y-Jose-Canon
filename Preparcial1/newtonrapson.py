#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 21:26:52 2023

@author: katedremur
"""

import numpy as np
import matplotlib.pyplot as plt



def funcion(x):
    #return 5*(1-np.exp(-x)) - x
    return 3*x**5+5*x**4 - x**3

x = np.linspace(-0.4,0.4,50)
y = Function(x)
plt.plot(x,y)
plt.axhline(y = 0,color='r')

def Derivative(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)
def GetNewtonMethod(f,df,xn,itmax=100,precision=1e-8):
    
    error = 1.
    it = 0
    
    while error > precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(f,xn)
            # Criterio de parada
            error = np.abs(f(xn)/df(f,xn))
            
        except ZeroDivisionError:
            print('Division por cero')
            
        xn = xn1
        it += 1
        
   # print('Raiz',xn,it)
    
    if it == itmax:
        return False
    else:
        return xn
root = GetNewtonMethod(Function,Derivative,1000.)
    