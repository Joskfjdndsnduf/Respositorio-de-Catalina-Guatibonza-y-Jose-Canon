import numpy as np
import sympy as sym

x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)

#-------------------------------------------------------------Gaus legendre---------------------------------------------

def GetLegendreRecursive(n,x):

    if n==0:
        poly = sym.Number(1)
    elif n==1:
        poly = x
    else:
        poly = ((2*n-1)*x*GetLegendreRecursive(n-1,x)-(n-1)*GetLegendreRecursive(n-2,x))/n
   
    return sym.expand(poly,x)

def GetDLegendre(n,x):
    Pn = GetLegendreRecursive(n,x)
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

def GetAllRootsGLeg(n):

    xn = np.linspace(-1,1,100)
    
    Legendre = []
    DLegendre = []
    
    for i in range(n+1):
        Legendre.append(GetLegendreRecursive(i,x))
        DLegendre.append(GetDLegendre(i,x))
    
    poly = sym.lambdify([x],Legendre[n],'numpy')
    Dpoly = sym.lambdify([x],DLegendre[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots

def GetWeightsGLeg(n):

    Roots = GetAllRootsGLeg(n)

    

    DLegendre = []
    
    for i in range(n+1):
        DLegendre.append(GetDLegendre(i,x))
    
    Dpoly = sym.lambdify([x],DLegendre[n],'numpy')
    Weights = 2/((1-Roots**2)*Dpoly(Roots)**2)
    
    return Weights
#-----------------------------------------------------Laguerre----------------------------------------------
def GetLaggereRecursive(n,x):

    if n==0:
        poly = 1
    elif n==1:
        poly = -x+1
    else:
        poly = ((2*n-1-x)*GetLaggereRecursive(n-1,x)-(n-1)*GetLaggereRecursive(n-2,x))/n
    return sym.simplify(poly)


def GetDLaggere(n,x):
    Pn = GetLaggereRecursive(n,x)
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

def GetAllRootsGLag(n):
    xn = np.linspace(0,n+((n-1)*np.sqrt(n)),100)
    Laggere = []
    DLaggere = []
    
    for i in range(n+1):
        Laggere.append(GetLaggereRecursive(i,x))
        DLaggere.append(GetDLaggere(i,x))
    
    poly = sym.lambdify([x],Laggere[n],'numpy')
    Dpoly = sym.lambdify([x],DLaggere[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots


def GetWeightsGLag(n):

    Roots = GetAllRootsGLag(n)
    weights=[]
    for i in range(n):
        Lagroot = GetLaggereRecursive(n+1,Roots[i])
        Weight = Roots[i]/(((n+1)**2)*(Lagroot)**2)
        weights.append(Weight)
    
    return weights
#--------------------------------------Integral--------------------------------------------------
def integralleg(f,a,b,n):
    Ip=0
    for i in range(n):
        t=0.5*((GetAllRootsGLeg(n)[i]*(b-a))+(b+a))
        Ip+=GetWeightsGLeg(n)[i]*f(t)
    return Ip*(b-a)*0.5

def integrallag(f,n):
    pesos=GetWeightsGLag(n)
    raices=GetAllRootsGLag(n)  
    I=0
    for i in range(n):
        I+= pesos[i]*f(raices[i])
        i+=1
    return I
#------------------------------------funciones----------------------------------------------------
lim1=((6.626*10**-34)*((3*10**8)/(100*10**-9)))/((1.3806*10**-23)*5772)
lim2=(6.626e-34*((3e8)/(400e-9)))/(1.3806e-23*5772)

<<<<<<< HEAD
n=20

=======
n=7
#El código no funciona a n mayor de 7 pero funciona y da el número
>>>>>>> 8e4b7ca250b390730fe8994f527a197e655620ea
def func1(x):
    return x**3/((np.e**x)-1)
def func2(x):
    return ((x**3)*((np.exp(x))-1))/((np.exp(x))-2+(1/np.exp(x)))
numerador=integralleg(func1,lim2,lim1,n)
denominador=integrallag(func2,n)

respuesta=numerador/denominador

print(respuesta)

