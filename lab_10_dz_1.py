import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01) 

def func(z, x):
    
    y , x  = z
    
    dy_dx = (y**2) * z
    
    dz_dx = (z/x) - y * (z**2)
    
    return dy_dx , dz_dx

y0 = 1
z0 = - 3

x0 = y0, z0

sol = odeint(func, z0, x)  

plt.plot(x, sol[:, 1], "b", label = "y(x)")

plt.legend()
plt.shpw()    