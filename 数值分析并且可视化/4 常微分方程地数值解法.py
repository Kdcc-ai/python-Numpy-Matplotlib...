import numpy as np
import matplotlib.pyplot as plt
import math
def func(x,y):
    return y - 2*x/y
x0 = 0
y0 = 1
h = 0.1
N = 10
# 改进的欧拉（Euler）公式
def ImproEuler():
    x1 = np.zeros(N+1)
    y1 = np.zeros(N+1)
    for i in range(N+1):
        x1[i] = x0 + h*(i)
    # 计算y数组各值
    for i in range(N+1):
        if i==0:
            y1[i] = y0
        else:
            k1 = y1[i-1] + h*func(x1[i-1],y1[i-1])
            k2 = y1[i-1] + h*func(x1[i],k1)
            y1[i] = (k1+k2)*1/2
    return x1,y1
# 四阶龙格-库塔(Runge-Kutta)方法
def RungeKutta():
    x1 = np.zeros(N+1)
    y1 = np.zeros(N+1)
    for i in range(N+1):
        x1[i] = x0 + h*(i)
    for i in range(N+1):
        if i==0:
            y1[i] = y0
        else:
            k1 = func(x1[i-1],y1[i-1])
            k2 = func(x1[i-1]+h/2,y1[i-1]+k1*h/2)
            k3 = func(x1[i-1]+h/2,y1[i-1]+k2*h/2)
            k4 = func(x1[i-1]+h,y1[i-1]+h*k3)
            y1[i] = y1[i-1] + (k1+2*k2+2*k3+k4)*h/6
    print(x1,y1)
    return x1,y1
def Draw():
    xEuler,yEuler = ImproEuler()
    xKutta,yKutta = RungeKutta()
    plt.plot(xEuler,yEuler,'*',xKutta,yKutta,'gx',xEuler,np.sqrt(2*xEuler+1),'r')
    plt.annotate(r'Euler Formula or Runge Kutta',xy=(xEuler[5],yEuler[5]),xytext=(xEuler[5],yEuler[5]-0.2),arrowprops=dict(facecolor='black',shrink=0.1,width=2))
    plt.annotate(r'Correct results',xy=(xEuler[10]-0.05,np.sqrt(2*xEuler[10]+1)),xytext=(xEuler[10]-0.05,np.sqrt(2*xEuler[10]+1)-0.2),arrowprops=dict(facecolor='black',shrink=0.1,width=2))
    plt.grid(True)
    plt.savefig('ODE test',dpi = 600)
    plt.show()
if __name__ == '__main__':
    Draw()