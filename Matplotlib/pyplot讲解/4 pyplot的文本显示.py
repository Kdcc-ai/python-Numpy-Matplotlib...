#                    本节课主要内容如下简单描述:plot函数
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# 就是讲了图上面可以有一些文本的显示 帮助理解
# 增加文本标签 对图形加文本标签  对图形一个位置增加文本
# 带箭头的注释啥的:包括箭头的指向 箭头的位置 箭头的属性 箭头旁边的标签啥的都行(annotate函数)
a = np.arange(0.0,5.0,0.02)
plt.plot(a,np.cos(2*np.pi*a),'r--')

plt.xlabel('横轴,时间',fontproperties='SimHei',fontsize=15,color='green')
plt.ylabel('纵轴,振幅',fontproperties='SimHei',fontsize=15)
plt.title(r'正弦波实例:$y=cos(2\pi x)$',fontproperties='SimHei',fontsize=25)

plt.text(2,1,r'$\mu=100$',fontsize=15)
# 使用Latex格式的文本
plt.axis([-1,6,-2,2])
plt.grid(True)
plt.show()
