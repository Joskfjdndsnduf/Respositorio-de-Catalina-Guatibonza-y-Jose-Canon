import numpy as np
import matplotlib.pyplot as plt

lambd=5
N=1000
def graf(lambd,N):
    
    acep1=0
    a=np.random.poisson(lambd,size=N)
    for j in range(N):
        if a[j]<=2:
            acep1+=1

        pa=acep1/N
    return pa


                
print(graf(lambd,N))  