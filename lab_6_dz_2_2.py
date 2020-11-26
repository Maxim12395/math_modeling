import matplotlib.pyplot as plt
import numpy as np

def giperbola_platter(k = 5,x = 3, xa =-10, xb = 10, dx = 2):
    
    x = np.arange(xa,xb,dx)
    y = k/x
    
    
    plt.plot(x,y,label="my giperbola")
    plt.xlabel("coord - x")
    plt.ylabel("coord - y")
    plt.legend()
    plt.grid()
    plt.show()
    
giperbola_platter()