import matplotlib.pyplot as plt
import numpy as np
def circlea_platter(R=1, title="circlea platter"):
    
    x = np.arange(-2.0, 2.0, 0.1)
    y = np.arange(-2.0, 2.0, 0.1)
    
    X, Y = np.meshgrid(x, y)
    fxy = X**2 + Y**2
    plt.contour(X, Y, fxy, levels =[R])
    plt.axis("equal")
    plt.savefig('pic1.png')
    
circlea_platter(3)
    