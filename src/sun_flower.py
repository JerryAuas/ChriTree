# 作  者:UJS.Lijie
# 时  间:2021/12/16 18:43
import turtle as tur
import time


def sun_type():
    tur.speed(10)
    tur.pencolor("yellow")
    tur.fillcolor("yellow")
    tur.begin_fill()
    for _ in range(36):
        tur.forward(200)
        tur.left(170)
    tur.end_fill()


if __name__ == '__main__':
    sun_type()
