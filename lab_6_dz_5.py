import matplotlib.pyplot as plt
import numpy as np


def spiral_plotter(b = 0.04):
    fi = np.arange(0,8*np.pi, 0.01)
    r = np.exp(b*fi)
    x = r*np.sin(fi)
    y = r*np.cos(fi)
    
    plt.plot(x, y)
    plt.axis("equal")
    plt.show()
    
spiral_plotter()

def spiral_plotter(k = 0.05):
    fi = np.arange(0,8*np.pi, 0.01)
    r = np.exp(k*fi)
    x = r*np.sin(fi)
    y = r*np.cos(fi)
    
    plt.plot(x, y)
    plt.axis("equal")
    plt.show()
    
spiral_plotter()

def spiral_plotter(k = 1):
    fi = np.arange(0,8*np.pi, 0.1)
    r = np.exp(k/(fi)**0.5)
    x = r*np.sin(fi)
    y = r*np.cos(fi)
    
    plt.plot(x, y)
    plt.axis("equal")
    plt.show()
    
spiral_plotter()