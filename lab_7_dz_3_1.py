import matplotlib.pyplot as plt
from math import sqrt, cos, sin, pi
import numpy as np

def babochka(e):
    
    t = np.linspace(-2*np.pi, 6*np.pi, 100)
    x = (np.sin*(t)*((e**(np.cos*(t))) - 2*np.cos*(4*t) + (np.sin**5)*(t/12)))
    y = (np.cos*(t)*((e**(np.cos*(t))) - 2*np.cos*(4*t) + (np.sin**5)*(t/12)))
    
    
    plt.axis("equal")
    plt.plot(y)
    plt.show()
    
babochka(3)