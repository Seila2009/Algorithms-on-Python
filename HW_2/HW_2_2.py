# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = input('Введите целое положительное число: ')
even_num = 0
odd_num = 0

for f in number:
    if int(f) % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
print(f'В числе {number}: {even_num} - четные числа, {odd_num} - нечетные.')