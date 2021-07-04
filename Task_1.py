# TASK 1

# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

name, par1, par2, par3 = argv


def my_salary(productivity, rate, award):
    try:
        return float(productivity) * float(rate) + float(award)
    except TypeError:
        return "TypeError: check initial data"
    except ValueError:
        return "ValueError: check initial data"


print(my_salary(par1, par2, par3))
