# 作  者:UJS.Lijie
# 时  间:2021/12/170:17
import turtle


def apple_right():
    turtle.speed(5)
    turtle.pensize(5)

    # 先画一个圆,并填充为红色
    turtle.begin_fill()
    turtle.color("red")
    turtle.penup()
    turtle.goto(70, -150)
    turtle.circle(radius=10)
    turtle.end_fill()

    # 画苹果把儿
    turtle.color("brown")
    turtle.pu()
    turtle.goto(52, -140)
    turtle.pd()
    turtle.right(90)
    turtle.circle(18, 40)
    turtle.pu()
    turtle.seth(105)
    turtle.goto(57, -140)
    turtle.pd()
    turtle.circle(18, 50)
    turtle.pd()

    # 画左边叶子
    turtle.begin_fill()
    turtle.color("green")
    turtle.circle(18, 50)
    turtle.seth(-30)
    turtle.circle(18, 55)
    turtle.end_fill()

    # 画右边叶子
    turtle.begin_fill()
    turtle.color("green")
    turtle.seth(15)
    turtle.circle(36, 50)
    turtle.seth(-180)
    turtle.circle(18, 50)
    turtle.end_fill()


if __name__ == '__main__':
    apple()