import numpy as np 
import matplotlib.pyplot as plt

from matplotlib.animation import FancAnimation

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], "-", lw=2)

xdata, ydata = [], []

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1)

def updata (frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    anim_odject.set_data(xdata, ydata)
    return anim_object,

ani = FancAnimation