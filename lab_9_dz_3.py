import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0, 10, 0.01)

def radio_function(v, t):
    dvdt = (-Y/m)*v**2 + a_0
    return dvdt

v_0 = 0
#v_0 = 5
m = 5
a_0 = 1
Y = 0.5

solve_Bi = odeint(radio_function, v_0, t)
plt.plot(t, solve_Bi[:, 0], label = '')

#plt.plot(t, n_o*10*np.ones(len(t)))

plt.show()
