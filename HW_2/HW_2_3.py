#3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

number = int(input('Введите целое число: '))
rev_numbers = 0

while number > 0:
    remains = number % 10 # Находим остаток от деления - последняя цифра
    number = number // 10 # Удаляем последнюю цифру делением на десятки без остатка
    rev_numbers = rev_numbers * 10 # увеличиваем разряд числа
    rev_numbers = rev_numbers + remains # добавляем в новое число последнюю цифру

print(f'Перевернутое ему число: {rev_numbers}')