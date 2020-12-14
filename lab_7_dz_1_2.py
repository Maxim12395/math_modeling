import matplotlib.pyplot as plt
import numpy as np


def astroid(r):
    x=[]
    y=[]
    for t in range (1,1000):
        x.append((r*np.sin(t))**3)
        y.append((r*np.cos(t))**3)

    plt.scatter(x,y)
    plt.show()
    
astroid(3)