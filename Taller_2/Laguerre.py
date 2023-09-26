# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 17:54:49 2023

@author: HP
"""
import sympy as sym
import numpy as np

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


def GetDLaggere(n,x):
    Pn = GetLaggereRecursive(n,x)
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

def GetAllRootsGLag(n):
    xn = np.linspace(0,n+((n-1)*np.sqrt(n)),100)
    Laggere = []
    DLaggere = []
    
    for i in range(n+1):
        Laggere.append(GetLaggereRecursive(i,x))
        DLaggere.append(GetDLaggere(i,x))
    
    poly = sym.lambdify([x],Laggere[n],'numpy')
    Dpoly = sym.lambdify([x],DLaggere[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots


def GetWeightsGLag(n):

    Roots = GetAllRootsGLag(n)
    weights=[]
    for i in range(n):
        Lagroot = GetLaggereRecursive(n+1,Roots[i])
        Weight = Roots[i]/(((n+1)**2)*(Lagroot)**2)
        weights.append(Weight)
    
    return weights
print(GetAllRootsGLag(20))








