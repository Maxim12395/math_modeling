import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

frames = 200

t = np.linspace(0, 5, frames)

def move_func(z, t):
    
    y, v, omega = z
    
    dy_dt = v
    
    dv_dt = g - (k) * y - 0.8*v + (5*(np.cos(omega*t)))
    
    return dy_dt, dv_dt

omega0 = 10

t = 5

g = 9.8

m = 0.5

y0 = 0.8

dl = 0.08

F0 = 1

v0 = 0.5

k = 12.5

z0 = y0, v0

def solve_func(i, key):
    
    sol = odeint(move_func, z0, t)  
    
    if key == "point":
        x = np.ones(len(t))
        y = sol[i, 0]

    return x, y

fig, ax = plt.subplots()

ball, = plt.plot([], [], "o", color ="r")

def animate(i):
    ball.set_data(solve_func(i, "point"))
    
ani = FuncAnimation(fig,
                    animate,
                    frames = frames,
                    interval = 30)    

edge = 2
ax.set_xlim(0, edge)
ax.set_ylim(0, 1)

ani.save("laba.gif")    
