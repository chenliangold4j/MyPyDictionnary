import matplotlib.pyplot as plt

# plt.ion()
# 在使用matplotlib的过程中，常常会需要画很多图，但是好像并不能同时展示许多图。这是因为python可视化库matplotlib的显示模式默认为阻塞（block）模式。
# 什么是阻塞模式那？我的理解就是在plt.show()之后，程序会暂停到那儿，并不会继续执行下去。
# 如果需要继续执行程序，就要关闭图片。那如何展示动态图或多个窗口呢？
# 这就要使用plt.ion()这个函数，使matplotlib的显示模式转换为交互（interactive）模式。即使在脚本中遇到plt.show()，代码还是会继续执行。
# 在交互模式下：
#
# plt.plot(x)或plt.imshow(x)是直接出图像，不需要plt.show()
# 如果在脚本中使用ion()命令开启了交互模式，没有使用ioff()关闭的话，则图像会一闪而过，并不会常留。要想防止这种情况，需要在plt.show()之前加上ioff()命令。
# 在阻塞模式下：
#
# 打开一个窗口以后必须关掉才能打开下一个新的窗口。这种情况下，默认是不能像Matlab一样同时开很多窗口进行对比的。
# plt.plot(x)或plt.imshow(x)是直接出图像，需要plt.show()后才能显示图像

plt.ion()
plt.plot([1.6, 2.7])
plt.title("interactive test")
plt.xlabel("index")
# plt.show()
ax = plt.gca()
ax.plot([3.1, 2.2])
plt.draw()
plt.ioff()
plt.plot([1.6, 2.7])
plt.show()


