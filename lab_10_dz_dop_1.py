import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-1, 1, 0.01) 

def func(v, t):
    
    y , z, x  = v
    
    dy_dt = x + y + z
    
    dz_dt = 4*x - y + 4*z
    
    dx_dt = 3*x - y + z
    
    return dy_dt , dz_dt, dx_dt

y0 = 1
z0 = - 3
x0 = -71

v0 = y0, z0, x0

sol = odeint(func, v0, x)  

plt.plot(x, sol[:, 1], "b", label = "dy_dt")
plt.plot(x, sol[:, 0], "b", label = "dz_dt")
plt.plot(x, sol[:, 2], "b", label = "dx_dt")

plt.legend()
plt.shpw()    