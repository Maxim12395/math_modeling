import matplotlib.pyplot as plt

plt.plot([1,2,3],[5,7,10])
plt.savefig('pic1.png')
plt.show()

x = [3,4,5]
y = [40,10,30]

plt.plot(x,y,color='g', label="luchte", marker=">", ms=5)

plt.xlabel("coord: x")
plt.ylabel("coord: y")
plt.title("base")
plt.legend()
plt.grid()
plt.savefig('pic1.png')#открыть в браузере
#plt.show()

