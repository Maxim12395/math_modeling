import numpy as np
index = int(input('Выбери: круг - 1, прямоугольник - 11, треугольник - 111 : '))

def mult_func(index=1):
    if index==1:
        r= float(input('Радиус = '))
        s=np.pi*r**2
        print('Площадь круга = ', s)
    elif index==11:
            a= float(input('Длина = '))
            b= float(input('Ширина = '))
            s=a*b
            print('Площадь прямоугольника = ', s)
    elif index==111:
        a= float(input('Сторона треугольника = '))
        h= float(input('Высота ='))
        
        s=0.5*(a*h)
        print('Площадь треугольника =', s)
    else:
        print('Ошибка')

mult_func(index)