"""
Создайте собственный класс-исключение, обрабатывающий 
ситуацию деления на нуль. Проверьте его работу на данных, 
вводимых пользователем. При вводе пользователем нуля в качестве
 делителя программа должна корректно обработать эту ситуацию и не 
 завершиться с ошибкой.
"""


class MyDivZero(Exception):
    def __init__(self, txt):
        self.txt = txt


x = 0
y = 0

while True:
    try:
        x = int(input('Введите числитель:'))
    except ValueError as err:
        print("Ошибка, введено не число,", err)
    else:
        break

while True:
    try:
        y = int(input('Введите знаменатель:'))
        if y == 0:
            raise MyDivZero("знаменатель равен 0!")
    except ValueError as err:
        print("Ошибка, введено не число,", err)
    except MyDivZero as err:
        print("Ошибка,", err)
    else:
        break

print(f'x={x}, y={y}, x/y={x/y}')
