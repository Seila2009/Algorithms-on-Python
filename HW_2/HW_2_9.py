# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def sum_numb(number):
    sum = 0
    for f in number:
        sum += int(f)
    return sum


sequence = [i for i in input('Введите через пробел последовательность натуральных чисел: ').split()]

max_numb = 0
max_sum = 0

for i in sequence:
    if sum_numb(i) > max_sum:
        max_numb = i
        max_sum = sum_numb(i)

print(f'{max_numb} - наибольшее число по сумме цифр. {max_sum} - сумма цифр наибольшего числа ')
