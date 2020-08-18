# Matplotlib graphs your data on Figures (i.e., windows, Jupyter widgets, etc.),
# each of which can contain one or more Axes (i.e., an area where points can be specified in terms of
# x-y coordinates (or theta-r in a polar plot, or x-y-z in a 3D plot, etc.).
# The most simple way of creating a figure with an axes is using pyplot.subplots. We can then use Axes.plot to draw some data on the axes:

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()  # Create a figure containing a single axes.
print(fig)
print(ax)
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
# 不指定轴也可以，直接输入，会自动创建
# plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show()

# It's convenient to create the axes together with the figure, but you can also add axes later on, allowing for more complex axes layouts.
fig, axs = plt.subplots(2, 2)
plt.show()
