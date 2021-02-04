import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt	

x = np.arange(0, 2, 0.01) 

def second_diff(z, x):
    
    y, omega = z
    
    dy = omega
    
    domega_dx = - np.sin(y) * omega + 3 * x * y + 5
    
    return dy, domega_dx

y0 = 0.01
omega0 = 0.05

z0 = y0, omega0



sol = odeint(second_diff, z0, x)

plt.plot(x, sol[:, 1], "b", label = "y(x)")
plt.plot(x, sol[:, 0], "r", label = "omega(x)")
plt.legend()
plt.shpw()
