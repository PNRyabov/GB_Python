# TASK 1

# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые
# пользователем. Об окончании ввода данных свидетельствует пустая строка.

try:
    f_obj = open("text_1.txt", "w", encoding="utf-8")
    while True:
        my_str = input("Введите строку для записи в файл (\"\" - выход) -> ")
        if my_str == "":
            break
        else:
            f_obj.write(my_str + "\n")
except IOError:
    print("Ошибка ввода-вывода!")
finally:
    f_obj.close()
