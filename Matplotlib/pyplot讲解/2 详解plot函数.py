#                    本节课主要内容如下简单描述:plot函数
import matplotlib.pyplot as plt
import numpy as np
# 只要记住他有那几个参数就可以了 x,y,format_string,**kwargs
# 1.绘制多条曲线 还可以进行曲线颜色的选择:可以用来选择曲线颜色啥样的
#                曲线风格的选择:可以用来选择曲线啥样的 绘制实现 破折线 点划线 虚线啥的
#                曲线标记风格:可以用来标记每个曲线上的点画成啥样子的
#                (为了区别风格 尽量曲线的改变风格)
a=np.arange(10)
plt.plot(a,a*1.5,'m--*',a,a*2.5,a,a*3.5,a,a*4.5)
plt.show()
# 真他妈牛逼 啥都能画,啥样的都能画,你想要啥样的我就画啥样的
