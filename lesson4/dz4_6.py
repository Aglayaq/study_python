"""
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""

from itertools import count

from itertools import cycle

for el in count(100):
    if el > 110:
        break
    else:
        print(el)

с = 0
for el in cycle(["зима", "весна", "лето", "осень"]):
    if с > 8:
        break
    print(el)
    с += 1
