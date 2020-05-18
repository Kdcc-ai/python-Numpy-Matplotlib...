import numpy as np
import matplotlib.pyplot as plt
def main(x):
    # 模拟 p(x)=2x+1 给定
    b,a = 2,1
    # 给出4个插值节点
    xi = np.array([0.4,0.5,0.6,0.7])
    yi = np.array([-0.9163,-0.6931,-0.5108,-0.3567])
    yLangage = 0
    # 拉格朗日插值节点值为yLangage
    for k in range(4):
        t = yi[k]
        for j in range(4):
            if j!=k:
                t*=(x-xi[j])/(xi[k]-xi[j])
        yLangage += t
    # 牛顿插值节点值为yNewton
    # [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    # 首先构造差商表
    yNewton = 0
    Q = [[0] * 4 for _ in range(4)]
    for n in range(4):
        Q[n][0]=yi[n]
    for i in range(1,4):
        for j in range(i,4):
            Q[j][i]=(Q[j][i-1]-Q[j-1][i-1])/(xi[j]-xi[j-i])
    # 得到差商表对角线值
    qDiagonal=[]
    for i in range(4):
        qDiagonal.append(Q[i][i])
    yNewton += qDiagonal[0]
    # 代入②插值多项式
    for i in range(1,4):
        p = qDiagonal[i]
        for j in range(i):
            p*=(x-xi[j])
        yNewton+=p
    # 线性拟合
    z = np.polyfit(xi, yi, 1)
    p = np.poly1d(z)
    y = []
    for i in range(4):
        y.append(p(xi[i]))
    # 拉格朗日插值节点值：  yLangage
    # 牛顿插值节点值：      yNewton
    # 通过matplotlib模块进行画图
    # 图分为三块 序号1位置为拉格朗日插值图 序号2位置为牛顿插值图
    # 序号3为线性拟合图
    plt.subplot(221)
    plt.plot(xi,yi,'k')
    plt.scatter(x,yLangage,color='red')
    plt.title('Lagrange Example')
    plt.subplot(222)
    plt.plot(xi,yi,'k')
    plt.scatter(x, yNewton, color='red')
    plt.title('Newton Example')
    plt.subplot(223)
    plt.plot(xi,y,'k')
    plt.scatter(xi,yi,color='red')
    plt.title('Linar Example')
    plt.savefig('DifValue test',dpi=600)
    plt.show()
    print("拉格朗日插值结果为：",yLangage)
    print("牛顿插值结果为：",yNewton)
if __name__ == '__main__':
    x = 0.54
    main(x)