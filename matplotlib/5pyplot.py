import matplotlib.pyplot as plt

# plot函数的一般的调用形式：

# #单条线：
# plot([x], y, [fmt], data=None, **kwargs)
# #多条线一起画
# plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)

# 可选参数[fmt] 是一个字符串来定义图的基本属性如：颜色（color），点型（marker），线型（linestyle），
# mt接收的是每个属性的单个字母缩写，例如：
#
# plot(x, y, 'bo-')  # 蓝色圆点实线

# 若属性用的是全名则不能用*fmt*参数来组合赋值，应该用关键字参数对单个属性赋值如：
#
# plot(x,y2,color='green', marker='o', linestyle='dashed', linewidth=1, markersize=6)
#
# plot(x,y3,color='#900302',marker='+',linestyle='-')
#

# 也可以对关键字参数color赋十六进制的RGB字符串如 color='#900302'
#
#     =============    ===============================
#     character        color
#     =============    ===============================
#     ``'b'``          blue 蓝
#     ``'g'``          green 绿
#     ``'r'``          red 红
#     ``'c'``          cyan 蓝绿
#     ``'m'``          magenta 洋红
#     ``'y'``          yellow 黄
#     ``'k'``          black 黑
#     ``'w'``          white 白
#     =============    ===============================
#  点型参数**Markers**,如：marker='+' 这个只有简写，英文描述不被识别
# =============    ===============================
#     character        description
#     =============    ===============================
#     ``'.'``          point marker
#     ``','``          pixel marker
#     ``'o'``          circle marker
#     ``'v'``          triangle_down marker
#     ``'^'``          triangle_up marker
#     ``'<'``          triangle_left marker
#     ``'>'``          triangle_right marker
#     ``'1'``          tri_down marker
#     ``'2'``          tri_up marker
#     ``'3'``          tri_left marker
#     ``'4'``          tri_right marker
#     ``'s'``          square marker
#     ``'p'``          pentagon marker
#     ``'*'``          star marker
#     ``'h'``          hexagon1 marker
#     ``'H'``          hexagon2 marker
#     ``'+'``          plus marker
#     ``'x'``          x marker
#     ``'D'``          diamond marker
#     ``'d'``          thin_diamond marker
#     ``'|'``          vline marker
#     ``'_'``          hline marker
#     =============    ===============================
# 线型参数**Line Styles**，linestyle='-'
#
#     =============    ===============================
#     character        description
#     =============    ===============================
#     ``'-'``          solid line style 实线
#     ``'--'``         dashed line style 虚线
#     ``'-.'``         dash-dot line style 点画线
#     ``':'``          dotted line style 点线
#     =============    ===============================

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
import numpy as np
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
plt.show()
