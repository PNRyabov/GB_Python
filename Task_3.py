# TASK 3

# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

my_month = int(input("Enter the month number: "))
if (my_month <= 12) and (my_month >= 1):
    # решение через словарь
    my_dict = {1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring", 6: "summer",
               7: "summer", 8: "summer", 9: "autumn", 10: "autumn", 11: "autumn", 12: "winter"}
    print("Dict solution:", my_dict[my_month])

    # решение через список
    my_list = [["winter", 1, 2, 12], ["spring", 3, 4, 5], ["summer", 6, 7, 8], ["autumn", 9, 10, 11]]
    for i in my_list:
        for m in i:
            if m == my_month:
                print("List solution:", i[0])
                break
else:
    print("Please try again and enter the correct month number!")
