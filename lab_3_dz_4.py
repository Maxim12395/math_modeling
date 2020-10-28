  
import numpy as np
N = 3
M = 4
A = np.ndarray(shape=(N,M))
for i in range(0,N,1):
    for j in range(0,M,1):
        if i > 0 and j > 0:
            A[i,j] = (np.sin(N*i + M*j)) 
            

 
for i in range(N):
    for j in range(M):
        if A[i][j] < 0:
            A[i][j] = 0

    print(A)  
