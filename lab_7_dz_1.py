import matplotlib.pyplot as plt
from math import sqrt, cos, sin
import numpy as np

def cicloid(r):
  x = []
  y = []
  for t in np.linspace(-2*np.pi, 2*np.pi, 100):
    x.append(r*(t - sin(t)))
    y.append(r*(1 - cos(t))) 
    plt.plot(x,y) 
    plt.show()  

cicloid(10)
