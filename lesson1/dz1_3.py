"""
3. Узнайте у пользователя число n. Найдите сумму чисел
 n + nn + nnn. Например, пользователь ввёл число 3.
 Считаем 3 + 33 + 333 = 369.
"""
# вариант 1. Работает с цифрами от 0 до 9.
x = 0
y = 0
x = input('Вариант 1. Введите число x в промежутке от 1 до 9 включительно: ')
if x.isnumeric():
    x = int(x)
    y = x + (10 * x + x) + (100 * x + 10 * x + x)
    print('Сумма xxx + xx + x = ', y)
else:
    print(x + ' - это строчка')

# вариант 2. Поняла, что вариант читерский, но работает
# c целыми положительными числами любой длины

x = 0
y = 0
x = input('Вариант 2. Введите целое положительное число x: ')
if x.isnumeric():
    y = int(x) + int(x * 2) + int(x * 3)
    print('Сумма xxx + xx + x = ', y)
else:
    print(x + ' - это строчка')
