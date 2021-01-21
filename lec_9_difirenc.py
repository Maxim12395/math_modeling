import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# пределы изменения переменной велечиной 
# в данной задаче переменной велечиной является время 

t = np.arange (0, 10**6, 100)

# запись диф. уравнение  в виде функции
def radio_function(m, t):  # на перевом изменяеиую на втором переменную
    dmdt = - k * m # название можно любое не dmdt
    
    return dmdt

# определить начальные условия и пораметпы

m_o = 10
k = 1.61*10**(-6) # постоянная распада для висмута 210

# решение диф. уравнени функции odeint
solve_Bi = odeint(radio_function, m_o, t)

# построение решения в виде графика функции
plt.plot(t, solve_Bi[:, 0], label = 'распад Висмута 210')

plt.show()