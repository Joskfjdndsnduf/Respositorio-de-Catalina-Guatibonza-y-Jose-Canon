import numpy as np
import time

G = np.array([lambda x,y: -114.6+y*np.cos(x),
     lambda x,y:((-y*np.sin(x)+270*((1/(4*25*(np.sin(x)**2)))+(np.sqrt(2)/(2*25*(np.sin(x)**2))))))])

def GetF(G,r):
    
    n = r.shape[0]
    
    v = np.zeros_like(r)
    
    for i in range(n):
        v[i] = G[i](r[0],r[1])
        
    return v

def GetJacobian(f,r,h=1e-6):
    
    n = r.shape[0]
    
    J = np.zeros((n,n))
    
    for i in range(n):
        for j in range(n):
            
            rf = r.copy()
            rb = r.copy()
            
            rf[j] = rf[j] + h
            rb[j] = rb[j] - h
            
            J[i,j] = (f[i](rf[0],rf[1]) - f[i](rb[0],rb[1]))/(2*h)
            
    
    return J
def NewtonRaphson(G,r,itmax=1000,error=1e-9):
    
    it = 0
    d = 1.
    dvector = []
    
    while d > error and it < itmax:
        
        rc = r
        
        F = GetF(G,rc)
        J = GetJacobian(G,rc)
        InvJ = np.linalg.inv(J)
        
        r = rc - np.dot(InvJ,F)
        
        diff = r - rc
        
        d = np.max( np.abs(diff) )
        
        dvector.append(d)
        it += 1
    

    return r,dvector



r,dvector=NewtonRaphson(G,np.array([2,1]))
print(r)
print(dvector)

print(np.sin(r[0]))
