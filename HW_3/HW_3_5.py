# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

numb_massive = [random.randint(-100, 100) for _ in range(10)]
max_index = 0

for i in numb_massive:
    if numb_massive[max_index] > i:
        max_index = numb_massive.index(i)

if numb_massive[max_index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'В массиве{numb_massive} максимально отрицательный элемент: {numb_massive[max_index]}. '
          f'Находится в массиве на позиции {max_index}')
