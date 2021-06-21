# TASK 2

# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

print("Hi, User. We convert seconds to the following time format hh:mm:ss")
print("Please try. Enter the number of seconds")
sec = int(input("Seconds = "))
hour = sec//3600
minutes = (sec - (sec//3600)*3600)//60
sec = sec - (sec//3600)*3600 - ((sec - (sec//3600)*3600)//60)*60
if hour < 10:
    hour = "0" + str(hour)
if minutes < 10:
    minutes = "0" + str(minutes)
if sec < 10:
    sec = "0" + str(sec)
print("\nYour time is: " + str(hour) + ":" + str(minutes) + ":" + str(sec))
