import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,2,3],[5,7,10])
plt.savefig('pic1.png')

x = [1,5,1]
y = [1,1,1]


plt.plot(x,y,color='g', label="luchte", marker="o", ms=5)

plt.xlabel("coord: x")
plt.ylabel("coord: y")
plt.title("base")
plt.legend()
plt.grid()
plt.savefig('pic1.png')