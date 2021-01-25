import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0 , 100, 0.01)

def radio_function(v, t):
    dvdt = (F - y*v**2)/m
    return dvdt

v_0 = 0
m = 100
F = 100
y = 0.05

solve_Bi = odeint(radio_function, v_0, t)
plt.plot(t, solve_Bi[:, 0], label = '')
plt.show()