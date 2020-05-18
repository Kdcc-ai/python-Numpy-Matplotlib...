#                    本节课主要内容如下简单描述

# CSV 文件基本就是用来存放一维数据 二维数据的文件格式
#     excel表格啥的

# 有两个函数可以向CSV文件中读数据 和 写数据
# 保存成表格形式 比较好看(但仅仅是一维二维数据。。。)
import numpy as np
a=np.arange(100).reshape(5,20)
np.savetxt('a.csv',a,fmt='%.1f',delimiter=';')
b=np.loadtxt('a.csv',delimiter=';')
print(b)
