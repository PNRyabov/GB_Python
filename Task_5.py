# TASK 5

# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом
# работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность
# выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите
# прибыль фирмы в расчете на одного сотрудника.

print("Hi, User! Please Enter Income of your firm.")
income = int(input("Income = "))
print("... and now enter the Costs")
costs = int(input("Costs = "))

if income - costs >= 0:
    print("Прибыль :) Ура! Шикуем!")
    profitability = (income - costs) / costs
    print("Please Enter the number of Staff")
    numStuff = int(input("Stuff = "))
    profPerSingleStuff = profitability / numStuff
else:
    print("Убыток:( Пора бы затянуть пояса")
