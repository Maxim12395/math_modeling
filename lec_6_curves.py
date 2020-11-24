import matplotlib.pyplot as plt
import numpy as np

def parabola_platter(a=1, b=1, c=0, title="parabola platter"):
    
    x = np.arange(-10,10,0.01)
    y = a*x**2 + b*x + c
    
    plt.plot(x,y,label="my parabola")
    plt.xlabel("coord - x")
    plt.ylabel("coord - y")
    plt.title(title)
    plt.legend()
    plt.savefig('pic1.png')#
    #plt.show()
    
parabola_platter()