# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

massive = [random.randint(0, 100) for _ in range(10)]
first_min = massive[1]
second_min = massive[0]

for number in massive:
    if number <= first_min:
        second_min = first_min
        first_min = number
    elif number <= second_min:
        second_min = number

print(f'В массиве: \n{massive}\n минимальные элементы: {first_min} и {second_min}')
