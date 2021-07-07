# TASK 2

# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

try:
    f_obj = open("text_2.txt", "r", encoding="utf-8")
    count = 1
    for line in f_obj:
        num_word = len(line.split())
        print(f"Формат вывода: (номер строки)(кол-во слов) -> ({count}) ({num_word})")
        count += 1
    print(f"Количество строк в файле -> {count - 1}")  # Не учитываем последнюю пустую строку
except IOError:
    print("Ошибка ввода-вывода!")
finally:
    f_obj.close()
