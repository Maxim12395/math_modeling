import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0, 5000, 0.1)

def radio_function(n, t):
     dmdt = k * n
     return dmdt

n_o = 10
k = 1/1200

solve_Bi = odeint(radio_function, n_o, t)
plt.plot(t, solve_Bi[:, 0], label = '')

plt.plot(t, n_o*10*np.ones(len(t)))

plt.show()