import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

frames = 200

t = np.linspace(0, 5, frames)
x = np.ones(len(t))

def move_func(z, t):
    
    y, v = z
    
    dy_dt = v
    
    dv_dt = - g - M * v
    
    return dy_dt, dv_dt

g = 9.8

v0 = 20

m = 0.5

M = 0.2

y0 = 0

z0 = y0, v0

def solve_func(i, key):
    
    sol = odeint(move_func, z0, t)  
    
    if key == "point":
        
        y = sol[i, 0]
    else:
       
        y = sol[:i, 0]
    return y

fig, ax = plt.subplots()

ball, = plt.plot([], [], "o", color = "r")
ball_line, = plt.plot([], [], "-", color = "r")

def animate(i):
    ball.set_data(x,solve_func(i, "point"))

    
ani = FuncAnimation(fig,
                    animate,
                    frames = frames,
                    interval = 30)    

edge = 50
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

ani.save("laba.gif")
