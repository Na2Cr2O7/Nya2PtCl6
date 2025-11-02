import turtle

# 设置画布和屏幕坐标
window = turtle.Screen()
window.bgcolor("black")

# 创建一个空的圆点
circle = turtle.Turtle()

# 将半径设置为 10
circle.pu()
circle.fillstyle("Red")
circle.begin_fill()

# 使用填充规则填充所有半径的边框
for _ in range(5):
    circle.pu()
    circle.fillstyle("Red", fillcolor="Red")
    circle.left(90)
    circle.pd()

# 我们在这里添加圆的边缘，因为每个点都在画布上绘制一个完整的弧形
circle.fillstyle("Red", fillcolor="Red")
circle.left(135)
circle.pd()

# 设置填充规则为 "Green"
circle.fillstyle("Green")

# 在画板中添加一些颜色
circle.pu()
circle.color('Yellow', 'Green', 'Blue')

circle.penup()  # 首先设置笔尖朝下，这样我们才能在画布上画出完整的图形

# 继续移动直到画布的顶部
circle.left(180)
circle.forward(200)

window.exitonclick()

