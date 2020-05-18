# 根据百分比进行展示数据的功能
# 总结：饼图有啥元素，肯定就对应啥参数，比如说颜色，某一部分是否突出出来，某部分所占比例，是否有阴影显示，从哪个地方开始画
#       比较容易 这是最值得思考的
import matplotlib.pyplot as plt
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)

plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
# 使之成为一个正圆形的饼图
plt.axis('equal')
plt.show()
