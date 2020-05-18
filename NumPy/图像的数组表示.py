#                    本节课主要内容如下简单描述


# # 1.
# from PIL import Image
# import numpy as np
# im = np.array(Image.open('D:/1.PNG'))
# print(im.shape,im.dtype)
# # 打印出一个图像的高度、宽度和图像的RGB值 以及dtype类型

# 一 个Image对象就是一个图像
# 讲了RGB是什么 图像就是有各个RGB（里面有三个参数）的作为元素形成的

# 2. 可以对图像进行灰度变换 任意的色彩变换 ！！比较厉害！！
# 图像可以进行变换 因为图像可以用数组表示的
# 首先读入图像 然后获得像素的RGB值 修改后保存为新的文件
from PIL import Image
import numpy as np
img = np.array(Image.open('D:/1.PNG'))
# 计算RGB三个通道的补值
b = [255,255,255] - img
# 生成一个新的图像类型
im = Image.fromarray(b.astype('uint8'))
# 进行保存
im.save('D:/2.PNG')


