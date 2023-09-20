import numpy as np
import matplotlib.pyplot as plt

t=np.linescape(0,10,20)
def posicion (A,k,t,m):
    omega = np.sqrt(k/m)
    return A*np.sin(omega*t)
 
