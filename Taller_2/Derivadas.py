import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(1,3,2000)
y=np.pi*((0.25/2)**2)*0.05*np.cos(3.5*x)*np.cos(2*np.pi*1000*x)

print(y)

plt.plot(x,y)
plt.show()

