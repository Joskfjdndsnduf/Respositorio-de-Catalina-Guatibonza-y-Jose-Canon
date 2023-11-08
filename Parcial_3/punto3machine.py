import numpy as np


def f(x):
    return np.abs(x-2)

Dx = lambda f,x,h=1e-5: (f(x+h) - f(x-h))/(2*h)

def Minimizer(f, N=300, gamma=0.01):
    
    r = np.zeros(N)

    r[0] = np.random.uniform(-5,5)
    
    for i in range(1,N):
        r[i] = r[i-1] - gamma*Dx(f,r[i-1])
        
    return r
r=Minimizer(f)
print(r[-1])

"no tiene sentido que dé el gradiente negativo así que no puede dar debido a que no es diferenciable en la punta de la gráfica haciendo imposible miximizar"