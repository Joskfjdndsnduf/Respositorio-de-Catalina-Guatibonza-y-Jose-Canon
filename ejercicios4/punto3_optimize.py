import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as spo

def func(p):
    x, y, z, _lambda = p
    return -1*(f(x, y, z) - _lambda * (x*y + 2*y*z + 2*x*z - 12))

#variables[0]=x, variables[1]=y, varfiables[2]=z

restricciones = ({'type': 'eq', 'fun': lambda variables: variables[1]*variables[0] + 2*variables[1]*variables[2] + 2*variables[0]*variables[2] - 12})

def f(x, y, z):
    return x * y * z

x0 = [1, 1, 1, 0]

mini = spo.minimize(func, x0, constraints=restricciones)

print("Valor máximo:", -mini.fun)
