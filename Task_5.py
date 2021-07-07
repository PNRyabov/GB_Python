# TASK 5

# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
# подсчитывать сумму чисел в файле и выводить ее на экран.
from functools import reduce

try:
    with open("text_5.txt", "w", encoding="utf-8") as f_obj:
        my_list = input("Введите числа разделенные пробелами -> ").split()
        my_line = " ".join(my_list)
        f_obj.writelines(my_line)
        f_obj.write("\n")
    with open("text_5.txt", "r", encoding="utf-8") as f_obj:
        my_calc_list = f_obj.read().split()
        my_calc_list = map(float, my_calc_list)
        print(f"Сумма чисел равна -> {reduce(lambda x, y: x + y, my_calc_list)}")
except IOError:
    print("Произошла ошибка ввода-вывода!")
except ValueError:
    print("Ошибка ввода данных. Создан некорректный файл")


