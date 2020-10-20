from random import random
A = 10
B = 5
a = []
for i in range(A):
    b = []
    for j in range(B):
        b.append(round(random()*2))
    a.append(b)
    print(b)
 
c1 = int(input("Первый столбец: ")) - 1
c2 = int(input("Второф столбец: ")) - 1

for i in range(A):
    a[i][c1], a[i][c2] = a[i][c2], a[i][c1]
    print(a[i])
