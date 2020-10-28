import numpy as np
N = 5
M = 8
A = np.ndarray(shape=(N,M))
for i in range(0,N,1):
    for j in range(0,M,1):
        if i > 0 and j > 0:
            A[i,j] = (np.sin(N*i + M*j)) 
            
c = int(input("Первый столбец: ")) - 1
d = int(input("Второф столбец: ")) - 1

for i in range(N):
    A[i][c], A[i][d] = A[i][d], A[i][c]
    
    print(A[i])
    
    
    
# from random import random
# A = 10
# B = 5
# a = []
# for i in range(A):
#     b = []
#     for j in range(B):
#         b.append(round(random()*2))
#     a.append(b)
#     print(b)
 
# c1 = int(input("Первый столбец: ")) - 1
# c2 = int(input("Второф столбец: ")) - 1

# for i in range(A):
#     a[i][c1], a[i][c2] = a[i][c2], a[i][c1]
#     print(a[i])
