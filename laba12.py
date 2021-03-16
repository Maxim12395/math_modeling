import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 365
seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years*seconds_in_year, frames)

def move_func(s, t):
    (x, vx, y, vy, 
     xm, vxm, ym, vym) = s
    
    dxdt = vx
    dvx_dt = - G * M * x / (x**2 + y**2)**1.5
    dydt = vy
    dvy_dt = - G * M * y / (x**2 + y**2)**1.5
    
    dxmdt = vxm
    dvxm_dt = - G * M * xm / (xm**2 + ym**2)**1.5
    dymdt = vym
    dvym_dt = - G * M * ym / (xm**2 + ym**2)**1.5
    
    return (dxdt, dvx_dt, dydt, dvy_dt,
            dxmdt, dvxm_dt, dymdt, dvym_dt)


G = 6.67 * 10**(-11)
M = 1.98 * 10**(30)

x0 = 149 * 10**9
vx0 = 0
y0 = 0
vy0 = 30000

xm0 = 0
vxm0 = - 24000
ym0 = 228 * 10**(9)
vym0 = 0

s0 = (x0, vx0, y0, vy0, xm0, vxm0, ym0, vym0)

def solve_func(i, key):
    sol = odeint(move_func, s0, t)
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
        xm = sol[i, 4]
        ym = sol[i, 6]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
        xm = sol[:i, 4]
        ym = sol[:i, 6]

    return ((x, y), (xm, ym))

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='b')
ball_line, = plt.plot([], [], '-', color='b')

ballm, = plt.plot([], [], 'o', color='k')
ball_linem, = plt.plot([], [], '-', color='k')
plt.plot([0], [0], 'o', color='y', ms=20)



def animate(i):
    ball.set_data(solve_func(i, 'point')[0])
    ball_line.set_data(solve_func(i, 'line')[0])
    
    ballm.set_data(solve_func(i, 'point')[1])
    ball_linem.set_data(solve_func(i, 'line')[1])
    
ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)
plt.axis('equal')
edge = 2*x0
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.show()
#запустить в repl.it
