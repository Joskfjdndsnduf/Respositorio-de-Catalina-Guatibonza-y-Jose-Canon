import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0.1,1.1,40)
print(x)

h=0.01
def func(x):
    return np.sqrt(np.tan(x))

def derivadaader(f,h,x):
    return (f(x+h)-f(x))/h

def dercent(f,h,x):
    return (f(x+h)-f(x-h))/2*h

print(func(x))
y=dercent(func,h,x)

plt.plot(x,y)
plt.show()

