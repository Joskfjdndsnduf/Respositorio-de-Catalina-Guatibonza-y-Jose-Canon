import sympy as sym
import numpy as np

x = sym.Symbol('x',real=True)

def derivada(x,n):
   dif=sym.diff(((np.e**-x)*x**n),x,n)
   return dif

def polinomio(x,n):
   return ((np.e**x)/sym.factorial(n))*derivada(x,n)


def GetDLaggere(n,x):
    Pn = polinomio(x,n)
    return sym.diff(Pn,x,1)

def GetNewton(f,df,xn,itmax=10000,precision=1e-14):
    error = 1
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
            if croot not in Roots and croot>0:
                Roots = np.append(Roots, croot)
    Roots.sort()
    return Roots

def GetAllRootsGLag(n,x):
    xn = np.linspace(0,n+((n-1)*np.sqrt(n)),100)
    Laggere = []
    DLaggere = []
    
    for i in range(n+1):
        Laggere.append(polinomio(x,i))
        DLaggere.append(GetDLaggere(i,x))
    
    poly = sym.lambdify([x],Laggere[n],'numpy')
    Dpoly = sym.lambdify([x],DLaggere[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)
    return Roots

def raices(n):
    lista=[]
    i=0
    while i<=n:
        if i==0:
          i+=1
        else:
            lista.append(GetAllRootsGLag(i,x))
            i+=1

    return lista
#print(raices(3))





                              



       