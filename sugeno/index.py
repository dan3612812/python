#!python3
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt


def funa1(i):
    if(i <= 0.2):
        return 1
    if(i >= 0.5):
        return 0

    return -(10 / 3) * i + (5 / 3)


def funa2(i):
    if(i <= 0.2):
        return 0
    if(i >= 0.8):
        return 0
    if(i == 0.5):
        return 1
    if(i < 0.5):
        return (10 / 3) * i - (2 / 3)

    return -(10 / 3) * i + (8 / 3)
#-----


def funa3(i):
    if(i >= 0.8):
        return 1
    if(i <= 0.5):
        return 0

    return (10 / 3) * i - (5 / 3)
# -------


def funb1(i):
    if(i <= 0.2):
        return 1
    if(i >= 0.7):
        return 0

    return (-2 * i) + (14 / 10)


def funb2(i):
    if(i <= 0.3):
        return 0
    if(i >= 0.8):
        return 1

    return(2 * i) - (6 / 10)


def func1(i):
    if(i == 0.2):
        return 1

    return 0


def func2(i):
    if(i == 0.5):
        return 1

    return 0


def func3(i):
    if(i == 0.8):
        return 1

    return 0


def draw(ina, inb, z1, z2, z3, ans):
    plt.subplot(441)
    plt.plot([0, 0.5, 0.8, 1], [0, 0, 1, 1])  # a3
    plt.plot([0, 1], [z1, z1])
    plt.plot([ina, ina, ina], [0, 1, 0])  # ina
    plt.subplot(445)
    plt.plot([0, 0.2, 0.5, 0.8, 1], [0, 0, 1, 0, 0])  # a2
    plt.plot([0, 1], [z2, z2])
    plt.plot([ina, ina, ina], [0, 1, 0])  # ina
    plt.subplot(449)
    plt.plot([0, 0.2, 0.5, 1], [1, 1, 0, 0])  # a1
    plt.plot([0, 1], [z3, z3])
    plt.plot([ina, ina, ina], [0, 1, 0])  # ina
    plt.subplot(442)
    plt.plot([0, 0.2, 0.7, 1], [1, 1, 0, 0])  # b1
    plt.plot([0, 1], [z1, z1])
    plt.plot([inb, inb, inb], [0, 1, 0])  # inb
    plt.subplot(446)
    plt.plot([0, 0.3, 0.8, 1], [0, 0, 1, 1])  # b2
    plt.plot([0, 1], [z2, z2])
    plt.plot([inb, inb, inb], [0, 1, 0])  # inb
    plt.subplot(443)
    plt.plot([0, 0.19, 0.2, 0.21, 1], [0, 0, 1, 0, 0])  # c1
    plt.plot([0, 1], [z1, z1])
    plt.subplot(447)
    plt.plot([0, 0.49, 0.5, 0.51, 1], [0, 0, 1, 0, 0])  # c2
    plt.plot([0, 1], [z2, z2])
    plt.subplot(4, 4, 11)

    plt.plot([0, 0.79, 0.8, 0.81, 1], [0, 0, 1, 0, 0])  # c3
    plt.plot([0, 1], [z3, z3])

    plt.subplot(4, 4, 15)
    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.plot([0, 0.19, 0.2, 0.21, 0.49, 0.5, 0.51, 0.79, 0.8,
              0.81, 1], [0, 0, z1, 0, 0, z2, 0, 0, z3, 0, 0])
    plt.plot([ans,ans,ans],[0,1,0])
    plt.show()


# a 輸入一樣的數 0.3
# b 輸入一樣的數 0.6
ina = 0.3
inb = 0.6
# if(x is a3) or(y is b1) then (z is z1);
# if(x is a2) and(y is b2) then (z is z2);
# if(x is a1) then(z is z3);
z1 = max(funa3(ina), funb1(inb))
z2 = min(funa2(ina), funb2(inb))
z3 = (funa1(ina))
# 權重 z1 20 z2 50 z3 80
# (z1*20 +z2*50 +z3*80) / (z1+z2+z3)
ans = (z1 * 20 + z2 * 50 + z3 * 80) / (z1 + z2 + z3) / 100  # 畫百分比

draw(ina, inb, z1, z2, z3, ans)
