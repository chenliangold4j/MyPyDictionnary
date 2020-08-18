import numpy as np
import matplotlib.pyplot as plt

# matplotlib有一套完全仿照MATLAB的函数形式的绘图接口，在matplotlib.pyplot模块中。这套函数接口方便MATLAB用户过度到matplotlib包

# 在绘图结构中，figure创建窗口，subplot创建子图。所有的绘画只能在子图上进行。plt表示当前子图，
# 若没有就创建一个子图。所有你会看到一些教程中使用plt进行设置，一些教程使用子图属性进行设置。他们往往存在对应功能函数。

# Figure：面板(图)，matplotlib中的所有图像都是位于figure对象中，一个图像只能有一个figure对象。
#
# Subplot：子图，figure对象下创建一个或多个subplot对象(即axes)用于绘制图像。

# 配置参数：
# axex: 设置坐标轴边界和表面的颜色、坐标刻度值大小和网格的显示
# figure: 控制dpi、边界颜色、图形大小、和子区( subplot)设置
# font: 字体集（font family）、字体大小和样式设置
# grid: 设置网格颜色和线性
# legend: 设置图例和其中的文本的显示
# line: 设置线条（颜色、线型、宽度等）和标记
# patch: 是填充2D空间的图形对象，如多边形和圆。控制线宽、颜色和抗锯齿设置等。
# savefig: 可以对保存的图形进行单独设置。例如，设置渲染的文件的背景为白色。
# verbose: 设置matplotlib在执行期间信息输出，如silent、helpful、debug和debug-annoying。
# xticks和yticks: 为x,y轴的主刻度和次刻度设置颜色、大小、方向，以及标签大小。
#
# 线条相关属性标记设置
# 线条风格linestyle或ls	描述
# ‘-‘	实线
# ‘:’	虚线
# ‘–’	破折线
# ‘None’,’ ‘,’’	什么都不画
# ‘-.’	点划线

# 线条标记
# 标记maker            描述
#
# ‘o’                 圆圈
# ‘.’                 点
# ‘D’                 菱形
# ‘s’                 正方形
# ‘h’                 六边形1
# ‘*’                 星号
# ‘H’                 六边形2
# ‘d’                 小菱形
# ‘_’                 水平线
# ‘v’                 一角朝下的三角形
# ‘8’                 八边形
# ‘<’                 一角朝左的三角形
# ‘p’                 五边形
# ‘>’                 一角朝右的三角形
# ‘,’                 像素
# ‘^’                 一角朝上的三角形
# ‘+’                 加号
# ‘\  ‘               竖线
# ‘None’,’’,’ ‘       无
# ‘x’                 X
#
# 颜色
#
# 别名             颜色
#
# b               蓝色
# g               绿色
# r               红色
# y               黄色
# c               青色
# k               黑色
# m               洋红色
# w               白色



