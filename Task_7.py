# TASK 7

# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если
# фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней
# прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

my_dict = dict()
final_list = list()
average_profit, count = 0, 0
try:
    with open("text_7.txt", "r", encoding="utf-8") as f_obj:
        for line in f_obj:
            my_list = line.split()
            my_dict.update({my_list[0]: float(my_list[2]) - float(my_list[3])})
            if float(my_list[2]) - float(my_list[3]) >= 0:  # Тут не ясно, учитывать ли 0 или нет. Пока учел.
                average_profit += float(my_list[2]) - float(my_list[3])
                count += 1
        average_profit = average_profit / count
    final_list.append(my_dict)
    final_list.append({"average_profit": average_profit})
    print(f"Итоговый список -> {final_list}")
    with open("my_json.json", "w", encoding="utf-8") as f_json:
        json.dump(final_list, f_json, ensure_ascii=False, indent=0)
except IOError:
    print("Произошла ошибка ввода-вывода!")
except ValueError:
    print("Ошибка ввода данных")
