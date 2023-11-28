
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

#print(sc.integrate.quad(func,0,1))
'''
b
'''
#print(sc.integrate.quad(func,1,2))


'''
segundo
'''
def normal(x):
    return (1/(36*((np.pi*2)**(1/2)))*sp.exp(-0.5*((x-78)/(36))**2))
#3.2.a
x=sp.symbols("x")
func=normal(x)
maya72=sp.integrate(func,(x,72,np.inf))
#print(maya72)

#3.2.b
x2=sp.symbols("b")
integral=sp.integrate(func,(x,x2,np.inf))
nota_limite=sp.solve(integral-0.1)[0].evalf()
#print(nota_limite)

#3.2.c
punto_limite=sp.solve(integral-0.281)[0].evalf()
#print(punto_limite)

#3.2.d
punto=sp.solve(integral-0.25)[0].evalf()
notapuntos=punto+5
mayanotamenormas5=sp.integrate(func,(x,notapuntos,np.inf)).evalf()
#print(mayanotamenormas5)

#3.2.e
maya84=sp.integrate(func,(x,84,np.inf))
#print(maya84)





