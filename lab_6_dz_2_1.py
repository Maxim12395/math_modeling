import matplotlib.pyplot as plt
import numpy as np

def parabola_platter(a  = 1, b = 2, c = 5, title="parabola platter"):
    
    xa = np.arange(int(input("введите число: ")))
    xb = np.arange(int(input("введите число: ")))
    y = a*(xa.xb)**2 + b*(xa.xb) + c

    plt.plot(xa,xb,y,label="my parabola")
    plt.xalabel("coord - xa")
    plt.xblabel("coord - xb")
    plt.title(title)
    plt.legend()
    plt.savefig('pic1.png')
    #plt.show()
    
parabola_platter()