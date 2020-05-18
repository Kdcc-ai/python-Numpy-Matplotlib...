# #                    本节课主要内容如下简单描述 ！随机数函数！
import numpy as  np
# 1.
# 介绍了一些numpy的随机数函数：生成随机数数组、正态分布数组、泊松分布数组都可以
print(np.random.randn(3,4,5))
# 正态分布
# 随机生成100-200的数 3行4列
print(np.random.randint(100,200,(3,4)))

# 2.
# 比较厉害的随机数函数：shuffle(对数组第0轴进行乱序排列) permutation(对数组第0轴进行乱序排列)
# choice：随机抽取元素形成size形状新数组(可以重复 可以不重复元素 还可以指定抽取概率)
a = np.random.randint(100,200,(8,))
print(np.random.choice(a,(3,2)))
print(np.random.choice(a,(3,2),p=a/sum(a)))

# 3.
# 比较厉害的随机数函数：uniform(产生具有均匀分布的指定形状的数组)
#                      normal(产生具有正太分布的指定形状的数组)
#                      poisson(产生泊松分布的指定形状的数组)
