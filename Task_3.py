# TASK 3

# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

print("Hi, User!")
print("Please Enter your number. Remember it should be positive")
number = input("Number = ")
if int(number) < 0:
    print("You are wrong. Restart program and Enter the positive number")
else:
    n = len(number)  # Количество разрядов можно еще в цикле посчитать
    number = int(number)
    print("\nYour number is",
          number + (number + 10 ** n * number) + (number + 10 ** n * number + (10 ** (2 * n)) * number))
