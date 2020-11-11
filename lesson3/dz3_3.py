"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, 
и возвращает сумму наибольших двух аргументов.
"""


# вариант 1

def my_func(var1, var2, var3):
    if var1 <= var2 <= var3:
        return var2 + var3
    elif var2 <= var1 <= var3:
        return var1 + var3
    elif var3 <= var2 <= var1:
        return var2 + var1
    elif var2 <= var3 <= var1:
        return var3 + var1
    elif var3 <= var1 <= var2:
        return var1 + var2
    elif var1 <= var3 <= var2:
        return var3 + var2


var1 = int(input('Введите число 1: '))
var2 = int(input('Введите число 2: '))
var3 = int(input('Введите число 3: '))

print('Cумма наибольших = ', my_func(var1, var2, var3))


# вариант 2
def summ_sort(var1, var2, var3):
    l = [var1, var2, var3]
    l.sort()
    return l[2] + l[1]


print('Cумма наибольших = ', summ_sort(var1, var2, var3))

