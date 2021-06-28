# TASK 1

# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
# у пользователя, предусмотреть обработку ситуации деления на ноль.


# ---------------------------------------Вариант 1 с оработойи исключений-----------------------------------------------

def my_division(chisl, znam):
    try:
        return chisl / znam
    except ZeroDivisionError:
        return "\n Ошибка! Деление на ноль!"


x = int(input("Enter nominator: "))
y = int(input("Enter denominator: "))
print(my_division(x, y))


# --------------------------------------Вариант 2 без оработки исключений-----------------------------------------------

# def my_division(chisl, znam):
#     return f"\nResult of division: {chisl / znam}" if znam != 0 else "\nError: division by zero"