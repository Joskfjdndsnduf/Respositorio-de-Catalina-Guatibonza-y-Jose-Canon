import numpy as np
import sympy as sym

x=np.linspace(-0.1,0.1,1000)

def func(a):
    return (np.sqrt(0.01**2-a**2))/(0.5+a) 

def trapecio(f,a,b):

    return (0.5*(b-a)*(f(a)+f(b)))

#print(trapecio(func,-0.01,0.01))

def simpson(f,a,b):
    return (b-a)/6*(f(a)+4*f((a+b)/2))+f(b)

print(simpson(func,-0.01,0.01))