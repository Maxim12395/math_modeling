n = int(input('введите натуральное число: '))
while n > 1:
    a = 2
    b = 0
    while 1:
        if n%a == 0:
            n = n // a
            print(a, end=' ')
            b = 1
            break
        else:
            a += 1
    if b == 1:
        continue
print( )
