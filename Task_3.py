# TASK 3

# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class IsNumList(Exception):
    text = "***Вы ввели не число***"

    def __str__(self):
        return self.text


my_list = list()
while True:
    try:
        el = input("Введите элемент списка [Выход (q)] -> ")
        if el == "q":
            break
        else:
            if el.isnumeric():
                 my_list.append(int(el))
            else:
                raise IsNumList()
    except IsNumList as err:
        print(err)
print(my_list)
