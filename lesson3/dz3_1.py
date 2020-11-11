"""
1. Реализовать функцию, принимающую два числа
(позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку
ситуации деления на ноль.

"""


def fun_del(a, b):
    return a / b


def it_is_digit(string):
    # if string.isdigit():
    #     return True
    # else:
    try:
        float(string)
        return True
    except ValueError:
        return False

while True:
    a = input('Введите число a: ')
    if it_is_digit(a):
        break
    else:
        print(a, 'не является числом')

while True:
    b = input('Введите число b: ')
    if it_is_digit(b):
        if float(b) != 0:
            break
        else:
            print('Делить на 0 нельзя. Введите число b')
    else:
        print(b, 'не является числом')

fa = float(a)
fb = float(b)

print('а = ', fa, ', b = ', fb)
print('a / b =', fun_del(fa, fb))
