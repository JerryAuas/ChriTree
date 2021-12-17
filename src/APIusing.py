# 作  者:UJS.Lijie
# 时  间:2021/12/16 18:05
import turtle as tur
# 画板参数
# tur.setup(width=0.6,height=0.6)
tur.screensize(600, 600, "green")
tur.setup(width=800,height=800, startx=100, starty=100)
tur.pensize(10)
tur.speed(1)
tur.pencolor('red')

"""
画笔运动命令
"""
# 将当前xy轴进行移动
tur.setx(100)
tur.sety(200)
# 绘制一个三角形
tur.forward(100)    # 向当前画笔方向移动distance像素长度
tur.right(120)      # 顺时针移动degree°     left 逆时针
tur.forward(100)
tur.right(120)
tur.forward(100)

tur.goto(100, 200)    # 将画笔移动到坐标为x,y的位置    路径中会绘制图像
tur.penup()             # 另起一个坐标 路径中不进行绘制
tur.pendown()           #
tur.circle(50)          # 画圆操作， 半径正负表示圆心在画笔的左右


"""
画笔控制命令
"""
tur.fillcolor("")     # 绘制图形的填充颜色
tur.color("", "")       # 同时设置画笔和填充颜色
tur.filling()           # 返回当前是否为填充状态
tur.begin_fill()        # 准备开始填充图形
tur.end_fill()          # 填充结束
tur.hideturtle()        # 隐藏画笔的形状
tur.showturtle()        # 展示画笔的形状


"""
全局控制命令
"""
tur.clear()             # 清空turtle窗口    位置和状态不会变
tur.reset()             # 清空窗口1
tur.undo()              # 撤销上一个动作
tur.isvisible()         # 返回当前turtle是否可见
tur.stamp()             # 复制当前图形
# 写文本，s为文本内容，font是字体的参数，分别为字体名称，大小和类型；font为可选项，font参数也是可选项
tur.write(arg=" ", font=("font-name", "font_size", "font_type"))
