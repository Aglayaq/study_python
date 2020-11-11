"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
— на ваше усмотрение. Переключение между режимами должно осуществляться только в
указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
и вызвав описанный метод.
"""
import time

class TrafficLight:
    def __init__(self):
        self.__color = "red"

    def running(self):
        seconds = time.time()
        while True:
            print(int(time.time()-seconds), self.__color)
            seconds = time.time()
            if self.__color == "red":
                time.sleep(7)
                self.__color = "yellow"
            elif self.__color == "yellow":
                time.sleep(2)
                self.__color = "green"
            else:
                time.sleep(5)
                self.__color = "red"


tl = TrafficLight()
tl.running()



