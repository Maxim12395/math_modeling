import numpy as np	
import matplotlib.pyplot as plt	
from mpl_toolkits.mplot3d import Axes3D

# определение трехмерного пространства

fig = plt.figure()

ax = fig.gca(projection='3d')

# определение параметров кривоцй
t = np.arange(0.01, 4*np.pi, 0.01) #это параметры
R = 1

#параметрическое задание пространственной кривой
x = R*np.cos(t)
y = R*t**0.5
z = R*np.log10(t)

#построение пространственной кривой
ax.plot(x, y, z, label='dich')
ax.legend()

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('3D test')
#начало стрелки
arrow_x0 = 0
arrow_y0 = 0
arrow_z0 = 0
#конец стрелки
arrow_x1 = 1
arrow_y1 = 1
arrow_z1 = 1

#
ax.quiver(arrow_x0,arrow_x0,arrow_x0,
          arrow_x1,arrow_x1,arrow_x1,
          length = 1, normalize = True, color = 'r')

plt.show()