# TASK 4 - TASK 6

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
# уроках по ООП.

class Error(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class NotInWarehouse(Error):
    def __init__(self):
        self.text = f"Ошибка: данного товара нет на складе!\n"


class NotInteger(Error):
    def __init__(self):
        self.text = f"Ошибка: требуется ввести количество товара цифрой!\n"


class IsOrgTech(Error):
    def __init__(self):
        self.text = f"Ошибка: данный товар не являетя орг. техникой!\n"


class Warehouse:
    """Индекс подразделения где хранится товар: у склада индекс 0"""
    dep_num = 0

    def __init__(self):
        self._storage = {}

    def add(self, tech_obj, number):
        try:
            if not number.isdigit():
                raise NotInteger()
            if not isinstance(tech_obj, OrgTech):
                raise IsOrgTech()
            self._storage.setdefault(tech_obj.model, []).append([int(number), self.dep_num])
        except NotInteger as er:
            print(er)
        except IsOrgTech as er:
            print(er)

    def peredacha(self, name, value, dep_num):
        try:
            if name not in self._storage:
                raise NotInWarehouse()
            if self._storage[name]:
                if self._storage[name][0][0] - int(value) >= 0 and self._storage[name][0][0] != 0:
                    self._storage[name][0][0] = self._storage[name][0][0] - int(value)
                    self._storage[name].append([int(value), dep_num])
                else:
                    print("\nПередача не возможна! На складе отсутствует техника в таком количестве!\n")
        except NotInWarehouse as er:
            print(er)


class OrgTech:
    def __init__(self, manufacturer, year, eq_type, model):
        self.manufacturer = manufacturer
        self.year = year
        self.eq_type = eq_type
        self.model = model

    def __str__(self):
        return f"Model {eq_type}-{model}-{manufacturer}-{year}"


class Printer(OrgTech):
    def __init__(self, manufacturer, year, eq_type, model):
        super().__init__(manufacturer, year, eq_type, model)

    @staticmethod
    def task(value):
        return f"Print {value} copies"


class Xerox(OrgTech):
    def __init__(self, manufacturer, year, eq_type, model):
        super().__init__(manufacturer, year, eq_type, model)

    @staticmethod
    def task(value):
        return f"Copy {value} copies"


class Scan(OrgTech):
    def __init__(self, manufacturer, year, eq_type, model):
        super().__init__(manufacturer, year, eq_type, model)

    @staticmethod
    def task(value):
        return f"Scan {value} copies"


class TestTech:
    def __init__(self, model, property_paper):
        self.property_paper = property_paper
        self.model = model


my_warehouse = Warehouse()
scaner_1 = Scan("Philips", "1987", "s", "ScanB0-2000")
scaner_2 = Scan("Samsumg", "2000", "s", "Samsa-1")
printer_1 = Printer("HP", "2023", "p", "PR-1")
xerox_1 = Xerox("Xerox", "2003", "x", "Epson - 6000")
bumaga = TestTech("Xerox", 150)
my_warehouse.add(scaner_1, "4")
my_warehouse.add(scaner_2, "6")
my_warehouse.add(printer_1, "8")
print("-----=Тестим возникновение ошибки при вводе количества товара не цифрой=------")
my_warehouse.add(xerox_1, "5sd")
print("-----=Тестим возникновение ошибки по классу объекта=------")
my_warehouse.add(bumaga, "1")
print("Состояние склада -> ", my_warehouse._storage)
my_warehouse.peredacha("PR-1", 2, "021")
my_warehouse.peredacha("PR-1", 10, "031")
print("Состояние склада -> ", my_warehouse._storage)
print("\n-----=Тестим возникновение ошибки при передачи не существующего товара на складе в подразделение=------")
my_warehouse.peredacha("Al-43", 1, "031")
