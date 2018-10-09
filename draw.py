#!python3
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import numpy as np
#測試

plt.subplot(441)
plt.plot([0,0.2,0.5,1],[1,1,0,0]) #a1
plt.subplot(445)
plt.plot([0,0.2,0.5,0.8,1],[0,0,1,0,0])#a2
plt.subplot(449)
plt.plot([0,0.5,0.8,1],[0,0,1,1])#a3
plt.subplot(442) 
plt.plot([0,0.2,0.7,1],[1,1,0,0])#b1
plt.subplot(446)
plt.plot([0,0.3,0.8,1],[0,0,1,1])#b2
plt.subplot(443)
plt.plot([0,0.19,0.2,0.21,1],[0,0,1,0,0])#c1
plt.subplot(447)
plt.plot([0,0.49,0.5,0.51,1],[0,0,1,0,0])#c2
plt.subplot(4,4,11)
plt.plot([0,0.79,0.8,0.81,1],[0,0,1,0,0])#c3

plt.show()
'''
figure, ax = plt.subplots()
# 设置x，y值域
ax.set_xlim(left=0, right=20)
ax.set_ylim(bottom=0, top=10)

line1 = [(1, 1), (5, 5)]
line2 = [(11, 9), (8, 8)]

(line1_xs, line1_ys) = zip(*line1)
(line2_xs, line2_ys) = zip(*line2)

ax.add_line(Line2D(line1_xs, line1_ys, linewidth=1, color='blue'))
ax.add_line(Line2D(line2_xs, line2_ys, linewidth=1, color='red'))

plt.show()

'''
