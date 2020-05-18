# 绘制散点图：每一个点对应图上一个点，使用plt就可以绘制的 这节我们用面向对象的方法绘制 散点图
# 总结：1.
import matplotlib.pyplot as plt
import numpy as np
# fig代表图表 ax代表图表对应区域 默认111
fig,ax = plt.subplots()
# 生成一个标准正态分布
# 使用ax中的plot函数生成对应点 一个x轴 ndarray数组 一个y轴 ndarray数组
ax.plot(10*np.random.randn(100),10*np.random.randn(100),'o')
ax.set_title('Simple Scatter')
plt.show()