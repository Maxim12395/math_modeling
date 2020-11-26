import matplotlib.pyplot as plt
import numpy as np


def parabola_platter(a  = 1, b = 2, c = 5, xa =-10, xb = 10):
    
    x = np.arange(xa,xb,1)
    y = a*x**2 + b*x + c
    

    plt.plot(x,y,label="my parabola")
    plt.xlabel("coord - x")
    plt.ylabel("coord - y")
    plt.legend()
    plt.savefig('pic1.png')
    #plt.show()
    
parabola_platter(1,2,3)


