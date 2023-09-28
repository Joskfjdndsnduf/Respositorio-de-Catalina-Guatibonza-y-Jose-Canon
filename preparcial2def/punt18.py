import sympy as sym
import numpy as np
from math import e
from math import sqrt

x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)

def GetHermiteRecursive(n,x):

    if n==0:
        poly = sym.Number(1)
    elif n==1:
        poly = 2*x
    else:
        poly = (2*x*GetHermiteRecursive(n-1,x)-2*(n-1)*GetHermiteRecursive(n-2,x))
   
    return sym.expand(poly,x)

def GetDHermite(n,x):
    Pn = GetHermiteRecursive(n,x)
    return sym.diff(Pn,x,1)


def GetNewton(f,df,xn,itmax=10000,precision=1e-14):
    
    error = 1.
    it = 0
    
    while error >= precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(xn)
            
            error = np.abs(f(xn)/df(xn))
            
        except ZeroDivisionError:
            print('Zero Division')
            
        xn = xn1
        it += 1
        
    if it == itmax:
        return False
    else:
        return xn
    
def GetRoots(f,df,x,tolerancia = 10):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewton(f,df,i)

        if  type(root)!=bool:
            croot = np.round( root, tolerancia )
            
            if croot not in Roots:
                Roots = np.append(Roots, croot)
                
    Roots.sort()
    
    return Roots

def GetAllRootsGHer(n):

    xn = np.linspace(-sqrt(4*n+1),sqrt(4*n+1),100)
    
    Hermite = []
    DHermite = []
    
    for i in range(n+1):
        Hermite.append(GetHermiteRecursive(i,x))
        DHermite.append(GetDHermite(i,x))
    
    poly = sym.lambdify([x],Hermite[n],'numpy')
    Dpoly = sym.lambdify([x],DHermite[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots
def GetWeightsGHer(n):

    Roots = GetAllRootsGHer(n)

    Weights = []


    for valor in range(n):
        HerRoot = GetHermiteRecursive(n-1,Roots[valor])
        weight = (2**(n-1)*np.math.factorial(n)*sqrt(np.pi))/((n**2)*HerRoot**2)
        Weights.append(weight)


    return Weights

def func(x):
    return (1/(2*np.sqrt(np.pi)))*4*x**2

def integrar(f,n):
    I=0
    i=1
    pesos=GetWeightsGHer[n]
    raices=GetAllRootsGHer[n]
    for i in range(n):
        I+=pesos[i]*f(raices[i])
        
    return I

print(integrar(func,1))
    

