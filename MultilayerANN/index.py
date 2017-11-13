#!python3
import math
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
# 宣告輸入,各路徑
a = 0.1  # 學習率
x1, x2 = 1, 1
w13, w14 = 0.5, 0.9
w23, w24 = 0.4, 1
w35, w45 = -1.2, 1.1
th3, th4, th5 = 0.8, -0.1, 0.3
era = 0  # 疊代次數
elist = []
# 訓練權重
# 重後方輸入
# 誤差梯度
# 當誤差平方和小於0.001及收斂
# 輸入1 輸入2 期望輸出


def fun(x1, x2, yd5):

    while(1):
        # 先算激勵
        global w13, w23, w14, w24, w35, w45, th3, th4, th5, era
        y3 = 1 / (1 + math.exp(-(x1 * w13 + x2 * w23 - th3)))
        y4 = 1 / (1 + math.exp(-(x1 * w14 + x2 * w24 - th4)))
        y5 = 1 / (1 + math.exp(-(y3 * w35 + y4 * w45 - th5)))
        e = yd5 - y5
        era += 1
        d5 = y5 * (1 - y5) * e
        dw35 = a * y3 * d5
        dw45 = a * y4 * d5
        dth5 = a * (-1) * d5  # -1 是th5 輸入的值
        d3 = y3 * (1 - y3) * d5 * w35
        d4 = y4 * (1 - y4) * d5 * w45
        # 權重校正值
        dw13 = a * x1 * d3
        dw23 = a * x2 * d3
        dth3 = a * (-1) * d3
        dw14 = a * x1 * d4
        dw24 = a * x2 * d4
        dth4 = a * (-1) * d4
        # 更新權重值
        w13 += dw13
        w14 += dw14
        w23 += dw23
        w24 += dw24
        w35 += dw35
        w45 += dw45
        th3 += dth3
        th4 += dth4
        th5 += dth5
        return math.pow(e, 2)


while(1):
    sume = round(fun(1, 1, 0) + fun(1, 0, 1) + fun(0, 1, 1) + fun(1, 1, 0), 4)
    elist.append(sume)
    if(sume <= 0.001):
        break
'''
for i in range(0, len(elist)):
    plt.plot(i, elist[i], 'ro')

# plt.axis([0,20000,0.0001,1])
plt.show()
'''
'''
for i in range(0,2000):
    plt.scatter(i,elist[i])

plt.show()
'''
'''
for i in range(0,len(elist)):
    #print(i,round(elist[i],4))
    plt.plot(1,elist[i])
plt.show()
'''

print(w13, w14, w23, w24, w35, w45, th3, th4, th5)
#print("ERA:", era)
# 輸出計算
in1, in2 = 1,1
an3 = 1 / (1 + math.exp(in1 * w13 + in2 * w23 - th3))
an4 = 1 / (1 + math.exp(in1 * w14 + in2 * w24 - th4))
an5 = 1 / (1 + math.exp(an3 * w35 + an4 * w45 - th5))
print("ANS:",an5)
