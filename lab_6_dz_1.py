import numpy as np
import matplotlib as ml
import matplotlib.pyplot as plt

plt.plot([1,5,5],[1,1,5])
plt.plot([1,1,1],[5,5,1])

x =[1,5,5]
y =[5,5,1]
z =[1,1,1]
q =[1,1,5]

plt.plot(x, y, z, q, color='r', label="luchte", marker="o", ms=5)

plt.title("base")
plt.legend()
plt.grid()
plt.axis("equal")

plt.savefig('pic1.png')
