# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

import random

comp_number = random.randint(1, 100)

user_number = None
count = 0
max_count = 3

while comp_number != user_number:
    count += 1
    if count > max_count:
        print('Вы проиграли.')
        break
    print(f'Попытка №{count}')
    user_number = int(input('Введите число от 1 до 100: '))
    if comp_number < user_number:
        print('Ваше число больше загаданного.')
    elif comp_number > user_number:
        print('Ваше число меньше загаданного')

print('Победа')
