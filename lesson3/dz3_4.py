"""
4. Программа принимает действительное положительное число x 
и целое отрицательное число y. Необходимо выполнить возведение числа x 
в степень y. Задание необходимо реализовать в виде функции my_func(x, y). 
При решении задания необходимо обойтись без встроенной функции возведения
 числа в степень.
"""


def my_func(x, y):
    if y == 0:
        return 1
    else:
        return 1 / x * my_func(x, y + 1)

x = float(int(input('Введите действительное положительное число 1: ')))
y = int(input('Введите целое отрицательное число 2: '))

if y < 0 and x > 0:
    print('Число x =', x, 'в степени y =', y, ' равно', my_func(x, y))

else:
    print('Введены неправильные числа.')
