import numpy as np

np.pi = 3.14
g = 10
U0x = 10
alpha = np.pi/6
x0 = 5
y0 = 8
t = np.arange(0,65,0.1)

x = x0 + U0x*t
y = y0 + U0x*t - ((g*t**2)/(2))

print(x)
print(y)

traj = np.ndarray(shape = (len(t),3))
for i in range(len(t)):
    traj[i,0] = t[i]
    traj[i,1] = x[i]
    traj[i,2] = y[i]
    
    
print(traj)