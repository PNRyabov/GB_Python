# TASK 2

# Создайте собственный класс - исключение, обрабатывающий ситуацию деления на нуль.Проверьте его работу на
# данных, вводимых пользователем.При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class MyZeroDiv(Exception):
    text = "Деление на 0!"

    def __str__(self):
        return self.text


numenator_data = input("Введите числитель число: ")
denumenator_data = input("Введите знаменатель число: ")

try:
    numenator_data = int(numenator_data)
    denumenator_data = int(denumenator_data)
    if denumenator_data == 0:
        raise MyZeroDiv("Деление на 0!")
except TypeError:
    print("Вы ввели не число")
except ValueError:
    print("Вы ввели не число")
except MyZeroDiv as err:
    print(err)
else:
    print(f"Все хорошо. Результат деления: {numenator_data / denumenator_data}")
