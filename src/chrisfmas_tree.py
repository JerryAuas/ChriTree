# 作  者:UJS.Lijie
# 时  间:2021/12/16 19:06
import turtle as tur
import time as t
import numpy
import random
from sun_flower import *
from time_block import *
from apple_tree_left import *
from apple_tree_right import *
from sun_face import sun_face


def fpstar():
    """
    绘制书上面的五角星
    :return:
    """
    tur.pensize(3)
    tur.pencolor("yellow")
    tur.fillcolor("red")
    # tur.sety(200)
    # tur.setx(100)

    tur.begin_fill()
    for _ in range(5):
        # tur.penup()
        tur.forward(50)
        tur.right(144)
    tur.end_fill()
    # time.sleep(2)

    tur.penup()
    # tur.goto(-150, -120)
    tur.color("violet")
    # tur.write("Done", font=('Arial', 40, 'normal'))


def first_floor():
    """
    绘制第一层的树
    外层线条为绿色
    填充颜色为绿色
    底部与第二层连接部分为白色线条
    :return:
    """
    tur.penup()
    # tur.setx(200)
    # tur.sety(50)
    tur.goto(30, -23)
    tur.pensize(2)
    tur.fillcolor("green")
    tur.pendown()
    tur.begin_fill()
    tur.pencolor("green")
    tur.right(70)
    tur.circle(150, 23)
    tur.pencolor("yellow")
    tur.pensize(1)
    tur.right(130)
    tur.circle(-30, 30)
    tur.left(102)
    for _ in range(8):
        tur.forward(10)
        tur.right(150)
        tur.forward(10)
        tur.left(150)
    # tur.left(130)
    tur.right(50)
    tur.circle(-30, 30)
    tur.right(130)
    tur.pencolor("green")
    tur.pensize(2)
    tur.circle(150, 24)
    tur.goto(30, -23)
    tur.end_fill()
    # tur.left(140)
    # tur.forward(20)
    # tur.right(140)
    # tur.circle(-70, 20)
    # tur.left(150)
    # tur.forward(20)
    # tur.right(140)
    # tur.circle(-70, 20)
    # tur.left(150)
    # tur.forward(20)
    # tur.right(160)
    # tur.circle(70, 20)
    # tur.left(150)
    # tur.circle(-60, 20)
    # tur.right(150)
    # tur.circle(50, 20)
    # tur.left(110)
    # tur.circle(-40, 20)
    # # tur.forward(20)
    # # tur.left(150)
    # # tur.circle(-70, 20)
    # tur.right(160)
    # tur.pencolor("green")
    # tur.pensize(2)
    # tur.circle(210, 18)
    # tur.goto(30, -23)
    # tur.end_fill()


def second_floor():
    """
    绘制第二层树结构
    :return:
    """
    tur.goto(50, -75)
    tur.pencolor(100, 200, 150)
    tur.fillcolor(100, 200, 150)
    tur.begin_fill()
    tur.right(120)
    tur.circle(100, 25)
    tur.right(150)
    tur.circle(100, 5)
    tur.left(52)
    for _ in range(10):
        tur.forward(10)
        tur.right(120)
        tur.forward(10)
        tur.left(120)
    tur.right(60)
    tur.forward(10)
    tur.right(160)
    tur.circle(90, 30)
    tur.goto(50, -75)
    tur.end_fill()


def third_floor():
    """
    绘制第三层树结构
    :return:
    """
    tur.fillcolor(255, 210, 120)
    tur.goto(75, -110)
    tur.begin_fill()
    tur.pencolor(255, 210, 120)
    tur.right(110)
    tur.circle(100, 30)
    tur.right(150)
    tur.forward(10)
    tur.left(60)
    for _ in range(15):
        tur.forward(10)
        tur.right(120)
        tur.forward(10)
        tur.left(120)
    tur.right(60)
    tur.forward(10)
    tur.right(150)
    tur.circle(93, 30)
    tur.goto(75, -110)
    tur.end_fill()


def forth_floor():
    """
    绘制第四层树结构
    :return:
    """
    tur.fillcolor(100, 100, 100)
    tur.goto(100, -155)
    tur.pencolor(100, 100, 100)
    tur.right(110)
    tur.begin_fill()
    tur.circle(100, 40)
    tur.right(160)
    tur.forward(10)
    tur.left(40)
    for _ in range(19):
        tur.forward(10)
        tur.right(100)
        tur.forward(10)
        tur.left(100)
    tur.right(95)
    tur.forward(10)
    tur.right(130)
    tur.circle(100, 40)
    tur.goto(100, -155)
    tur.end_fill()


def tree_pop():
    """
    绘制树根
    :return:
    """
    tur.fillcolor(200, 100, 0)
    tur.goto(11, -200)
    tur.right(135)
    tur.pencolor("brown")
    tur.begin_fill()
    tur.forward(100)
    tur.left(90)
    tur.forward(30)
    tur.left(90)
    tur.forward(100)
    tur.end_fill()


