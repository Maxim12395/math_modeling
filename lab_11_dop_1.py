import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

frames = 200

t = np.linspace(0, 5, frames)

def move_func(z, t):
    
    a, b, c = z
    
    da_dt = - k1 * a
    
    db_dt = k1 * a - k2 * b
    
    dc_dt = k2 * b - k3 * c
    
    return da_dt, db_dt, dc_dt

k1 = 0.5

k2 = 0.3

k3 = 0.2

a0 = 15

A0 = 0

b0 = 0

c0 = 0

z0 = a0, b0, c0

sol = odeint(move_func, z0, t) 


plt.plot(t, sol[:, 0], "b", label = "da_dt")
plt.plot(t, sol[:, 1], "r", label = "db_dt")
plt.plot(t, sol[:, 2], "k", label = "dc_dt")

plt.legend()
plt.show()
