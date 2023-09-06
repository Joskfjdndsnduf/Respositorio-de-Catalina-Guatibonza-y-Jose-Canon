import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,100)

def func(x):
    return ((np.e)**-x)-x

def Derivative(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)
der=(func,x)

def GetNewtonMethod(f,df,xn,itmax=100,precision=1e-8):
    
    error = 1.
    it = 0
    
    while error > precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(f,xn)
   
            error = np.abs(f(xn)/df(f,xn))
            
        except ZeroDivisionError:
            print('Division por cero')
            
        xn = xn1
        it += 1
        

    
    if it == itmax:
        return Flase
    else:
        return xn
print(GetNewtonMethod(func,der,1.))



