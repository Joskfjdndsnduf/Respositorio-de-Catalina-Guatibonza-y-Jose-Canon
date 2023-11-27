import numpy as np



pri=np.array([[0.25,0,0.5,0.25]])

T= np.array([[0.4,0.2,0.2,0.2],[0.25,0.25,0.25,0.25],[0.3,0.3,0.1,0.3],[0.1,0.1,0.1,0.7]])
g=np.array([[3,2,1,3,1,0,0,0]])

'''
punto 1
'''
def gen(pri,T,g):
    cont=1
    for i in g[0]:
        if cont==1:
            cont=cont*pri[0][i]
            j=i
        else:
            cont=cont*T[j][i]
            j=i
            
    return cont


#print(gen(pri,T,g))

'''
punto 2
'''
E=np.array([[0.8,0,0,0.2],[0.05,0.9,0.1,0.1],[0.05,0.1,0.9,0],[0.1,0,0,0.7]])
gt=np.array([[3,2,1,3,1,0,0,0]])
def traduc(pri,T,g,E,gt):
    prob=gen(pri,T,g)
    for i in range(len(g[0])):
        prob=prob*E[gt[0][i]][g[0][i]]

            
    return prob
print(traduc(pri,T,g,E,gt))




