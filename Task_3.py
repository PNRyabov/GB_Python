# TASK 3

# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.

try:
    f_obj = open("text_3.txt", "r", encoding="utf-8")
    count = 0
    avg_ben = 0
    for line in f_obj:
        my_list = line.split()
        if float(my_list[1]) < 20000:
            print(f"Сотрудник (Фамилия) -> {my_list[0]}")
        avg_ben += float(my_list[1])
        count += 1
    print(f"Средняя зарплата сотрудников равна -> {avg_ben/count}")
except IOError:
    print("Ошибка ввода-вывода!")
except ValueError:
    print("Ошибка: Некорректно введены данные о сотруднике")
finally:
    f_obj.close()
