# 作  者:UJS.Lijie
# 时  间:2021/12/17 0:43
import turtle as tur


def sun_face():
    tur.pensize(3)
    tur.pencolor("red")
    tur.penup()
    tur.goto(-100, 20)
    tur.pendown()
    tur.circle(100, 40)
    tur.mainloop()


if __name__ == '__main__':
    sun_face()
