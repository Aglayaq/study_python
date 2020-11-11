"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета 
заработной платы сотрудника. В расчете необходимо использовать формулу: 
(выработка в часах * ставка в час) + премия. Для выполнения расчета для 
конкретных значений необходимо запускать скрипт с параметрами.
"""

import sys


def get_salary(production, rate, bonus):
    return f'Зарплата с премией - {int(production)*int(rate)+int(bonus)} руб.'


# ввод данных через командную строку.
# пример ввода: python dz_1.py 55 6 8

if len(sys.argv) == 4:
    print(get_salary(sys.argv[1], sys.argv[2], sys.argv[3]))
else:
    print('неверное количество аргументов')