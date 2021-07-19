# TASK 1

# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_int(cls, date):
        tmp_list = date.split("-")
        tmp_list = list(map(int, tmp_list))
        return tmp_list

    @staticmethod
    def validation(date):
        data, month, year = map(int, date.split('-'))
        if month <= 12 and data <= 31 and year > 0:
            return True
        else:
            return False


my_date = '1-7-21'
one = Date(my_date)
print(one.date)
print(one.date_to_int(my_date))
print(one.validation(my_date))
