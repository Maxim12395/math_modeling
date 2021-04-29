import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np	
import matplotlib.pyplot as plt	

fig = plt.figure()
ax = p3.Axes3D(fig)

phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, 2 * np.pi, 100)
h = 1

x =np.outer(phi, np.cos(theta))
y =np.outer(phi, np.sin(theta))
z =np.outer(h*(np.sinh(phi)), np.sinh(theta))

ax.plot_surface(x, y, z, color='b')
plt.show()