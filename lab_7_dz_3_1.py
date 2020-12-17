import matplotlib.pyplot as plt
from math import sqrt, cos, sin, pi
import numpy as np

def babochka(e):
    t = np.linspace(-2*np.pi, 6*np.pi, 100)
    # x = (np.sin*(t)*((e**(np.cos*(t))) - 2*np.cos*(4*t) + (np.sin**5)*(t/12)))
    # y = (np.cos*(t)*((e**(np.cos*(t))) - 2*np.cos*(4*t) + (np.sin**5)*(t/12)))
    
    for x in (-5 , 5):
        x = ((np.sin*(t)*(e**(np.cos*(t)))) - (2*np.cos*(4*t)) + ((np.sin**5)*(t/12)))
    for y in (-5 , 5):
        y = (np.cos*(t)*((e**(np.cos*(t))) - 2*np.cos*(4*t) + (np.sin**5)*(t/12)))
    for t in (0 , 12*np.pi):
        t = np.linspace(-2*np.pi, 6*np.pi, 100)
        
        plt.axis("equal")
        plt.plot(x,y)
        plt.show()
    
babochka(5)
