#                    本节课主要内容如下简单描述:subplot2grid函数 GridSpec类
#                                              subplot函数
#
# # 就是讲了图可以设定网格 选中网格 确定选中行列区域数量
# # 1.
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
plt.subplot2grid((3,3),(2,1),colspan=2)
a=np.arange(10)
plt.plot(a,a*1.5,'m--*',a,a*2.5,a,a*3.5,a,a*4.5)
plt.show()

# 2.通过网格坐标选择区域
gs = gridspec.GridSpec(3,3)
ax1 = plt.subplot(gs[0,:])
ax2 = plt.subplot(gs[1,:-1])
ax3 = plt.subplot(gs[1:,-1])
ax4 = plt.subplot(gs[2,0])
ax5 = plt.subplot(gs[2,1])