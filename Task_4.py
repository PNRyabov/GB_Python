# TASK 4
#
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
# color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны
# сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar,
# SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Скорость автомобиля {self.name} -> {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Скорость автомобиля {self.name} -> {self.speed}")
        if self.speed >= 60:
            print(f"Превышение скорости на {self.speed - 60}")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Скорость автомобиля {self.name} -> {self.speed}")
        if self.speed >= 40:
            print(f"Превышение скорости на {self.speed - 40}")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def is_police_car(self):
        if self.is_police:
            print(f"{self.name} спешит на помощь")
        else:
            print(f"{self.name} гражданская тачка.")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


beha = SportCar(100, "Black", "BMW", False)
mers = TownCar(100, "White", "MersedesBentz", False)
zver = WorkCar(45, "Grey", "Buhanka", False)
ford = PoliceCar(110, 'Blue', 'Ford', True)
zver.turn("налево")
beha.show_speed()
print(beha.name)
ford.is_police_car()
mers.show_speed()
zver.show_speed()
