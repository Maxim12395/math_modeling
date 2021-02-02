import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(6, 18, 0.01)

def radio_function(S0, t):
    dsdt = E0 * S * ((np.cos((np.pi/12) * (t - 12)) * K * ((S/np.pi)**0.5)))
    return dsdt

S0 = 1600
K = 300*10**(-8)
E0 = 1367

solve_Bi = odeint(radio_function, S0 , t )
plt.plot(t, solve_Bi[:, 0], label = '')

#plt.plot(t, n_o*10*np.ones(len(t)))

plt.show()