x0 = 10 #глобальная переменная 
def move(t):
  x = x0*t #локальная переменная
  return x

print(move(3))

x = " Good "
def my_func():
  x = " Bad "
  print(x)

my_func()

print(x)