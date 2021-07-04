# TASK 6

# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый
# цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle


def task_a(start_point):
    try:
        start_point = int(start_point)
        end_point = start_point + 6
        my_iter = count(start_point)
        for i in range(start_point, end_point, 1):
            print(f"itVal_{i - start_point}=", next(my_iter))
    except SyntaxError:
        print("SyntaxError: invalid syntax")
    except TypeError:
        print("Unsupported operand type(s)")
    except ValueError:
        print("ValueError: invalid initial data")


def task_b(my_list):
    my_iter = cycle(my_list)
    for i in range(len(my_list) + 5):
        print(f"itVal_{i}=", next(my_iter))


"""Тестируем код"""
"""Задание а) - сначала вводим начальное значение параметра с которого начинаем итерировать целые числа"""
"""Задание б) - вводим руками список"""
task_a(input("Enter int number -> "))
task_b(input("Enter list with the space delimiter -> ").split())
