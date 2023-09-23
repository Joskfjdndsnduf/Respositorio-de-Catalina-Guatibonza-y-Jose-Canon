import numpy as np
import matplotlib.pyplot as plt

#punto 4.2
#N = 1000000
N=np.linspace(10000,1000000,100)
a = 0
b = np.pi
def func_integrate(x):
    return np.exp(-x)*np.sin(x)
def integral(a,b,f,N):
    return (b-a)*sum(f)/N

def errores(a,b,N):
    lista=[]
    for i in N:
        x = np.random.uniform(a,b,int(i))
        fi=func_integrate(x)
        I=integral(a,b,fi,i)
        V=np.abs(I-0.521607)/0.521607
        lista.append(V)
    return lista
#valores=errores(a,b,N)
#plt.scatter(N,valores)
#plt.show()

#punto 4.3
R=1
N = 10000
x = np.random.uniform(-R,R,N)
y = np.random.uniform(-R,R,N)
z = np.random.uniform(-R,R,N)

def integral(R,N,x,y,z):
    suma = 0
    for i in range(N):
        if x[i]**2+y[i]**2+z[i]**2<R**2:
            suma += np.sin(x[i]**2+y[i]**2+z[i]**2)*np.e**(x[i]**2+y[i]**2+z[i]**2)
    I = (2*R)**3*suma/N
    return I

print(integral(R,N,x,y,z))