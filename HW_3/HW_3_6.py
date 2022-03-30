# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

massive = [random.randint(0, 99) for _ in range(15)]
index_min = 0
index_max = 0
step = 1
amount = 0

for i in massive:
    if massive[index_min] > i:
        index_min = massive.index(i)
    elif massive[index_max] < i:
        index_max = massive.index(i)

if index_max - index_min < 0:
    step = -1

for i in massive[index_min + step:index_max:step]:
    amount += i

print(f'Массив: {massive}.\nСумма элементов между минимальным ({massive[index_min]}) '
      f'и максимальным ({massive[index_max]}) элементами: {amount}')
