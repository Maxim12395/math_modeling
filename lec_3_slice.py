import numpy as np
A = np.array([[1,2,3],[4,5,6]])
print(A[1, :])# 0:длина:строка

print(A[:, 1])

B = A[:, ::-1] #[start:stop:step] по умолчанию
               # start =0
               # stop = len(строка, цели, столбцы)
print(B)

