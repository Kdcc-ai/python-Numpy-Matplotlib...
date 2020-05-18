#                             前言：
# 有很多创建方法
# 记住这玩意就是用来搞矩阵之类的东西的 相当于线代

# numpy的底层由C语言完成的
# numpy数组对象中的数据类型是自己定义的 python中没有数据类型
# 当ndarray数组中元素不相同的时候 把每个元素都视为一个对象


#                    本节课主要内容如下简单描述
import numpy as np
# 1.
# ones zeros eye linspace生成的数组中的元素都是浮点数类型
# x=np.array([[1,2,3],[1,2,3]])
# print(x)
# print(x.ndim)  记好：这个返回的是轴的数量
# ndarray中的shape属性详见https://blog.csdn.net/qq_38669138/article/details/79084275

# a = np.array([[[0, 1, 2, 3], [4, 5, 6, 7]], [[8, 9, 10, 11], [12, 13, 14, 15]]])
# print(a.sum(axis=2))
# 这么理解24行：再最外层元素中 有两个元素(理解为两块)
#                         每个元素有三个维度(每块有三行)
#                         每个维度下有四个元素(每行有三列)
# 先理解为从最外层到最内层的一个表示方式
# print(np.ones((2,3,4)).ndim)
# print(np.zeros((2,3,4)))
# print(np.eye(5))

# print(np.ones_like([[123,2],[123,33,3]]))

# print(np.linspace(1,10,4))
# print(np.linspace(1,10,4,endpoint=False))
# print(np.concatenate((np.linspace(1,10,4,endpoint=False),np.linspace(1,10,4))))
# 22行等间距的多分成一份 输出[1.   3.25 5.5  7.75]
# 25行进行了数组的合并

# 2.
# ndarray数组还能进行维度变换 并讲了一些函数
# 有的函数进行完之后是改变原数组的 有的不改变原数组

# 3.
# 还能进行ndarray数组的类型变换
# 可以转变数组中元素类型 将ndarrar数组类型转变成一个列表类型

