# TASK 4

# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
print("\nEnter the initial string. Format: element1 element2 and etc.: ")
my_str = input().split()
str_num = 1
for i in my_str:
    if len(i) <= 10:
        print(str_num, "\t", i)
    else:
        print(str_num, "\t", i[:10])
    str_num += 1
