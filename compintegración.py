# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 17:17:56 2023

@author: HP
"""


import numpy as np
import sympy as sym

x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)

#-----------------------------------------------------------------------------

def func(x):
    return -x+3
    

def GetLegendreRecursive(n,x):

    if n==0:
        poly = sym.Number(1)
    elif n==1:
        poly = x
    else:
        poly = ((2*n-1)*x*GetLegendreRecursive(n-1,x)-(n-1)*GetLegendreRecursive(n-2,x))/n
   
    return sym.expand(poly,x)

def GetDLegendre(n,x):
    Pn = GetLegendreRecursive(n,x)
    return sym.diff(Pn,x,1)

def GetNewton(f,df,xn,itmax=10000,precision=1e-14):
    
    error = 1.
    it = 0
    
    while error >= precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(xn)
            
            error = np.abs(f(xn)/df(xn))
            
        except ZeroDivisionError:
            print('Zero Division')
            
        xn = xn1
        it += 1
        
    if it == itmax:
        return False
    else:
        return xn

def GetRoots(f,df,x,tolerancia = 10):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewton(f,df,i)

        if  type(root)!=bool:
            croot = np.round( root, tolerancia )
            
            if croot not in Roots:
                Roots = np.append(Roots, croot)
                
    Roots.sort()
    
    return Roots

def GetAllRootsGLeg(n):

    xn = np.linspace(-1,1,100)
    
    Legendre = []
    DLegendre = []
    
    for i in range(n+1):
        Legendre.append(GetLegendreRecursive(i,x))
        DLegendre.append(GetDLegendre(i,x))
    
    poly = sym.lambdify([x],Legendre[n],'numpy')
    Dpoly = sym.lambdify([x],DLegendre[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots

def GetWeightsGLeg(n):

    Roots = GetAllRootsGLeg(n)

    

    DLegendre = []
    
    for i in range(n+1):
        DLegendre.append(GetDLegendre(i,x))
    
    Dpoly = sym.lambdify([x],DLegendre[n],'numpy')
    Weights = 2/((1-Roots**2)*Dpoly(Roots)**2)
    
    return Weights

#desde acá integral antes solo Legendre------------------------------------------

def integral(f,a,b,n):
    Ip=0
    for i in range(n):
        t=0.5*((GetAllRootsGLeg(n)[i]*(b-a))+(b+a))
        Ip+=GetWeightsGLeg(n)[i]*f(t)
    return Ip*(b-a)*0.5

#Hasta acá una integral ----------------------------------------------------------

def func1(x,y):
    return x+2*y**2

def doble(b,a,c,d,f,n):
    Ip=0
    for i in range(n):
        ti=0.5*((GetAllRootsGLeg(n)[i]*(b-a))+(b+a))
        for j in range(n):
            tj=0.5*((GetAllRootsGLeg(n)[j]*(d-c))+(d+c))
            Ip+=GetWeightsGLeg(n)[i]*GetWeightsGLeg(n)[j]*f(ti,tj)
    return Ip*0.25*(b-a)*(d-c)
print(doble(3,1,1,4,func1,3))

#segunda integral---------------------------------------------------------------

    
    


        
        