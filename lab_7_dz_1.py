import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


def cicloid(R, t, r):

    x = R*(t-(np.sin**3)*t)
    y = R*(1-(np.cos**3)*t)
    
for theta in np.linspace(-2*np.pi, 2*np.pi, 100):
    x.append(r*(theta - sin(theta))) 
    y.append(r*(1 - cos(theta)))
    plt.plot(x,y) 
    plt.show() 

cicloid(5)