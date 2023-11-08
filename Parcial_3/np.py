import numpy as np
import sympy as sym

x0 = sym.Symbol('x0',real=True)
x1 = sym.Symbol('x1',real=True)
x2 = sym.Symbol('x2',real=True)
x3 = sym.Symbol('x3',real=True)
x4 = sym.Symbol('x4',real=True)

A= np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])
b=  np.array([[1,2,3,4,5]])
v= np.array([[1,1,1,1,1]])
def desc_conj (A,b,v,t=0.01):
    rv=np.dot(A,v)
    r=np.max(np.absolute(np.max(np.dot(A,v))))  
    p=-rv
    k=0
    while r > t and k <=5:
        print(np.dot(np.transpose(r),p))

    
        alf= -(np.dot((r.T),p)/((np.dot(np.dot(p.T,A),p))))
        x= float(x + np.dot(alf,p))
        rv= float(np.dot(A,x[k+1])-b)
        r=np.max(np.absolute(np.max(np.dot(A,v)))) 
        bk= float((np.dot(r[k+1].T,A)*p[k])/((np.dot(p[k].T),A)*p[k]))
        pk= float(-r[k+1]+np.dot(b[k+1],p[k]))
        k=k+1
        
        return x[k]
    
desc_conj(A,b,v.T,t=0.01)