# TASK 7

# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
# for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только
# первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def rec_fact(n):
    try:
        if n >= 2:
            return n * rec_fact(n - 1)
        else:
            return 1
    except SyntaxError:
        print("SyntaxError: invalid syntax")
    except TypeError:
        print("Unsupported operand type(s)")
    except ValueError:
        print("ValueError: invalid initial data")


def fact(n):
    try:
        for i in range(n + 1):
            yield rec_fact(i)
    except SyntaxError:
        print("SyntaxError: invalid syntax")
    except TypeError:
        print("Unsupported operand type(s)")
    except ValueError:
        print("ValueError: invalid initial data")


n = int(input("Enter the final number of factorial -> "))
for el in fact(n):
    print(el)
