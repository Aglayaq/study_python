"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
(название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
реализовать переопределение метода draw . Для каждого из классов метод должен выводить
уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра.
"""


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Start drawing...")


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Draw pen", self.title)


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Draw pencil", self.title)


class Marker(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Draw marker", self.title)


sta = []

sta.append(Pen("pen1"))
sta.append(Pencil("pencil1"))
sta.append(Marker("marker1"))

for s in sta:
    s.draw()
