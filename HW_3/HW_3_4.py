# 4. Определить, какое число в массиве встречается чаще всего.
import random

numb_mass = [random.randint(0, 99) for _ in range(20)]
max_num = 0

for i in numb_mass:
    if numb_mass.count(max_num) < numb_mass.count(i):
        max_num = numb_mass.index(i)

print(f'В массиве{numb_mass},\nчисло {numb_mass[max_num]}, встречается {numb_mass.count(max_num)} раз(а).')
