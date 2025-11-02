from PIL import Image, ImageDraw
import random

# 设置图像的宽度和高度
width, height = 2560,1440

# 创建一个白色背景的图像
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# 随机绘制多个图形
num_shapes = 10  # 图形的数量
for _ in range(num_shapes):
    # 随机选择图形类型
    shape_type = random.choice(['rectangle', 'circle', 'ellipse'])
    
    # 随机生成图形的坐标
    x1 = random.randint(0, width - 100)
    y1 = random.randint(0, height - 100)
    x2 = random.randint(x1, width)
    y2 = random.randint(y1, height)

    # 随机生成颜色
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if shape_type == 'rectangle':
        # 绘制矩形
        draw.rectangle([x1, y1, x2, y2], fill=color)
    elif shape_type == 'circle':
        # 绘制圆形
        radius = (x2 - x1) // 2
        center = (x1 + radius, y1 + radius)
        draw.ellipse([x1, y1, x2, y2], fill=color)
    elif shape_type == 'ellipse':
        # 绘制椭圆形
        draw.ellipse([x1, y1, x2, y2], fill=color)

# 保存结果图像
image.save("random_shapes_art.png")
