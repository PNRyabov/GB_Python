# TASK 7

# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
# перегрузку методов # сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
# класса (комплексные числа) и # выполнив сложение и умножение созданных экземпляров. Проверьте корректность
# полученного результата.

class ComplexNumber:
    def __init__(self, real_part, img_part):
        self.real_part = real_part
        self.img_part = img_part

    def __add__(self, other):
        return ComplexNumber(self.real_part + other.real_part, self.img_part + other.img_part)

    def __mul__(self, other):
        return ComplexNumber(self.real_part * other.real_part - self.img_part * other.img_part,
                             self.real_part * other.img_part + self.img_part * other.real_part)

    def __str__(self):
        sign = "+" if self.img_part > 0 else "-"
        return f"{self.real_part}{sign}{abs(self.img_part)}i"


z_1 = ComplexNumber(2, 3)
z_2 = ComplexNumber(-1, 1)
z_3 = ComplexNumber(1, 1)
print("Комплексное число z_1 = ", z_1)
print("Комплексное число z_2 = ", z_2)
print("Комплексное число z_3 = ", z_3)
print("Сложение z_1 + z_2 == ", z_1 + z_2)
print("Сложение z_1 * z_2 == ", z_1 * z_2)
print("---=Тестим сложение и перемножение более чем 2-ух числе одновременно в принте=----")
print("Сложение z_1 + z_2 + z_3 == ", z_1 + z_2 + z_3)
print("Сложение z_1 * z_2 * z_3 == ", z_1 * z_2 * z_3)
