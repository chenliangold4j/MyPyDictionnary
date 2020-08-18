import matplotlib.pyplot as plt
import numpy as np

# This is what you think of as 'a plot', it is the region of the image
# with the data space. A given figure can contain many Axes,
# but a given Axes object can only be in one Figure.
# The Axes contains two (or three in the case of 3D) Axis objects
# (be aware of the difference between Axes and Axis) which take care of the data limits (the data limits can also be controlled via the axes.Axes.set_xlim()
# and axes.Axes.set_ylim() methods). Each Axes has a title (set via set_title()), an x-label (set via set_xlabel()), and a y-label set via set_ylabel()).


# axes.Axes.set_xlim()  axes.Axes.set_ylim()  可以设置xy轴的limit
# set_title()   set_xlabel()  set_ylabel() 可以设置label

x = np.linspace(0, 2, 100)

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x ** 2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x ** 3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()

# 或者直接使用plt
x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, x ** 2, label='quadratic')  # etc.
plt.plot(x, x ** 3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()
