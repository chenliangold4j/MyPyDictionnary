import matplotlib.pyplot as plt
import numpy as np
from sympy import *

n = np.array([i for i in range(201)])
y = n / (3 * n + 1)
plt.figure(figsize=(8, 8))
plt.plot(n, y)
x = symbols('x')
f = x / (3 * x + 1)
x = limit(f, x, np.inf)
print("x=", x)
plt.show()
