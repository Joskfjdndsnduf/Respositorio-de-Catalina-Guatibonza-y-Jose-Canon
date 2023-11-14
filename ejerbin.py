import numpy as np
import matplotlib.pyplot as plt

p=np.linspace(0,1)
N=1000
def graf(p,N,n1,n2):
    
    datos1=[]
    datos2=[]
    pa=0
    for i in p:
        acep1=0
        acep2=0
        a=np.random.binomial(n1,i,size=N)
        b=np.random.binomial(n2,i,size=N)
        for j in range(N):
            if a[j]<=1:
                acep1+=1
            if b[j]<=5:
                acep2+=1
        pa=acep1/N
        print(pa)
        pa2=acep2/N
        datos1.append(pa)
        datos2.append(pa2)
    plt.plot(p,datos1)
    plt.plot(p,datos2)
    plt.xlabel("p")
    plt.ylabel("probabilidad aceptación")
    plt.legend()
    plt.show()
                
print(graf(p,N,5,25))      


    
    




