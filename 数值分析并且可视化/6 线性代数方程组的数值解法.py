import numpy as np
# 模拟3阶矩阵 其实
A = np.array([[10,-1,-2],[-1,10,-2],[-1,-1,5]])
# 方程系数矩阵为A 阶数为 A.shape[1]
B = np.array([7.2,8.3,4.2])
# 方程右边的列向量为B
N = 10
# N为最大迭代次数
TOL = 1e-4
# TOL为迭代误差

# 雅可比迭代法
def Jacobi():
    x0 = np.zeros(A.shape[1])
    x = np.zeros(A.shape[1])
    cnt = 0
    while cnt < N:
        for i in range(A.shape[1]):
            temp = 0
            for j in range(A.shape[1]):
                if i!=j:
                    temp+=x0[j]*A[i][j]
            x[i]=(B[i]-temp)/A[i][i]
        Temp = max(abs(x - x0))
        cnt+=1
        if Temp<TOL:
            print('最终迭代方程根为',x)
            return None
        else:
            print('第',cnt,'次迭代方程根为',x)
            x0 = x.copy()
    print('不收敛,最终迭代结果为',x)
# Gauss-Seidel法
def GaussSeidel():
    x0 = np.zeros(A.shape[1])
    x = np.zeros(A.shape[1])
    cnt = 0
    while cnt<N:
        for i in range(A.shape[1]):
            temp = 0
            temps = x0.copy()
            for j in range(A.shape[1]):
                if i!=j:
                    temp+=x0[j]*A[i][j]
            x[i]=(B[i]-temp)/A[i][i]
            x0[i]=x[i].copy()
        Temp = max(abs(x-temps))
        cnt+=1
        if Temp<TOL:
            print('最终迭代方程根为',x)
            return None
        else:
            print('第',cnt,'次迭代方程根为',x)
            x0 = x.copy()
    print('不收敛,最终迭代结果为',x)
# 超松弛法 需要给出松弛因子
def Overre():
    w = 1.07
    x0 = np.zeros(A.shape[1])
    x = np.zeros(A.shape[1])
    cnt = 0
    while cnt<N:
        for i in range(A.shape[1]):
            temp = 0
            temps = x0.copy()
            for j in range(A.shape[1]):
                if i!=j:
                    temp+=x0[j]*A[i][j]
            x[i]=w*((B[i]-temp)/A[i][i])
            x0[i]=x[i].copy()
        Temp = max(abs(x-temps))
        cnt+=1
        if Temp < TOL:
            print('最终迭代方程根为', x)
            return None
        else:
            print('第', cnt, '次迭代方程根为', x)
            x0 = x.copy()
    print('不收敛,最终迭代结果为', x)
if __name__ == '__main__':
    print('雅可比迭代法结果')
    Jacobi()
    print('Gauss-Seidel法结果')
    GaussSeidel()
    print('超松弛法结果')
    Overre()







