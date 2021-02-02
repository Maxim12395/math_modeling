import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0, 2*np.pi, 0.1)

def radio_function(w, t):
    dwdt = R**2 *L0 /(4 * q * wq)
    return dwdt

R = 6400000
L0 = 3.827 * 10**26
q = 147 * 10**9
wq = 30400

solve_Bi = odeint(radio_function, wq , t )
plt.plot(t, solve_Bi[:, 0], label = '')

#plt.plot(t, n_o*10*np.ones(len(t)))

plt.show()