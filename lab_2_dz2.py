a=float(input('первый член: '))
b=int(input('количество членов: '))
c=float(input('знаменатель '))

for a in range(1,b,1):
    print(a*c**a, end='')