import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

h_0 = 7007659
R = 6371000
r = np.arange(h_0, R, -1000)

def radio_function(v, r):
    drdt = -((G*m)/(r**2*v))
    return drdt

G = 6.67*10**(-11)
m = 5.97 * 10**24
v_0 = 0.1

solve_Bi = odeint(radio_function, v_0, r )
plt.plot(r, solve_Bi[:, 0], label = '')

#plt.plot(t, n_o*10*np.ones(len(t)))

plt.show()