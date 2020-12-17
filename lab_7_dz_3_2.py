import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, cos, sin, pi, exp
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], "-", color = "b")
plt.axis("equal")
xdata, ydata = [], []
edge=20
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(t):
    x0 = 0
    y0 = 0
    xdata.append(16*np.sin(t)**3)
    ydata.append(13*np.cos(t)- 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t))
    anim_object.set_data(xdata, ydata)
    return anim_object

ani=FuncAnimation(fig,
                  animate,
                  frames=np.arange(0, 25, 0.1),
                  interval=100 
                  )

ani.save("lab_7_dz_4.gif")
