# #                    本节课主要内容如下简单描述

# 1.
# # 多维数据的存取的话 python也可以
import numpy as np
a=np.arange(100).reshape(5,20)
a.tofile('a.bat',sep=',',format='%d')
# 这个就以,为分隔符 然后存入个数组
b=np.fromfile('a.bat',dtype=np.int,sep=',')
print(b.reshape(5,20))
# 这个读取也是读入一维数组了 然后可以reshape一下

# 2.
# 另外save load方法同样也可以读文件 便捷方法
# 他比较厉害👍 可以读出来同样的维度到另一个数组中
a=np.arange(100).reshape(5,20)
np.save('c.npy',a)
b=np.load('c.npy')
# print(b)
# 但这样就没法和其他语言或者其他工具打开了