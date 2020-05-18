#                    本节课主要内容如下简单描述
import matplotlib.pyplot as plt
import numpy as np
# 画图的库 啥都可以画 还可以把图进行保存!
# 指定x,y轴值绘制(plot函数) 指定y x轴名称(ylabel xlable)
# 指定x轴y轴值在啥区间进行绘制(axis函数)
# 可以画在一个区域内画两个及以上的图形
# (subplot函数 先指定绘图分为几个区域 然后指定在哪个区域进行绘图)

# 例子1:画个普通的图 指定了y坐标为3,1,4,5,2
plt.plot([3,1,4,5,2])
plt.ylabel("grade")
# dpi指的是每一英寸空间中包含点的数量 越多越清楚呗 默认PNG格式
plt.savefig('test2',dpi=10)
plt.show()

# 例子2:两个区域内画图
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)
a = np.arange(0.0,5.0,0.02)
plt.subplot(211)
plt.plot(a,f(a))

plt.subplot(2,1,2)
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.show()





