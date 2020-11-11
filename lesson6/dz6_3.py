"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name ,
surname , position (должность), income (доход). Последний атрибут должен быть
защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker .
В классе Position реализовать методы получения полного имени сотрудника ( get_full_name ) и
дохода с учетом премии ( get_total_income ). Проверить работу примера на реальных данных
(создать экземпляры класса Position , передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


pos1 = Position("Ivan", "Ivanov", "director", 100000, 30000)
print(pos1.name, pos1.surname, pos1.get_full_name(), pos1.get_total_income())

pos2 = Position("Maria", "Petrova", "accountant", 50000, 10000)
print(pos2.name, pos2.surname, pos2.get_full_name(), pos2.get_total_income())
