import tkinter
import math
import time
from datetime import datetime

canvas_size = 700
canvas = tkinter.Canvas(bg="#091921", width=canvas_size, height=canvas_size)
canvas.pack()

radius = 250
angle = 270

elements = [0 for _ in range(6)]


def calculate(_angle, _radius):
    x = math.cos(math.radians(_angle)) * _radius + canvas_size / 2
    y = math.sin(math.radians(_angle)) * _radius + canvas_size / 2

    return x, y


def line(_x, _y, _width, _color):
    return canvas.create_line(canvas_size / 2, canvas_size / 2, _x, _y, width=_width, fill=_color,
                              capstyle="round")


def draw(elements):
    for element in elements:
        canvas.delete(element)

    tm = datetime.utcnow()
    epoch = time.mktime(tm.timetuple())
    tm += datetime.fromtimestamp(epoch) - datetime.utcfromtimestamp(epoch)

    digital_time = tm.strftime('%d.%m.%Y %H:%M:%S')
    elements[0] = canvas.create_text(canvas_size / 2, 40, text=digital_time, fill="#804d33",
                                     font=("PT Sans", 25, "bold"))

    x, y = calculate(tm.hour * 30 + tm.minute / 2 - 90, radius - 110)
    elements[1] = line(x, y, 12, "#591b30")

    x, y = calculate(tm.minute * 6 + tm.second / 10 - 90, radius - 60)
    elements[2] = line(x, y, 7, "#1b594f")

    x, y = calculate(tm.second * 6 + tm.microsecond * 0.000006 - 90, radius - 35)
    elements[3] = line(x, y, 4, "#1b3f59")

    x, y = calculate(tm.second * 6 + tm.microsecond * 0.000006 + 90, radius - 210)
    elements[4] = line(x, y, 4, "#1b3f59")

    elements[5] = canvas.create_oval(canvas_size / 2 - 10, canvas_size / 2 - 10,
                                     canvas_size / 2 + 10, canvas_size / 2 + 10, fill="#29264d",
                                     width=0)

    return elements


for i in range(12):
    if (i + 1) % 3 == 0:
        x, y = calculate(angle + 30, radius)
        canvas.create_text(x, y, text=i + 1, fill="#336680", font=("PT Sans", 25, "bold"))
    else:
        x1, y1 = calculate(angle + 30, radius - 15)
        x2, y2 = calculate(angle + 30, radius + 15)
        canvas.create_line(x1, y1, x2, y2, width=5, fill="#1f2b4d", capstyle="round")

    angle += 360 / 12

while True:
    elements = draw(elements)
    canvas.update()
