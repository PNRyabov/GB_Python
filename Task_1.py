# TASK 1

# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
# running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение
# светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет
# 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между
# режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу
# примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.
import time
import turtle


# ------------------------------------------------------Вариант 1-------------------------------------------------------

# class TrafficLight:
#     __color = "red"
#
#     def running(self):
#         count = 0
#         while True:
#             __color = "red"
#             print("TrafficLight color is --> ", __color)
#             time.sleep(7)
#             __color = "yellow"
#             print("TrafficLight color is --> ", __color)
#             time.sleep(2)
#             __color = "green"
#             print("TrafficLight color is --> ", __color)
#             time.sleep(5)
#             __color = "yellow"
#             print("TrafficLight color is --> ", __color)
#             time.sleep(2)
#             """останавливаем бесконечное мигание"""
#             count += 1
#             if count >= 1:
#                 print(count)
#                 break
#
#
# my_traffic = TrafficLight()
# my_traffic.running()

# ------------------------------------------------------Вариант 2-------------------------------------------------------


class TrafficLight:
    def running(self):
        my = turtle.Screen()
        my.title("My traffic light")
        my.bgcolor("white")
        draw = turtle.Turtle()
        draw.color("black")
        draw.width(2)
        draw.penup()
        draw.goto(-60, 120)
        draw.pendown()
        draw.fd(90)
        draw.rt(90)
        draw.fd(240)
        draw.rt(90)
        draw.fd(90)
        draw.rt(90)
        draw.fd(240)
        __color_red = turtle.Turtle()
        __color_red.shape("circle")
        __color_red.color("red")
        __color_red.penup()
        __color_red.goto(-15, 90)
        __color_yellow = turtle.Turtle()
        __color_yellow.shape("circle")
        __color_yellow.color("black")
        __color_yellow.penup()
        __color_yellow.goto(-15, 0)
        __color_green = turtle.Turtle()
        __color_green.shape("circle")
        __color_green.color("black")
        __color_green.penup()
        __color_green.goto(-15, -90)
        count = 0
        while True:
            __color_red.color("red")
            time.sleep(7)
            __color_red.color("black")
            __color_yellow.color("yellow")
            time.sleep(2)
            __color_yellow.color("black")
            __color_green.color("green")
            time.sleep(5)
            __color_yellow.color("yellow")
            __color_green.color("black")
            time.sleep(2)
            __color_yellow.color("black")
            """останавливаем бесконечное мигание"""
            count += 1
            if count >= 1:
                break


my_traffic = TrafficLight()
my_traffic.running()
