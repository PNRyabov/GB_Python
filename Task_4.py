# TASK 4

# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.


notation = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
# print(notation)
try:
    f_obj = open("text_4.txt", "r", encoding="utf-8")
    f_obj_new = open("text_4_result.txt", "w", encoding="utf-8")
    my_str = ""
    for line in f_obj:
        my_list = line.split()
        my_str = notation[my_list[0]] + " " + my_list[1] + " " + my_list[2] + "\n"
        f_obj_new.write(my_str)
except IOError:
    print("Ошибка ввода-вывода!")
except KeyError:
    print("Ошибка: некорректно задан словарь")
finally:
    f_obj.close()
    f_obj_new.close()
