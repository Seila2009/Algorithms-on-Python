# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.

a = 5
b = 6

bit_and = a & b
bit_or = a | b
bit_shift_right = a >> 2
bit_shift_left = a << 2

print(f'Логические побитовые операции над 5 и 6:\n'
      f'5 & 6 = {bit_and}. Операция "И" выбирает бит, если тот присутствует в обоих операндах.\n'
      f'5 | 6 = {bit_or}. Операция "ИЛИ" выбирает бит, если тот присутствует в хотя бы в одном операнде.\n'
      f'5 >> 2 = {bit_shift_right}. Побитовый сдвиг вправо.\n'
      f'Значение левого операнда "сдвигается" вправо на количество бит указанных в правом операнде.\n'
      f'5 << 2 = {bit_shift_left}.  Побитовый сдвиг влево.\n'
      f'Значение левого операнда "сдвигается" влево на количество бит указанных в правом операнде.\n')
