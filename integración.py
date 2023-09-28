# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 17:38:13 2023

@author: HP
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
#import integrate as god


def funcion(x):
    return np.sin(x)


#a=0
#b=np.pi*0.5


#I=0.5*((b-a)*(funcion(a)+funcion(b)))

x1=np.linspace(np.pi/2,50)
y1=funcion(x)



class Integrator:
    
    def _init_(self,x,f):
        self.x=x
        self.h=self.x[1]-self.x[0]
        self.y=f(self.x)
        
        self.Integral=0.
        
    def Integral(self):
        self.Integral+=0.5*self.y[0]+self.y[-1]#-1 es el último elemento
        
        for i in range(1,self.y.shape[0]-1):#-1 porque no queremos saber a cerca de el último dato debido al self.y[-1
            self.Integral+=self.h
        self.Integral+=np.sum(self.y[1:-1])
        self.Integral+=self.h
        return self.Integral 
    
class Integrator1:
    
    def _init_(self,x,f):
        self.x=x
        self.h=self.x[1]-self.x[0]
        self.y=f(self.x)
        
        self.Integral=0.
        
class Simson1(Integrator1):
    def _init_(self,x,f):
        Integrator._init_(self,x,f) #Utilizar el init del padre para el hijo
        
    def Getintegral(self):
        self.Integral=0
        
        self.Integral+=self.y[0]+self.y[-1]
        for i in range(len(y[1:-1])):
            if i%2==0:
                self.Integral+=4*self.y[i+1]
            else:
                self.Integral+=2*self.y[i+1]
        return self.Integral*self.h/3
    
f = lambda x: np.sin(x)
a=0
b=0.25*np.pi
I=-np.cos(b)+np.cos(a)
print(I)

n=4
Roots, Weights=np.polynomial.legendre.leggauss(n)
print(Roots, Weights)

t=0.5*((b-a)*Roots+a+b)
Integral=0.5*(b-a)*np.sum(Weights*f(t)


x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)
def Getlegendre(n,x,y):
    y=(x**2-1)**n
    poly=sym.diff(y,x,n)/(2**n*np.math.factorial(n))
    
    return poly

Legendre=[]
DLegendre=[]
for i in range(n+1):
    Poly=GetLegendre(i,x,y)
    Legendre.append(Poly)
    DLegendre.append(sym.diff(Poly,x,1))
    
    
    


    
    
                 
        
    
    
    
    

    
