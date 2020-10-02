a1=float(input('первый член: '))
b=float(input('знаменатель: '))
c=int(input('количество членов: '))

for a in range(1,c,1):
    print(a1*b**(a), end='    ')
