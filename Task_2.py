# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя,
# фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные
# аргументы. Реализовать вывод данных о пользователе одной строкой.

def user_data(name, surname, birth_date, year_berth, city, email, phone):
    print(f"{name}, {surname}, {birth_date}, {year_berth}, {city}, {email}, {phone}")


user_data(surname="Ivanov", name="Vasya", year_berth=1987, city="Moscow", email="iv@gmail.com", phone="+79666666666",
          birth_date="22.11")
