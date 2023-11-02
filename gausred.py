import numpy as np
import sympy as sym

a=np.array([[2,1,1],[1,1,-2],[5,10,5]])
'''
crear la matriz

'''
b = np.array([8,-2,10])
'''
la parte de solución de la matriz, está en la foto del ipad

'''
n = np.shape(a)[0]
M = np.zeros(shape=(n,n+1))
'''
Crear la matriz de 0

'''
M[:,0:n] = a

'''
pone los valores de la matriz a en la matriz M
'''
M[:,n] = b
'''
Pone la "solución b en la matriz m dando el aspecto que siempre hemos visto en reducción
de Gaus
'''

# j son columnas, i son filas
def reduccion(a):
    
    for j in range(n-1):
        for i in range(j+1,n):
            coeff=a[i,j]/a[j,j]
            nf=a[i,:]-(coeff*a[j,:])
            a[i,:]=nf
    return a

"""
Valores propios
"""
        
#m=np.array([[1,2,-1],[1,0,1],[4,-4,5]])
m=np.array([[2,-1],[-4,2]])
q=np.array([4,3])
#q=np.array([7,8,9])

def mew(q,m):
    a=np.matmul(q.T,m)
    return np.matmul(a,q)
def potinv(m,q):
    for i in range(10):
        z=np.matmul(m,q)
        q=z/np.sqrt(np.matmul(z.T,z))
        j=mew(q,m)
    return j

print(potinv(m,q))




'''
multiplicación de matrices

'''
u=np.array([[5,-4,-2],[5,-5,4],[2,5,-4],[-5,4,3],[3,-4,-3]])
v=np.array([[5,-2,-3]])
vp=np.transpose(v)
def multi(m,vp):
    c1=len(m[0])
    f2=len(vp)
    if c1!=f2:
        print("las matrices no se pueden multiplicar")
    else:
        f1=len(m)
        c2=len(vp[0])
        r=np.zeros(shape=(f1,c2))

        for i in range(f1):
            for j in range(c2):
                for k in range(c1):
                    r[i][j]+=m[i][k]*vp[k][j]
        return r

                    


#print(multi(u,vp))

m=np.array([[1,2,-1],[1,0,1],[4,-4,5]])

q=np.array([1,2,1])

def mew(q,m):
    a=multi(q.T,m)
    return multi(a,q)
def potinv(m,q):
    for i in range(10):
        z=multi(m,q)
        q=z/np.sqrt(np.matmul(z.T,z))
        j=mew(q,m)
    return j

#print(potinv(m,q))