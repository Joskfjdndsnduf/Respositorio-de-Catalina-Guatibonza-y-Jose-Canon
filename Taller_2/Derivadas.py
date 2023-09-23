import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2,2000)

def func(x):
    y=np.pi*((0.25/2)**2)*0.05*np.cos(3.5*x)*np.cos(2*np.pi*7*x)
    return y
def grafica(x):
    y=func(x)
    plt.plot(x,y)
    plt.show()

#grafica(x)#hacer la gráfica
def derivada(f, t, h=1e-6):
    return (f(t+h)-f(t-h))/(2*h)

def I(t):
    return (-1/(0.25/2))*derivada(func,t)

def graficaI(x):
    y=I(x)
    plt.plot(x,y)
    plt.show()
#graficaI(x)
                    
def newton_rhapson(x_0, f, epsilon):
    x_n = x_0
    while np.abs(f(x_n)) > epsilon:
        x_n -= f(x_n)/derivada(f,x_n,0.0001)
    return x_n

def GetNewton(f,df,xn,itmax=10000,precision=1e-14):
    
    error = 1.
    it = 0
    
    while error >= precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(f,xn)
            
            error = np.abs(f(xn)/df(f,xn))
            
        except ZeroDivisionError:
            print('Zero Division')
            
        xn = xn1
        it += 1
        if it == itmax:
            return False
        else:
            return xn

def GetAllRoots(x, tolerancia=10):
    
    Roots = np.array([])
    
    for i in x:
        root = GetNewton(I,derivada,i)
        print(root)
        
        if root != False:
            
            croot = np.round(root,tolerancia)

            
            if croot not in Roots:
                Roots = np.append(Roots,croot)
        if len(Roots)==2:
           break
                
    Roots.sort()
    
    return Roots
print(len(GetAllRoots(x)))



