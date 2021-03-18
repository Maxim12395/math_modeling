import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 1000
seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, 100, frames)

def move_func(s, t):
    (x, vx, y, vy, 
     xm, vxm, ym, vym,
     xn, vxn, yn, vyn,
     xr, vxr, yr, vyr,) = s
    
    dxdt = vx
    dvx_dt = (k * q1 * q) / (m*(x**2 + y**2)**1.5)
    dydt = vy
    dvy_dt = (k * q1 * q) / (m*(x**2 + y**2)**1.5)
    
    dxmdt = vxm
    dvxm_dt = (k * q2 * q) / (m*(x**2 + y**2)**1.5)
    dymdt = vym
    dvym_dt = (k * q2 * q) / (m*(x**2 + y**2)**1.5)
    
    dxndt = vxn
    dvxn_dt = (k * q3 * q) / (m*(x**2 + y**2)**1.5)
    dyndt = vyn
    dvyn_dt = (k * q3 * q) / (m*(x**2 + y**2)**1.5)
    
    dxrdt = vxr
    dvxr_dt = (k * q4 * q) / (m*(x**2 + y**2)**1.5)
    dyrdt = vyr
    dvyr_dt = (k * q4 * q) / (m*(x**2 + y**2)**1.5)
    
    return (dxdt, dvx_dt, dydt, dvy_dt,
            dxmdt, dvxm_dt, dymdt, dvym_dt,
            dxndt, dvxn_dt, dyndt, dvyn_dt,
            dxrdt, dvxr_dt, dyrdt, dvyr_dt)


k = 9 * 10 ** 9

q = 100

q1 = 1
q2 = -1
q3 = -1
q4 = 1

m = 1 * 10**9

x0 = - 40
vx0 = 1
y0 = 20
vy0 = 0

xm0 = -40
vxm0 = 1
ym0 = -20
vym0 = 0

xn0 = -40
vxn0 = 1
yn0 = -40 
vyn0 = 0

xr0 = -40
vxr0 = 1
yr0 = 40
vyr0 = 0

s0 = (x0, vx0, y0, vy0, xm0, vxm0, ym0, vym0, xn0, vxn0, yn0, vyn0, xr0, vxr0, yr0, vyr0)

def solve_func(i, key):
    sol = odeint(move_func, s0, t)
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
        xm = sol[i, 4]
        ym = sol[i, 6]

        xn = sol[i, 8]
        yn = sol[i, 10]

        xr = sol[i, 12]
        yr = sol[i, 14]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
        xm = sol[:i, 4]
        ym = sol[:i, 6]

        xn = sol[:i, 8]
        yn = sol[:i, 10]

        xr = sol[:i, 12]
        yr = sol[:i, 14]

    return ((x, y), (xm, ym),(xn, yn), (xr, yr))

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='b')
ball_line, = plt.plot([], [], '-', color='b')

ballm, = plt.plot([], [], 'o', color='k')
ball_linem, = plt.plot([], [], '-', color='k')

balln, = plt.plot([], [], 'o', color='k')
ball_linen, = plt.plot([], [], '-', color='k')

ballr, = plt.plot([], [], 'o', color='k')
ball_liner, = plt.plot([], [], '-', color='k')

plt.plot([0], [0], 'o', color='y', ms=20)



def animate(i):
    ball.set_data(solve_func(i, 'point')[0])
    ball_line.set_data(solve_func(i, 'line')[0])
    
    ballm.set_data(solve_func(i, 'point')[1])
    ball_linem.set_data(solve_func(i, 'line')[1])
    
    balln.set_data(solve_func(i, 'point')[2])
    ball_linen.set_data(solve_func(i, 'line')[2])
    
    ballr.set_data(solve_func(i, 'point')[3])
    ball_liner.set_data(solve_func(i, 'line')[3])
    
ani = FuncAnimation(fig,
                    animate,
                    frames=500,
                    interval=30)

plt.axis('equal')
edge = 2*50
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('earth_sun.gif')
