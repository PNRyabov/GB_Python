# TASK 5

# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
# Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение
# метода draw. Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры
# классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Начало отрисовки"


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Я рисую на асфальте белой ручкой {self.title} слово ХВАТИТ"


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"В коробке с Карандашами лежит наш {self.title}"


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Стереть из памяти все мысли при помощи {self.title}"

penok = Pen("ibonit")
karandash = Pencil("Buzina")
sterka = Handle("Pustota")
print(penok.draw())
print(karandash.draw())
print(sterka.draw())
