import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

frames = 200

t = np.linspace(0, 5, frames)

def move_func(z, t):
    
    y, v = z
    
    dy_dt = v
    
    dx_dt = g * (x / l) - mu * g * (l * x / l)
    
    return dy_dt, dx_dt

g = 9.8

l = 2.5

mu = 1

x = 0.5

y0 = 0

z0 = x, y0

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