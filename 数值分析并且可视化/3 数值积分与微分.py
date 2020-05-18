import numpy as np
import matplotlib.pyplot as plt
a = 1
b = 5
n = 4
h = (b-a)/4
def func(x):
    return 1/x
def ComplTrape():
    S1 = h*(func(b)+func(a))/2
    x = a
    for k in range(1,n):
        S1 += h*func(x+k*h)
    print("复化梯形公式计算结果为 ",S1)
def Romberg():
    # T序列依次取0次等分 1次等分 2次等分 3次等分 4次等分
    # 间距分别为 4 2 1 0.5 0.25
    T = np.zeros(5)
    S = np.zeros(4)
    C = np.zeros(3)
    R = np.zeros(2)
    Distance = [(b-a)/2**i for i in range(5)]
    T[0] = (func(b)-func(a))*(b-a)/2
    # 求出T[1] T[2] T[3] T[4]
    for k in range(1, 5):
        # 化成2**k等分 步长Distance[k]
        x = a
        t1 = (func(a)+func(b))*Distance[k]/2
        for i in range(1,2**k):
            t1 += Distance[k]*func(x+i*Distance[k])
        T[k] = t1
    # 利用公式循环生成S序列 C序列 R序列
    S = [(4 * T[i+1]-T[i])/3 for i in range(0,4)]
    C = [(16 * S[i+1] - S[i])/15 for i in range(0,3)]
    R = [(64 * C[i+1] - C[i])/63 for i in range(0,2)]
    print('T序列 ',str(T))
    print('S序列 ', str(S))
    print('C序列 ', str(C))
    print("龙贝格公式计算结果序列为 ",str(R))
if __name__ == '__main__':
    ComplTrape()
    Romberg()



