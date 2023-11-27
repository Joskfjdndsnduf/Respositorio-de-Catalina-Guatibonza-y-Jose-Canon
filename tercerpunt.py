
import scipy as sc
import numpy as np
import sympy as sp

'''
prinmero

'''
def func(x):
    return (x**2)/3
'''
a
'''

print(sc.integrate.quad(func,0,1))
'''
b
'''
#print(sc.integrate.quad(func,1,2))


'''
segundo
'''
def normal(x):
    return (1/(36*(36*(np.pi*2)**(1/2)))*sp.exp(-0.5*((x-78)/(36))**2))

x=sp.symbols("x")
func=normal(x)
#print(sp.integrate(func,(x,72,np.inf)))

x2=sp.symbols("b")
integral=sp.integrate(func,(x,x2,np.inf))
nota_limite=sp.solve(integral-0.1)
#print(nota_limite)




