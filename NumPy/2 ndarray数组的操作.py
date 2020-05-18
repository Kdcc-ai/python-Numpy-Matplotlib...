#                    本节课主要内容如下简单描述
# 1.索引取值
import  numpy as np
a = np.arange(24).reshape((2,3,4))
print(a[0][0][0])
print(a[-1][-2][-3])

# 2.切片
# 分别取第一块和第二块的第一行第三列的元素值
print(a[:,1,-3])
# 分别取第一块和第二块得第一行~第二行的元素
print(a[:,1:3,:])
# 分别取第一块和第二块以2为步长取每一行的元素
print(a[:,:,::2])