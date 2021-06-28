# TASK 4

# Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
#
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    if (y < 0) and (x > 0):
        return 1 / (x ** abs(y))
    else:
        return "Ошибка в входных данных"


def my_func2(x, y):
    if (y < 0) and (x > 0):
        pr = x
        for i in range(abs(y) - 1):
            pr = pr * x
        return 1 / pr
    else:
        return "Ошибка в входных данных"


x = int(input("Введите X -> "))
y = int(input("Введите Y -> "))
print(f"Итоговый ответ: {my_func(x, y)}")
