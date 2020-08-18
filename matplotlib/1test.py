import numpy as np
import matplotlib.pyplot as plt

# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
#
# 在指定的间隔内返回均匀间隔的数字。
#
# 返回num均匀分布的样本，在[start, stop]。
#
# 这个区间的端点可以任意的被排除在外。

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
print(X)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C)
plt.plot(X, S)

plt.show()
