import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-1, 1, 0.1) 

def func(z, t):
    
    x, y = t
    
    dx_dt = 3*x - 2*y + ((np.exp**(3*t)) / (np.exp**t) + 1)
    
    dy_dt = x - ((np.exp**(3*t)) / (np.exp**t) + 1)
    
    return dx_dt,dy_dt

x0 = 5
y0 = - 7 

z0 = x0, y0 

sol = odeint(second_diff, z0, x)
plt.plot(x, sol[:, 1], "b", label = "dx_dt")
plt.plot(x, sol[:, 0], "k", label = "dy_dt")
plt.legend()
plt.shpw()
