import tkinter, math, time

width, height = 600, 700
canvas = tkinter.Canvas(bg="blue", width=width, height=height)
canvas.pack()

radius = 250
angle = 270
digits = hour = minute = second_1 = second_2 = circle = 0


def calculate(_angle, _radius):
    x = math.cos(math.radians(_angle)) * _radius + width / 2
    y = math.sin(math.radians(_angle)) * _radius + height / 2

    return x, y


def line(_x, _y, _width, _color):
    return canvas.create_line(width / 2, height / 2, _x, _y, width=_width, fill=_color,
                              capstyle="round")


def draw():
    global digits, hour, minute, second_1, second_2, circle

    canvas.delete(digits, hour, minute, second_1, second_2, circle)
    tm = time.localtime()

    digital_time = f"{tm[2]:02}.{tm[1]:02}.{tm[0]:04} {tm[3]:02}:{tm[4]:02}:{tm[5]:02}"
    digits = canvas.create_text(300, 25, text=digital_time, fill="red", font="Arial 30")

    x, y = calculate(tm[3] * 30 - 90, radius - 100)
    hour = line(x, y, 4, "white")

    x, y = calculate(tm[4] * 6 - 90, radius - 50)
    minute = line(x, y, 3, "green")

    x, y = calculate(tm[5] * 6 - 90, radius - 30)
    second_1 = line(x, y, 2, "red")

    x, y = calculate(tm[5] * 6 + 90, radius - 210)
    second_2 = line(x, y, 2, "red")

    circle = canvas.create_oval(width / 2 - 7, height / 2 - 7, width / 2 + 7, height / 2 + 7,
                                fill="orange", width=0)


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
