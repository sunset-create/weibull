# ------------------------------------------------#
"ﾜｲﾌﾞﾙﾌﾟﾛｯﾄ描画プログラム"
# ------------------------------------------------#


import numpy as np
import matplotlib.pyplot as plt
import os

working_path = os.getcwd()

os.chdir(working_path)

time = '30,25,40'
x_str = time.split(',')

x_sort = list(map(float, x_str))

x = np.sort(x_sort)


# データ個数のカウント
x_i = 0
for i in x:
    x_i += 1

# Ftの計算
Ft = [(i - 0.3)/(x_i + 0.4) for i in range(1, x_i + 1)]
y = [np.log(np.log(1/(1-i))) for i in Ft]
log_x = [np.log(i) for i in x]
linear = np.polyfit(log_x, y, 1)
x_2 = np.append(0.1, 10000)
log_x_2 = [np.log(i)for i in x_2]
y2_linear = [linear[0] * x_linear2 + linear[1] for x_linear2 in log_x_2]

fig = plt.figure()
plt.xscale("log")
plt.xlim([1, 10000])
plt.ylim([-7, 2])
plt.scatter(x, y, color='black', marker='s')
plt.plot(x_2, y2_linear)
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(which='major', color='black', linestyle='-')
plt.grid(which='both')
plt.grid(which='minor', color='black', linestyle='-')
plt.grid()

x = [0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 1, 1.5, 2, 3, 4, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 95, 99, 99.8, 99.9]
ya = []
for i in x:
    ya.append(np.log(np.log(1/(1-i/100))))

a = 0

for i in x:
    xa = 10000
    s = i
    plt.text(xa, ya[a], s)
    plt.plot(x_2, [ya[a], ya[a]], color='black', linewidth=0.5)
    a += 1

fig.savefig(working_path + "\\" + "weibull.png")

plt.show()