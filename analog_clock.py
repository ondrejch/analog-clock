import tkinter, math, time

sp, vp = 600, 700
pl = tkinter.Canvas(bg='blue', width=sp, height=vp)
pl.pack()

r = 250
u = 270

xs, ys = sp / 2, vp / 2
kruh, d = 0, 0

u = 270

dc = time.localtime()
print(dc[0], dc[1], dc[2], dc[3], dc[4], dc[5])

for i in range(12):
    x = math.cos(math.radians(u)) * r + xs
    y = math.sin(math.radians(u)) * r + ys

    pl.create_oval(x - 20, y - 20, x + 20, y + 20, fill='yellow', width=2)

    c = i
    if c == 0: c = 12
    pl.create_text(x, y, text=c, fill='red', font="Arial 20")
    u += 360 / 12


def kresli():
    global kruh, d

    pl.delete(kruh, d)

    dc = time.localtime()

    digi = str(dc[2]) + '.' + str(dc[1]) + '.' + str(dc[0]) + ' ' + str(dc[3]) + ':' + str(dc[4]) + ':' + str(dc[5])

    d = pl.create_text(300, 25, text=digi, fill='red', font='Arial 30')
    u = 360 / 60 * dc[5] + 270

    x = math.cos(math.radians(u)) * r + xs
    y = math.sin(math.radians(u)) * r + ys

    kruh = pl.create_oval(x - 10, y - 10, x + 10, y + 10, fill='red', width=2)


while True:
    kresli()
    pl.update()
