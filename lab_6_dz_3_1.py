import matplotlib.pyplot as plt
import numpy as np
def circlea_platter(R=1, xa = - 2,xb = 3, dx = 0.02):
    
    x = np.arange(xa, xb, dx)
    y = np.arange(xa, xb, dx)
    
    X, Y = np.meshgrid(x, y)
    fxy = X**2 + Y**2
    plt.contour(X, Y, fxy, levels =[R])
    plt.axis("equal")
    plt.show()
    
circlea_platter(3)

