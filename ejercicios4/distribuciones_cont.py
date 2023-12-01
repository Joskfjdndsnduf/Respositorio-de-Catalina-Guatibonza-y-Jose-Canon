import scipy as sp
import numpy as np
import sympy as sym

x=sym.Symbol('x',real=True)
y=sym.Symbol('y',real=True)

def funci(x,y):
    return 2/3*(x+2*y)
func=funci(x,y)
#a
a=sym.integrate(func,(x,0,1))
b=sym.integrate(a,(y,0,1))


#b
g=sym.integrate(func,(y,0,1))

h=sym.integrate(func,(x,0,1))

#c
Ex=sym.integrate(x*g,(x,0,1))
#d
Ey=sym.integrate(y*h,(y,0,1))
#e
Exy=sym.integrate(x*y*func,(x,0,1),(y,0,1))
co1=Exy-Ex*Ey

#f
mux=sym.integrate(x*g,(x,0,1))
muy=sym.integrate(y*h,(y,0,1))
co2=sym.integrate((x-mux)*(y-muy)*func,(x,0,1),(y,0,1))
#f
''''
No son independientes debido a que la covarianza no es 0

'''
