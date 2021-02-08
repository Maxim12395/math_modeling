from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-5,5,0.01)

def diff_func(v,x):

    y, w =v

    dy_dt = w
    
    dw_dt = np.sin(x) + np.cos(x)
    
    return dy_dt, dw_dt

y0= 3

dy_dt0= 0

v0= y0, dy_dt0

sol=odeint(diff_func,v0,x)
plt.plot(x,sol[:,1],'r',label="dy_dt")
plt.plot(x,sol[:,0],'b',label="dw_dt")
plt.show()
