# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

first_massive = [random.randint(0, 100) for _ in range(10)]
print(f'Массив до изменений: {first_massive}')

max = first_massive[0]
min = first_massive[0]

for i in first_massive:
    if i > max:
        max = i
    elif i < min:
        min = i
min_index = first_massive.index(min)
max_index = first_massive.index(max)

first_massive[min_index], first_massive[max_index] = first_massive[max_index], first_massive[min_index]
print(f'Массив после изменений: {first_massive}')
