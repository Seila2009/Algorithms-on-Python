# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Введите 3 числа:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if b < a < c or c < a < b:
    print(f'Среднее: {a}')
elif a < b < c or c < b < a:
    print(f'Среднее: {b}')
else:
    print(f'Среднее: {c}')
