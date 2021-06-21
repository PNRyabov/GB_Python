# TASK 6

# Спортсмен занимается ежедневными пробежками. В первый день его результат
# составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно
# предыдущего. Требуется определить номер дня, на который общий результат спортсмена
# составить не менее b километров. Программа должна принимать значения параметров a и b и
# выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

print("Hi, User! Please Enter initial number of kilometers.")
init_kilometers = int(input("Initial value = "))
print("Now Enter the limit of kilometers required")
limit_kilometers = int(input("Limit value = "))
days = 1
if init_kilometers <= limit_kilometers:
    while init_kilometers < limit_kilometers:
        print(str(days)+"-й день:", "%.2f" % init_kilometers)
        init_kilometers += init_kilometers * 0.1
        days += 1
    print(str(days) + "-й день:", "%.2f" % init_kilometers)
    print("\nОтвет: на " + str(days)+"-й день спортсмен достиг результата - не менее " + str(limit_kilometers)+" км.")
else:
    print("\nYou are wrong. Try again")
