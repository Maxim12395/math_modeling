import matplotlib.animation as FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r', label='Ball')

	
	
def circle_move(R, angle_vel, time):
	
    alpha = angle_vel * (np.pi/180) * time
	
    x = R*np.cos(alpha)
	
    y = R*np.sin(alpha)
	
    return x, y

edge = 3
plt.axis('equal')

ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animation(i):
    ball.set_data(circle_move(R = 2, angle_vel = 1, time = i))
    
plt.legend()
	
ani = FuncAnimation(fig,
                    animation,
                    frames=180,
                    interval=30
                    )
	
	
ani.save('lec_7_no_standart_object.gif')

#ЗАЙТИ ЧЕРЕЗ РЕПЛИТ!!!!!!!!!!!!!!!
