"""
Реализовать класс «Дата», функция-конструктор которого должна принимать 
дату в виде строки формата «день-месяц-год». В рамках класса реализовать
 два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
 год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
 должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
 Проверить работу полученной структуры на реальных данных.
"""

class Date:

    @classmethod
    def tonumber(cls, datestring):
        n = datestring.split('-')
        day = int(n[0])
        month = int(n[1])
        year = int(n[2])
        if Date.check(day, month, year):
            return year*10000 + month*100 + day
        else:
            return None

    @staticmethod
    def check(day, month, year):
        if 0 < day < 32 and 0 < month < 13 and year > 0:
            return True
        else:
            print("Неправильный формат даты")
            return False

    def __init__(self, datestring):
        self.date=Date.tonumber(datestring)

aa = "29-12-2019"
print(aa)
a = Date(aa)
print(a.date)

print('\n')

bb = "32-14-2020"
print(bb)
b = Date(bb)
print(b.date)

