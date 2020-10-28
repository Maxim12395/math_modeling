from math import sin
N = 3
M = 4
mtx = []
for i in range(N):
    a = []
    for j in range(M):
        a.append(sin(N*(i+1) + M*(j+1)))
    mtx.append(a)
 
for i in range(N):
    for j in range(M):
        if mtx[i][j] < 0:
            mtx[i][j] = 0

    print(mtx)