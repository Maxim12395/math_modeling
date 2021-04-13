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
     x3,v_x3,y3,v_y3)=s
      
    dxdt1=v_x1
    dv_xdt1=(-G*m2*(x1-x2)/((x1-x2)**2+(y1-y2)**2)**1.5
              -G*m3*(x1-x3)/((x1-x3)**2+(y1-y3)**2)**1.5
              +k*v1*v2/m1*(x1-x2)/((x1-x2)**2+(y1-y2)**2)**1.5
              +k*v1*v3/m1*(x1-x3)/((x1-x3)**2+(y1-y3)**2)**1.5)
     
    dydt1=v_y1
    dv_ydt1=(-G*m2*(y1-y2)/((x1-x2)**2+(y1-y2)**2)**1.5
              -G*m3*(y1-y3)/((x1-x3)**2+(y1-y3)**2)**1.5
              +k*v1*v2/m1*(y1-y2)/((x1-x2)**2+(y1-y2)**2)**1.5
              +k*v1*v3/m1*(y1-y3)/((x1-x3)**2+(y1-y3)**2)**1.5)
    
    dxdt2=v_x2
    dv_xdt2=(-G*m1*(x2-x1)/((x2-x1)**2+(y2-y1)**2)**1.5
              -G*m3*(x2-x3)/((x2-x3)**2+(y2-y3)**2)**1.5
              +k*v2*v1/m1*(x2-x1)/((x2-x1)**2+(y2-y1)**2)**1.5
              +k*v2*v3/m1*(x2-x3)/((x2-x3)**2+(y2-y3)**2)**1.5)
     
    dydt2=v_y2
    dv_ydt2=(-G*m1*(y2-y1)/((x2-x1)**2+(y2-y1)**2)**1.5
              -G*m3*(y2-y3)/((x2-x3)**2+(y2-y3)**2)**1.5
              +k*v2*v1/m1*(y2-y1)/((x2-x1)**2+(y2-y1)**2)**1.5
              +k*v2*v3/m1*(y2-y3)/((x2-x3)**2+(y2-y3)**2)**1.5)
     
    dxdt3=v_x3
    dv_xdt3=(-G*m1*(x3-x1)/((x3-x1)**2+(y3-y1)**2)**1.5
              -G*m3*(x3-x2)/((x3-x2)**2+(y3-y2)**2)**1.5
              +k*v2*v1/m1*(x3-x1)/((x3-x1)**2+(y3-y1)**2)**1.5
              +k*v2*v3/m1*(x3-x2)/((x2-x3)**2+(y2-y3)**2)**1.5)
     
    dydt3=v_y3
    dv_ydt3=(-G*m1*(y3-y1)/((x3-x1)**2+(y3-y1)**2)**1.5
              -G*m3*(y3-y2)/((x3-x2)**2+(y3-y2)**2)**1.5
              +k*v2*v1/m1*(y3-y1)/((x3-x1)**2+(y3-y1)**2)**1.5
              +k*v2*v3/m1*(y3-y2)/((x2-x3)**2+(y2-y3)**2)**1.5)
    
    return (dxdt1,dv_xdt1,dydt1,dv_ydt1,
            dxdt2,dv_xdt2,dydt2,dv_ydt2,
            dxdt3,dv_xdt3,dydt3,dv_ydt3)

G=6.67*10**(-11)
k = 8.98755*10**9

v1x= 
v1y= 

v2x= 
v2y= 

v3x= 
v3y= 

v4y= 
v4x=

x10= 0
v_x10=100
y10=0
v_y10=0
    
x20=100
v_x20=0
y20=0
v_y20=0
    
x30=-100
v_x30=0
y30=0
v_y30=0
    
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