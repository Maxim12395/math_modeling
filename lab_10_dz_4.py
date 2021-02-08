import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01) 

def diff_func(v, t):
    
    y , omega  = v
    
    dy_dt = omega
    
    domega_dt = -4*omega + 5*y
    
    return dy_dt , domega_dt

y0 = 4
dy_dt = - 1


v0 = y0, dy_dt

sol = odeint(diff_func, v0, x)  

plt.plot(x, sol[:, 0], "b", label = "dy_dt")
plt.plot(x, sol[:, 1], "r", label = "domega_dt")

plt.legend()
plt.shpw()    