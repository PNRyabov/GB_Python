# TASK 4

# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

print("Hi, User! Please Enter your number.")
number = int(input("Number = "))
maxDigit = number % 10
while number > 10:
    number = (number - number % 10) // 10
    if maxDigit < number % 10:
        maxDigit = number % 10
print("\nThe maximum digit in the number is:", maxDigit)
