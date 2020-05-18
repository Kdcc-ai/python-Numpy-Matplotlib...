import numpy as np
import matplotlib.pyplot as plt
# from scipy.interpolate import spline
N = 10
TOL = 1e-5
def func(x):
    return x**3 - x - 1
def f(x):
    return 3*(x**2) - 1
def Bindary():
    low,high = 1,2
    for i in  range(N):
        g = (low + high) / 2
        if func(g) == 0 or (high-low)/2 < TOL:
            return g
        elif func(low)*func(g) > 0:
            low = g
        else:
            high = g
    #         返回二分法第N次计算所得的根
    return g
def Newton():
    low, high = 1, 2
    NewtonApprox = np.zeros(N+1)
    NewtonApprox[0] = low
    if func(low)==0:
        return low
    for i in range(1,N+1):
        NewtonApprox[i] = NewtonApprox[i-1] - func(NewtonApprox[i-1])/f(NewtonApprox[i-1])
    #     返回牛顿法N次计算所得的根
    return NewtonApprox
def Secant():
    low, high = 1, 2
    SecantApprox = np.zeros(N+1)
    SecantApprox[0] = low
    SecantApprox[1] = low+0.1
    if func(low)==0:
        return low
    for i in range(2,N+1):
        SecantApprox[i] = SecantApprox[i-1] - func(SecantApprox[i-1])*(SecantApprox[i-1]-SecantApprox[i-2])/(func(SecantApprox[i-1])-func(SecantApprox[i-2]))
    return SecantApprox
def Draw():
    Bind = Bindary()
    print("二分法求解方程的近似根为 ",Bind)
    Newton1 = Newton()
    Secant1 = Secant()
    x = 2*np.random.rand(10)
    x1 = np.linspace(1,2,502)
    y1 = x1**3 - x1 - 1
    plt.plot(x1,y1)
    plt.xlabel('X',size=15,horizontalalignment='right')
    plt.ylabel('Y',size=15,verticalalignment='top')
    plt.axhline(y=0,color='b',linestyle='--')
    plt.annotate(r'y = 0', xy=(2,0), xytext=(1.7, 0.4),size=15,
                 arrowprops=dict(facecolor='black', shrink=0.2, width=0.6))
    plt.annotate(r'y = x**3 - x - 1', xy=(1.8,3), xytext=(1.3, 3.4),size=15,
                 arrowprops=dict(facecolor='black', shrink=0.2, width=0.6))
    plt.scatter(Newton1[0:N],func(Newton1[0:N]),color='black')
    plt.scatter(Secant1[0:N-1], func(Secant1[0:N-1]), color='orange')
    plt.plot(1.1, 4.0, color="black", linewidth=2.5, linestyle='solid', label="Newton")
    plt.plot(1.1, 3.5, color="orange", linewidth=2.5, linestyle='solid', label="Secant")
    plt.legend(loc='upper left')
    plt.title('Antiderivative graph')
    plt.savefig('Extract a root',dpi=600)
    plt.show()
if __name__ == '__main__':
    Draw()




