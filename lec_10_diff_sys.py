import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt	
# Определяем переменную величину
	
t = np.arange(0, 10, 0.01) 
	
# Определяем функцию для системы диф. уравнений
	
def diff_func(z, t): # z - изменяемая величина для системы
	
    theta, omega = z # Указание изменяемых функций, через z	
    
    # Первое уравнение системы
    dtheta_dt = omega 
    
    # Второе уравнение системы
    domega_dt = - b * omega - c * np.sin(theta) 
	
    return dtheta_dt, domega_dt

# Определяем начальные значения и параметры,
# входящие в систему диф. уравнений

theta0 = np.pi - 0.1
omega0 = 0


z0 = theta0, omega0

b = 0.25
c = 5.0 


sol = odeint(diff_func, z0, t)

plt.plot(t, sol[:, 1], "k", label = "theta")

plt.legend()
plt.shpw()
