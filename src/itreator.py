# 作  者:UJS.Lijie
# 时  间:2021/12/171:47
import turtle
#
# def draw_pentagram(size):
#     count = 1
#     while count <= 5:
#         turtle.forward(size)
#         turtle.right(144)
#         #count = count + 1
#         count += 1

def draw_recursive_pentagram(size):
    '''
    迭代绘制五角星
    '''
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        # count = count + 1
        count += 1
    #五角星绘制完成，更新参数
    size += 10
    if size <= 100:
        draw_recursive_pentagram(size)

def main():
    '''
    主函数
    '''
    #笔抬起来 往后移动一段距离后再开始画
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(3)
    turtle.pencolor('green')
    #size
    size = 50
    draw_recursive_pentagram(size)
    turtle.exitonclick()

if __name__ == '__main__':
    main()
