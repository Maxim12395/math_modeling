a = int(input('введите делимое: '))
b = int(input('введите делитель: '))

if b!=0 and a%b==0:
    print('делимое= ', a, 'делитель= ', b, 'a делится на b','частное= ', a/b)

elif b!=0:
    print('делимое= ', a, 'делитель= ', b, 'a делится на b','частное= ', a/b, 'остаток= ', a%b)

else:
    print('на 0 не делится')