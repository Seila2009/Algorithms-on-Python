# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

print('Введите две буквы латинского алфавита: ')

a = ord(input('Первая буква: '))
b = ord(input('Вторая буква: '))

a_num = a - ord('a') + 1
b_num = b - ord('a') + 1
distant = abs(a_num - b_num) - 1

print(f'Позиции указанных букв: {a_num} и {b_num}')
print(f'Между указанными буквами распологается {distant} букв(ы)')
