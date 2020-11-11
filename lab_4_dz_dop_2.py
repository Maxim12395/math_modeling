fib1 = 0    
fib2 = 1

n = input("Номер элемента ряда Фибоначчи: ")
n = int(n)

i = 0

while i < n - 2:
    
    fib_summa = fib1 + fib2
    
    fib1 = fib2
    
    fib2 = fib_summa
    
    i = i + 1

print(fib2)