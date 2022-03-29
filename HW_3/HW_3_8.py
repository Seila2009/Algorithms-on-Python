# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = []

for i in range(4):
    matrix.append([])
    amount = 0
    for n in range(4):
        user_number = int(input(f'Введите {i+1} и {n+1} элементы столбца: '))
        amount += user_number
        matrix[i].append(user_number)

    matrix[i].append(amount)

for a in matrix:
    print(('{:>4d}' * 5).format(*a))