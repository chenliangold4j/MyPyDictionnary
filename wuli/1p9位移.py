import matplotlib.pyplot as plt
import numpy as np

g = 9.8
v0 = 1
x = range(100)

y = [((-1 * g) / (2 * (v0 ** 2)) * (val ** 2)) for val in x]
print(x)
print(y)
plt.plot(x, y)  # plotting x and y
plt.show()
