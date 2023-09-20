# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 17:54:49 2023

@author: HP
"""
import sympy as sym
x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)

def GetLaggereRecursive(n,x):

    if n==0:
        poly = 1
    elif n==1:
        poly = -x+1
    else:
        poly = ((2*n-1-x)*GetLaggereRecursive(n-1,x)-(n-1)*GetLaggereRecursive(n-2,x))/n
   
    return sym.simplify(poly)

