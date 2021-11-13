import tkinter
import math
import time

canvas_size = 700
canvas = tkinter.Canvas(bg="#08141a", width=canvas_size, height=canvas_size)
canvas.pack()

radius = 250
angle = 270

elements = [0 for _ in range(5)]


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

    tm = time.localtime()

    digital_time = time.strftime('%d.%m.%Y %H:%M:%S', tm)
    elements[0] = canvas.create_text(canvas_size / 2, 40, text=digital_time, fill="#804d33",
                                     font=("PT Sans", 25, "bold"))

    x, y = calculate(tm[3] * 30 + tm[4] / 2 - 90, radius - 90)
    elements[1] = line(x, y, 12, "#591b30")

    x, y = calculate(tm[4] * 6 + tm[5] / 10 - 90, radius - 40)
    elements[2] = line(x, y, 7, "#1b594f")

    x1, y1 = calculate(tm[5] * 6 + 90, radius - 200)
    x2, y2 = calculate(tm[5] * 6 - 90, radius - 30)
    elements[3] = canvas.create_line(x1, y1, x2, y2, width=4, fill="#1b3f59", capstyle="round")

    elements[4] = canvas.create_oval(canvas_size / 2 - 10, canvas_size / 2 - 10,
                                     canvas_size / 2 + 10, canvas_size / 2 + 10, fill="#29264d",
                                     width=0)

    return elements


for i in range(12):
    x, y = calculate(angle + 30, radius - 45)
    canvas.create_text(x, y, text=i + 1, fill="#336680", font=("PT Sans", 35, "bold"))

    angle += 360 / 12

for i in range(60):
    if i % 5 == 0:
        x1, y1 = calculate(angle + 30, radius - 10)
        width = 5
    else:
        x1, y1 = calculate(angle + 30, radius)
        width = 3

    x2, y2 = calculate(angle + 30, radius + 10)
    canvas.create_line(x1, y1, x2, y2, width=width, fill="#1f2b4d", capstyle="round")

    angle += 360 / 60

while True:
    elements = draw(elements)
    canvas.update()
