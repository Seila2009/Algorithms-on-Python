# 3.По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

print('Введите координаты прямой: ')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

k = (y2 - y1) / (x2 - x1)
b = y1 - k * x1

print(f'Уравнение прямой y = {k}x + {b}')
