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



def GetAllRootsGLagguere(n):

    xn = np.linspace(0,n+((n-1)*np.sqrt(n)),100)
    
    Laguerre = []
    
    for i in range(n+1):
        Laguerre.append(GetLaggereRecursive(i,x))

    
    poly = sym.lambdify([x],Laguerre[n],'numpy')
    Roots = GetRootsGLeg(poly,xn)
    
    return Roots