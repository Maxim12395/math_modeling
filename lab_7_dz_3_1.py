import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, cos, sin, pi, exp
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], "-", color = "b")
plt.axis("equal")
xdata, ydata = [], []
edge=10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(t):
    x0 = 0
    y0 = 0
    xdata.append(x0 + np.sin(t)*(exp(np.cos(t)) - 2*np.cos(4*t) + np.sin(t/12)**5))
    ydata.append(y0 + np.cos(t)*(exp(np.cos(t)) - 2*np.cos(4*t) + np.sin(t/12)**5))
    anim_object.set_data(xdata, ydata)
    return anim_object

ani=FuncAnimation(fig,
                  animate,
                  frames=np.arange(0,25, 0.1),
                  interval=100 
                  )

ani.save("lab_7_dz_3.gif")
