import numpy as np	
from scipy.integrate import odeint	
import matplotlib.pyplot as plt	
from matplotlib.animation import FuncAnimation	

seconds_in_year = 365 * 24 * 60 * 60	
frames= 1000
years = 2
t = np.linspace(0, years*seconds_in_year, frames)

def move_func(s,t):
    (x1,v_x1,y1,v_y1,
     x2,v_x2,y2,v_y2,
     x3,v_x3,y3,v_y3,
     x4,v_x4,y4,v_y4)=s
      
    dxdt1=v_x1
    dv_xdt1=(-G*m2*(x1-x2)/((x1-x2)**2+(y1-y2)**2)**1.5
              -G*m3*(x1-x3)/((x1-x3)**2+(y1-y3)**2)**1.5
              +k*q1*q2/m1*(x1-x2)/((x1-x2)**2+(y1-y2)**2)**1.5
              +k*q1*q3/m1*(x1-x3)/((x1-x3)**2+(y1-y3)**2)**1.5)
     
    dydt1=v_y1
    dv_ydt1=(-G*m2*(y1-y2)/((x1-x2)**2+(y1-y2)**2)**1.5
              -G*m3*(y1-y3)/((x1-x3)**2+(y1-y3)**2)**1.5
              +k*q1*q2/m1*(y1-y2)/((x1-x2)**2+(y1-y2)**2)**1.5
              +k*q1*q3/m1*(y1-y3)/((x1-x3)**2+(y1-y3)**2)**1.5)
    
    dxdt2=v_x2
    dv_xdt2=(-G*m1*(x2-x1)/((x2-x1)**2+(y2-y1)**2)**1.5
              -G*m3*(x2-x3)/((x2-x3)**2+(y2-y3)**2)**1.5
              +k*q2*q1/m1*(x2-x1)/((x2-x1)**2+(y2-y1)**2)**1.5
              +k*q2*q3/m1*(x2-x3)/((x2-x3)**2+(y2-y3)**2)**1.5)
     
    dydt2=v_y2
    dv_ydt2=(-G*m1*(y2-y1)/((x2-x1)**2+(y2-y1)**2)**1.5
              -G*m3*(y2-y3)/((x2-x3)**2+(y2-y3)**2)**1.5
              +k*q2*q1/m1*(y2-y1)/((x2-x1)**2+(y2-y1)**2)**1.5
              +k*q2*q3/m1*(y2-y3)/((x2-x3)**2+(y2-y3)**2)**1.5)
     
    dxdt3=v_x3
    dv_xdt3=(-G*m1*(x3-x1)/((x3-x1)**2+(y3-y1)**2)**1.5
              -G*m3*(x3-x2)/((x3-x2)**2+(y3-y2)**2)**1.5
              +k*q2*q1/m1*(x3-x1)/((x3-x1)**2+(y3-y1)**2)**1.5
              +k*q2*q3/m1*(x3-x2)/((x2-x3)**2+(y2-y3)**2)**1.5)
     
    dydt3=v_y3
    dv_ydt3=(-G*m1*(y3-y1)/((x3-x1)**2+(y3-y1)**2)**1.5
              -G*m3*(y3-y2)/((x3-x2)**2+(y3-y2)**2)**1.5
              +k*q2*q1/m1*(y3-y1)/((x3-x1)**2+(y3-y1)**2)**1.5
              +k*q2*q3/m1*(y3-y2)/((x2-x3)**2+(y2-y3)**2)**1.5)
    
    dxdt4=v_x4
    dv_xdt4=(-G*m1*(x4-x1)/((x4-x1)**2+(y4-y1)**2)**1.5
              -G*m3*(x4-x2)/((x4-x2)**2+(y4-y2)**2)**1.5
              +k*q2*q1/m1*(x4-x1)/((x4-x1)**2+(y4-y1)**2)**1.5
              +k*q2*q4/m1*(x4-x2)/((x2-x4)**2+(y2-y4)**2)**1.5)
     
    dydt4=v_y4
    dv_ydt4=(-G*m1*(y4-y1)/((x4-x1)**2+(y4-y1)**2)**1.5
              -G*m4*(y4-y2)/((x4-x2)**2+(y4-y2)**2)**1.5
              +k*q2*q1/m1*(y4-y1)/((x4-x1)**2+(y4-y1)**2)**1.5
              +k*q2*q4/m1*(y4-y2)/((x4-x3)**2+(y2-y4)**2)**1.5)
    
    
    return (dxdt1,dv_xdt1,dydt1,dv_ydt1,
            dxdt2,dv_xdt2,dydt2,dv_ydt2,
            dxdt3,dv_xdt3,dydt3,dv_ydt3,
            dxdt4,dv_xdt4,dydt4,dv_ydt4)

G=6.67*10**(-11)
k = 8.98755*10**9

f = np.pi / 4
vx = f * np.cos
np.cos = vx / f

v1x= vx*np.cos*f
v1y= vx*np.sin*f
q1 = 1.1 * 10**(-11)
m1 = 1.1 * 10**(-27)

v2x= -vx*np.cos*f
v2y= -vx*np.sin*f
q2 = 1.1 * 10**(-11)
m2 = 1.1 * 10**(-27)

v3x= vx*np.cos*f
v3y= -vx*np.sin*f
q3 = 1.1 * 10**(-11)
m3 = 1.1 * 10**(-27)

v4y= vx*np.cos*f
v4x= vx*np.sin*f
q4 = 1.1 * 10**(-11)
m4 = 1.1 * 10**(-27)

a = 0.008

x10= a
v_x10= 100
y10=a
v_y10=0
    
x20=-a
v_x20=0
y20=a
v_y20=0
    
x30=-a
v_x30=0
y30=-a
v_y30=0

x40=a
v_x40=0
y40=-a
v_y40=0
    
s0=(x10,v_x10,y10,v_y10,
    x20,v_x20,y20,v_y20,
    x30,v_x30,y30,v_y30)


def solve_func(i, key):
    sol = odeint(move_func, s0, t)
    if key == 'point':
        x1 = sol[i, 0]
        y1 = sol[i, 2]
        x2 = sol[i, 4]
        y2 = sol[i, 6]
        x3 = sol[i, 8]
        y3 = sol[i, 10]
    else:
        x1 = sol[i, 0]
        y1 = sol[i, 2]
        x2 = sol[i, 4]
        y2 = sol[i, 6]
        x3 = sol[i, 8]
        y3 = sol[i, 10]
    return ((x1, y1), (x2, y2), (x3, y3))
fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='b')
ball_line, = plt.plot([], [], '-', color='b')

ballm, = plt.plot([], [], 'o', color='b')
ball_linem, = plt.plot([], [], '-', color='b')

ballz, = plt.plot([], [], 'o', color='b')
ball_linez, = plt.plot([], [], '-', color='b')

def animate(i):
    ball.set_data(solve_func(i, 'point')[0])
    ball_line.set_data(solve_func(i, 'line')[0])

    ballm.set_data(solve_func(i, 'point')[1])
    ball_linem.set_data(solve_func(i, 'line')[1])

    ballz.set_data(solve_func(i, 'point')[2])
    ball_linez.set_data(solve_func(i, 'line')[2])
    
ani = FuncAnimation(fig,
                    animate,
                    frames=1000,
                    interval=30)  

plt.axis('equal')
edge = 150
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.show()
