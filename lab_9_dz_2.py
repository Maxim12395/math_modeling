import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0, 4 , 0.01)

def radio_function(n, t):
     dmdt = - k * n * t
     return dmdt

n_o = 1000
k = 0.08

solve_Bi = odeint(radio_function, n_o, t)
plt.plot(t, solve_Bi[:, 0], label = '')

#plt.plot(t, n_o*10*np.ones(len(t)))

plt.show()