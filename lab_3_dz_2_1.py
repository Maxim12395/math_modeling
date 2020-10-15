import numpy as np

h = 100
a = 3.14/3
B = np.pi/6
g = 9.8
cos = 0.9
tan = 6.4


U = np.sqrt((g*h*np.tan(B)**2)/(2*(np.cos(a)**2)*(1-np.tan(B)*np.tan(a))))

print(U)