def changer(a, b):
  a = 2
  b[0] = " Good "

x = 10 
L = [1, 2]

changer(x, L) 

print(x)
print(L)

L = [1, 2]
changer(x, L[:])

print(L)

def my_func(a,b):
  x = 3*a-b
  return x

#print(ma_func())

def my_func(a=1, b=0):
  x = 3*a - b
  return x

print(my_func())

print(my_func(3, 4))

print(my_func(6))

print(my_func(b = 7))

print(my_func(a = 5, b = 6))