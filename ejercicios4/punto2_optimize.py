import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as spo

def func(p):
    x, y, z, _lambda = p
    return f(x, y, z) - _lambda * (2*x - 4*y + 5*z - 2)

restricciones = ({'type': 'eq', 'fun': lambda variables: 2*variables[0] -4*variables[1] + 5*variables[2] - 2})

def f(x, y, z):
    return x**2 + y**2 + z**2 -2*z + 1

x0 = [0, 0, 0, 0]

mini = spo.minimize(func, x0, constraints=restricciones)

print("Valor mínimo:", mini.fun)
