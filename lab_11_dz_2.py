import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

frames = 200

t = np.linspace(0, 5, frames)
x = np.ones(len(t))

def move_func(z, t):
    
    y, v = z
    
    dx_dt = k1 * (a0 - x - y)
    
    dy_dt = k2 * (a0 - x - y)
    
    return dx_dt, dy_dt

k1 = 0.5

k2 = 0.3

a0 = 15

z0 = k1, k2

sol = odeint(move_func, z0, t) 


plt.plot(t, sol[:, 0], "b", label = "dy_dt")
plt.plot(t, sol[:, 1], "r", label = "domega_dt")

plt.legend()
plt.show()    