import matplotlib.pyplot as plt
import numpy as np

def lesenka_platter(N=1):

    x = np.arange(0, 37, 0.1)
    y = []

    for i in range(len(x)):
        y.append(x[i]//1)
    plt.plot(x,y)
    print(x)
    print(y)

    plt.show()
lesenka_platter()