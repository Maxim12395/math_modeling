import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 

t = np.arange(0, 3, 0.01) 

def func(v, t):

    y, omega = v
    
    dy_dt = omega
    
    domega_dt = (1 - omega)**0.5
    return dy_dt, domega_dt

y0 = 1
dy_dt0 = 0
v0 = 

sol = odeint(func, v0, t)  

plt.plot(t, sol[:, 0], "r", label = "dy_dx")
plt.plot(t, sol[:, 0], "k", label = "domega_dx")

plt.legend()
plt.show()  