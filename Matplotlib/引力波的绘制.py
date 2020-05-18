import numpy as np
import matplotlib.pyplot as plt
# 读取波形文件（numpy）的库
from scipy.io import wavfile

# 读取下载好的音频文件 赋值给速率rate_h 数据hstrain
# 打印rate_h和hstrain可知H1 Strain图的速率以及点的数组
# 打印rate_l和lstrain可知L1 Strain图的速率以及点的数组 以rb形式进行读取
# 打印.shape[0]可知道点的个数
rate_h, hstrain = wavfile.read(r"H1_Strain.wav", "rb")
rate_l, lstrain = wavfile.read(r"L1_Strain.wav", "rb")
# print(rate_h,hstrain)
# print(hstrain.shape[0])

# 引力波模型的数据 先将文件的每一行转换成字符串序列 将每个字符串序列转换成相应的数据类型
# 再用transpose进行转置
reftime, ref_H1 = np.genfromtxt('wf_template.txt').transpose()  # 使用python123.io下载文件

# 得到波形的时间间隔 通过速率得到
htime_interval = 1 / rate_h
ltime_interval = 1 / rate_l
# # 绘制绘图空间 指定长12宽6
fig = plt.figure(figsize=(12, 6))
#
# 丢失信号起始点 hstrain是个数据矩阵，shape[0]代表读取矩阵第一维度的长度，数据点的个数
#               除rete_h 得到函数在坐标轴上的总长度
# H1 Strain图的Time轴长度 打印htime_len=32.0
htime_len = hstrain.shape[0] / rate_h
# print(htime_len)
# 按时间间隔为步长得到htime的ndarray数组
htime = np.arange(-htime_len / 2, htime_len / 2, htime_interval)
# 画H1 Strain图
plth = fig.add_subplot(221)
plth.plot(htime, hstrain, 'y')
plth.set_xlabel('Time (seconds)')
plth.set_ylabel('H1 Strain')
plth.set_title('H1 Strain')

# 画L1 Strain图
ltime_len = lstrain.shape[0] / rate_l
ltime = np.arange(-ltime_len / 2, ltime_len / 2, ltime_interval)
pltl = fig.add_subplot(222)
pltl.plot(ltime, lstrain, 'g')
pltl.set_xlabel('Time (seconds)')
pltl.set_ylabel('L1 Strain')
pltl.set_title('L1 Strain')

# 画Template Strain图
pltref = fig.add_subplot(212)
pltref.plot(reftime, ref_H1)
pltref.set_xlabel('Time (seconds)')
pltref.set_ylabel('Template Strain')
pltref.set_title('Template')
# 调整图像的四周边缘
fig.tight_layout()

plt.savefig("Gravitational_Waves_Original.png")
plt.show()
plt.close(fig)