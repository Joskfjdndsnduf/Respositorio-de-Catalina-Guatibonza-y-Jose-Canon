import matplotlib.pyplot as plt
import numpy as np

def calcular_probabilidad(n):
    probabilidad = 1.0
    for i in range(n):
        probabilidad *= (365-i) / 365
    return 1 - probabilidad


n_valores = list(range(1, 81))
probabilidades = [calcular_probabilidad(n) for n in n_valores]
plt.plot(n_valores, 1-np.array(probabilidades))
plt.xlabel('personas')
plt.ylabel('Probabilidad')
plt.show()
