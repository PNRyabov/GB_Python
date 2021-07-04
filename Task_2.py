#  TASK 2

# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Пример: [300, 2, 12, 44, 1, 1, 4, 10 , 7, 1, 78, 123, 55]

def my_new_list(my_list):
    try:
        my_new_list1 = [my_list[i] for i in range(1, len(my_list), 1) if float(my_list[i]) > float(my_list[i - 1])]
        return my_new_list1
    except TypeError:
        return "TypeError: check initial data"
    except ValueError:
        return "ValueError: check initial data"


list1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 1, 55]
print(my_new_list(list1))
