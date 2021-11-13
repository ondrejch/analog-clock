import tkinter
import math
import time
from datetime import datetime

canvas_size = 700
canvas = tkinter.Canvas(bg="blue", width=canvas_size, height=canvas_size)
canvas.pack()

radius = 250
angle = 270
digits = hour = minute = second_1 = second_2 = circle = 0


def calculate(_angle, _radius):
    x = math.cos(math.radians(_angle)) * _radius + canvas_size / 2
    y = math.sin(math.radians(_angle)) * _radius + canvas_size / 2

    return x, y


def line(_x, _y, _width, _color):
    return canvas.create_line(canvas_size / 2, canvas_size / 2, _x, _y, width=_width, fill=_color,
                              capstyle="round")


def draw():
    global digits, hour, minute, second_1, second_2, circle

    canvas.delete(digits, hour, minute, second_1, second_2, circle)

    tm = datetime.utcnow()
    epoch = time.mktime(tm.timetuple())
    tm += datetime.fromtimestamp(epoch) - datetime.utcfromtimestamp(epoch)

    digital_time = tm.strftime('%d.%m.%Y %H:%M:%S')
    digits = canvas.create_text(canvas_size / 2, 25, text=digital_time, fill="red", font="Arial 30")

    x, y = calculate(tm.hour * 30 + tm.minute / 2 - 90, radius - 100)
    hour = line(x, y, 4, "white")

    x, y = calculate(tm.minute * 6 + tm.second / 10 - 90, radius - 50)
    minute = line(x, y, 3, "green")

    x, y = calculate(tm.second * 6 + tm.microsecond * 0.000006 - 90, radius - 30)
    second_1 = line(x, y, 2, "red")

    x, y = calculate(tm.second * 6 + tm.microsecond * 0.000006 + 90, radius - 210)
    second_2 = line(x, y, 2, "red")

    circle = canvas.create_oval(canvas_size / 2 - 7, canvas_size / 2 - 7, canvas_size / 2 + 7,
                                canvas_size / 2 + 7, fill="orange", width=0)


for i in range(12):
    x, y = calculate(angle, radius)

    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="yellow", width=2)

    number = i
    if number == 0: number = 12
    canvas.create_text(x, y, text=number, fill="red", font="Arial 20")
    angle += 360 / 12

while True:
    draw()
    canvas.update()
