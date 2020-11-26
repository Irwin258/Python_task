# Задача 2
# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def call_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self._v = v

    @property
    def call_consumption(self):
        return round(self._v/6.5 + 0.5, 1)


class Suit(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self._h = h

    @property
    def call_consumption(self):
        return round(self._h * 2 + 0.3, 1)


coat_1 = Coat("Пальто", 54).call_consumption
coat_2 = Coat("Пальто_2", 52).call_consumption
suit_1 = Suit("Костюм", 1.98).call_consumption
suit_2 = Suit("Костюм_2", 1.78).call_consumption
print(coat_1 + coat_2)
print(suit_1 + suit_2)
