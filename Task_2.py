# TASK 2

# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто
# и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для
# костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    tmp = 0

    def __init__(self, cl_vh_parameter):
        self.cl_vh_parameter = cl_vh_parameter

    @property
    @abstractmethod
    def textile(self):
        pass

    def __add__(self, other):
        Clothes.tmp += self.textile + other.textile
        return ClothesZero(0)

    def __str__(self):
        return f"Общий объем расходуемой ткани равен -> {Clothes.tmp}"


class Coat(Clothes):
    def __init__(self, cl_vh_parameter):
        super().__init__(cl_vh_parameter)

    @property
    def textile(self):
        return 2 * self.cl_vh_parameter + 0.3


class Suite(Clothes):
    def __init__(self, cl_vh_parameter):
        super().__init__(cl_vh_parameter)

    @property
    def textile(self):
        return self.cl_vh_parameter / 6.5 + 0.5


"""Данный класс создается для того чтобы перегрузить add правильно"""
"""а именно, чтобы суммировать много параметров в print"""


class ClothesZero(Clothes):
    def __init__(self, cl_vh_parameter):
        super().__init__(cl_vh_parameter)

    @property
    def textile(self):
        return 0


r = Coat(1)
j = Suite(6.5)
m = Suite(6.5)
print(r + j + m)
