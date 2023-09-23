import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2,2000)

def func(x):
    y=np.pi*((0.25/2)**2)*0.05*np.cos(3.5*x)*np.cos(2*np.pi*1000*x)
    return y
def grafica(x):
    y=func(x)
    plt.plot(x,y)
    plt.show()

#grafica(x)#hacer la gráfica
def derivada(f, t, h=1e-6):
    return (f(t+h)-f(t-h))/(2*h)
    
                           
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
        return xn1
    else:
        return xn
def GetAllRoots(x, tolerancia=10):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewtonMethod(func,derivada,i)
        
        if root != False:
            
            croot = np.round(root, tolerancia)
            
            if croot not in Roots:
                Roots = np.append(Roots,croot)
            if len(Roots)==3:
                break
                
    Roots.sort()

print(GetAllRoots(x))


print(newton_rhapson(0,func,10e-8))

x = np.random.uniform(a,b,N)
x1 = np.random.uniform(a,b,N1)
x2 = np.random.uniform(a,b,N2)
x3 = np.random.uniform(a,b,N3)

def func_integrate(x):
    return np.exp(-x)*np.sin(x)
lista=[]
fi = func_integrate(x)
fi1= func_integrate(x1)
fi2= func_integrate(x2)
fi3= func_integrate(x3)
def integral(a,b,f,N):
    return (b-a)*sum(fi)/N

I=np.abs(integral(a,b,fi,N)-0.521607)/0.521607
I1=np.abs(integral(a,b,fi1,N1)-0.521607)/0.521607
I2=np.abs(integral(a,b,fi2,N2)-0.521607)/0.521607
I3=np.abs(integral(a,b,fi3,N3)-0.521607)/0.521607
lista=[I,I3,I2,I1]
listay=[N,N3,N2,N1]
plt.plot(listay,lista)
plt.xscale("log")
plt.show()
    