def left_print():
    """
    圣诞快乐打印函数
    :return:
    """
    dic_x = -100
    dic_y = 240
    tur.goto(dic_x, dic_y)
    arg = "Happy Christmas!"
    for i in arg:
        tur.write(i, font=('Comic Sans MS', 30, 'normal'))
        dic_x += 30
        tur.goto(dic_x, dic_y)
    tur.pendown()


def face_type():
    """
    为太阳创建表情
    以三个半圆表示
    :return:
    """
    # 左眼
    tur.penup()
    tur.goto(-260, 310)
    tur.pencolor("red")
    tur.forward(100)
    tur.pendown()
    tur.right(130)
    tur.circle(20, 180)

    # 右眼
    tur.penup()
    tur.goto(-240, 240)
    tur.pencolor("red")
    tur.pendown()
    tur.right(180)
    tur.circle(20, 180)

    # 嘴
    tur.penup()
    tur.goto(-270, 200)
    tur.pencolor("red")
    tur.pendown()
    tur.circle(-30, 180)
    tur.penup()


def flash_star(color):
    """
    绘制闪光五角星(右侧
    :param color: 颜色
    :return:
    """
    rand_x = random.randint(200, 400)
    rand_y = random.randint(-300, 180)
    tur.goto(rand_x, rand_y)
    tur.penup()
    tur.hideturtle()
    tur.fillcolor(color)
    tur.begin_fill()
    for _ in range(5):
        tur.forward(35)
        tur.right(144)
    tur.end_fill()


def flash_star_up(color):
    """
    绘制上册小五角星
    :param color:
    :return:
    """
    """
    绘制闪光五角星
    :param color: 颜色
    :return:
    """
    rand_x = random.randint(-200, 300)
    rand_y = random.randint(100, 250)
    tur.goto(rand_x, rand_y)
    tur.penup()
    tur.hideturtle()
    tur.fillcolor(color)
    tur.begin_fill()
    for _ in range(5):
        tur.forward(35)
        tur.right(144)
    tur.end_fill()


def flash_map_right(color):
    """
    创建圣诞树右侧闪光灯
    当闪光灯更新时用背景颜色代替
    背景 RGB （31， 247， 255）
    :return:
    """
    rand_x = random.randint(200, 400)
    rand_y = random.randint(-300, 180)
    tur.goto(rand_x, rand_y)
    tur.penup()
    tur.hideturtle()
    tur.fillcolor(color)
    tur.begin_fill()
    tur.circle(10)
    tur.end_fill()


def flash_map_up(color):
    """
    创建圣诞树以上的闪光灯
    :param color: 颜色
    :return:
    """
    rand_x = random.randint(-200, 300)
    rand_y = random.randint(100, 250)
    tur.goto(rand_x, rand_y)
    tur.penup()
    tur.hideturtle()
    tur.fillcolor(color)
    tur.begin_fill()
    tur.circle(10)
    tur.end_fill()


def show_flash():
    """
    显示闪光点
    利用undo（）来进行迭代
    :return:
    """
    while True:
        color_map = (
            'red',
            'yellow',
            'blue',
            'orange',
            'green',
            'purple'
        )
        for color_type in color_map:
            # flash_map_right(color_type)
            # t.sleep(0.1)
            # tur.undo()
            # flash_map_up(color_type)
            # t.sleep(0.1)
            # tur.undo()
            flash_star(color_type)
            t.sleep(0.15)
            tur.undo()
            flash_star_up(color_type)
            t.sleep(0.15)
            tur.undo()
        # for i in range(6):
        #     flash_map_right(color_map[i])
        #     t.sleep(0.2)
        #     tur.undo()
        #     flash_map_up(color_map[i])
        #     t.sleep(0.3)
        #     tur.undo()
        #     flash_star(color_map[i])
        #     t.sleep(0.2)
        #     tur.undo()


def main():
    # tur.setup(1800, 1600, 200, 100)
    # tur.goto(1800, 1600)
    # turtle.tracer(False)
    # Init()
    # SetupClock(160)
    # turtle.tracer(True)
    # Tick()
    # tur.reset()
    # 打开/关闭龟动画，并为更新图纸设置延迟。
    tur.setup(800, 600, -100, -100)
    tur.Screen().colormode(255)  # 设置取值范围到（0,255）默认0-1
    # tur.tracer(False)  # 掩饰状态  False为关   True为开
    # tur.penup()
    tur.bgpic("../img/1.gif")
    tur.speed(0)
    fpstar()
    first_floor()
    second_floor()
    third_floor()
    forth_floor()
    tree_pop()
    apple_right()
    apple_left()
    tur.penup()
    left_print()
    tur.penup()
    tur.goto(-250, 300)
    tur.pendown()
    sun_type()
    face_type()
    show_flash()
    # turtle.tracer(False)
    # Init()
    # SetupClock(160)
    # turtle.tracer(True)
    # Tick()

    tur.mainloop()


if __name__ == "__main__":
    main()
