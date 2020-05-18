# coding=UTF-8
# Author:winyn
'''
给定一个函数，如：f(x)= 1/x，和积分上下限a,b，用机械求积Romberg公式求积分。
'''
import numpy as np
def func(x):
    return np.sin(x)/x
class Romberg:
    def __init__(self, integ_dowlimit, integ_uplimit):
        '''x
        初始化积分上限integ_uplimit和积分下限integ_dowlimit
        输入一个函数，输出函数在积分上下限的积分
        '''
        self.integ_uplimit = integ_uplimit
        self.integ_dowlimit = integ_dowlimit
    def calc(self):
        '''
        计算Richardson外推算法的四个序列
        '''
        # 返回来一个给定形状和类型的用0填充的数组
        t_seq1 = np.zeros(5, 'f')
        s_seq2 = np.zeros(4, 'f')
        c_seq3 = np.zeros(3, 'f')
        r_seq4 = np.zeros(2, 'f')
        # 循环生成hm间距序列(不断二分) [4 2 1 0.5 0.25]
        hm = [(self.integ_uplimit - self.integ_dowlimit) / (2 ** i) for i in range(0,5)]
        print(hm)
        # 计算T0
        fa = func(self.integ_dowlimit)
        fb = func(self.integ_uplimit)
        t0 = (1 / 2) * (self.integ_uplimit - self.integ_dowlimit) * (fa+fb)
        t_seq1[0] = t0
        # 计算T1 T2 T3 T4
        for i in range(1, 5):
            # 每次循环sum赋值为0
            sum = 0
            # 各点间距为2  i循环点数为2**i个
            # hm[i]为i循环节点距离
            for each in range(1, 2**i,2):
                sum =sum + hm[i]*func(self.integ_dowlimit+each * hm[i])#计算两项值总和
            temp1 = 1 / 2 * t_seq1[i - 1]
            temp2 = sum
            temp =  temp1 + temp2
            # 求t_seql的1-4位
            t_seq1[i] = temp
        print('T序列：'+ str(list(t_seq1)))

        # 循环生成s_seq2
        s_seq2 = [round((4 * t_seq1[i + 1] - t_seq1[i]) / 3,6) for i in range(0, 4)]
        print('S序列：' + str(list(s_seq2)))
        # 循环生成c_seq3
        c_seq3 = [round((4 ** 2 * s_seq2[i + 1] - s_seq2[i]) / (4 ** 2 - 1),6) for i in range(0, 3)]
        print('C序列：' + str(list(c_seq3)))
        # 循环生成r_seq4
        r_seq4 = [round((4 ** 3 * c_seq3[i + 1] - c_seq3[i]) / (4 ** 3 - 1),6) for i in range(0, 2)]
        print('R序列：' + str(list(r_seq4)))
        return 'end'
rom = Romberg(1, 5)
print(rom.calc())
