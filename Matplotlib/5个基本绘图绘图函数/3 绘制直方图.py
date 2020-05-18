# 绘制直方图:直方图有啥元素，肯定得有个数据数组，这可以用numpy来实现一个正态分布、泊松分布的数组啥的
# 总结：1.
# 关键理解bin参数 bin是多少就生成多少个直立的形状
# 怎么做呢：通过数组a，a中数据有个取值范围，
# 直方图将a中数组最大值-最小值均等划分bin个区间
# 但是从元素的值来看他并不是等分落在这个区间上的
# 比如那个正态分布的数组a，在均值100附近落的比较多，
# 所以说在直方图每个区间内落了多少个数据，就构成了那个区间的高度
# 2.
# 直坐标图的颜色，标题边缘线之类的都可以
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
mu,sigma=100,20
a = np.random.normal(mu,sigma,size=100)
# 生成个正态分布的数组a

plt.hist(a,40,histtype='stepfilled',facecolor='c',alpha=0.75)
plt.title('Histgram')
plt.show()

