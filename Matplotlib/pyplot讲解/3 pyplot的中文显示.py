#                    本节课主要内容如下简单描述:plot函数

# 1.
# pyplot不支持中文显示...醉了
# 想要纵坐标标志成中文得修改哪个reParams属性:这个是把图的所有字体都改变了
# 改变显示字体的名字('font.family'),字体风格(加粗 斜体啥的),字体大小上的都可以..牛逼
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rcParams['font.family']='STSong'
matplotlib.rcParams['font.size']=20

a=np.arange(0.0,5.0,0.02)
plt.xlabel('横轴:时间')
plt.ylabel('纵轴:振幅')
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.show()

# 2.
# pyplot不支持中文显示...醉了
# 可以在有中文输出的地方增加一个属性:fontproperties(在特定需要输入中文的地方进行中文输出)
                            # 收获:这个肯定很灵活


