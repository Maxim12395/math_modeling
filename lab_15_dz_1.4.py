import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np	
import matplotlib.pyplot as plt	

fig = plt.figure()
ax = p3.Axes3D(fig)

phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, 2 * np.pi, 100)
l = 2
f = 3
m = 4
n = 5

x =np.outer(phi, np.cos(theta)) + (l, f(theta))
y =np.outer(phi, np.sin(theta)) + (m, f(theta))
z =np.outer(n, f(theta), (np.size(theta)))

ax.plot_surface(x, y, z, color='b')
plt.show()