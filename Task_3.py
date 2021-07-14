# TASK 3
# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться
# только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление
# клеток, соответственно. В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
# количества ячеек этих двух клеток.
# Деление.
# Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(),
# принимающий экземпляр класса и количество ячеек в ряду. Данный
# метод позволяет организовать ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****..., где
# количество ячеек между \n равно переданному аргументу.  Если ячеек на формирование ряда не хватает,
# то в последний ряд записываются все оставшиеся. Например, количество ячеек клетки равняется 12,
# количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет
# строку: *****\n*****\n*****.

class Cell:
    def __init__(self, number):
        self.number = int(number)

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number - other.number > 0:
            return Cell(self.number + other.number)
        else:
            return f"Операция не выполнима. Разница количества ячеек клеток отрицательна"

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, lines):
        return "\n".join(["o" * lines for _ in range(self.number // lines)]) + "\n" + "o" * (self.number % lines)


m = Cell(12)
n = Cell(17)
print(m.make_order(5))
print("Число клеток равно: ", (m + n).number)
print((m + n).make_order(8))
