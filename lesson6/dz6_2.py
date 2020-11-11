"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width
(ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого
для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса
асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см
толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    mass_1m2 = 25 * 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_asphalt_mass(self):
        return self._length * self._width * self.mass_1m2


newroad1 = Road(1000, 20)
print("1000 m x 20 m x", newroad1.mass_1m2, "kg/m2 =", newroad1.get_asphalt_mass()/1000, "t")
newroad2 = Road(5000, 20)
print("5000 m x 20 m x", newroad2.mass_1m2, "kg/m2 =", newroad2.get_asphalt_mass()/1000, "t")
