import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

frames = 200

t = np.linspace(0, 5, frames)

def move_func(z, t):
    
    v, a, dy, dt = z
    
    dy_dt = v
    
    dy_dt = g - M * (dy / dt)
    
    dy_dt = a
    
    return dy_dt

g = 9.8

v0 = 1

m = 0.5

M = 0.2

z0 = g, v0, m, M


fig, ax = plt.subplots()

ball1, = plt.plot([], [], "o", color = "r")


def animate(i):
    ball1.set_data(solve_func(i, "point"))

ani = FuncAnimation(fig,
                    animate,
                    frames = frames,
                    interval = 30)    

edge = 15
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

plt.legend()
plt.show()    