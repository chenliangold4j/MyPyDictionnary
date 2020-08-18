# -*- coding: utf-8 -*-

"""
PyQt5 tutorial

In this example, we create a custom widget.

author: py40.com
last edited: 2017年3月
"""
import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QApplication,
                             QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import QObject, Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QFont, QColor, QPen


class Communicate(QObject):
    updateBW = pyqtSignal(int)


class BurningWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setMinimumSize(1, 30)
        # 我们改变了控件的最小大小(高度), 默认值为有点小。

        self.value = 75
        self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]

    def setValue(self, value):

        self.value = value

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()

    def drawWidget(self, qp):

        font = QFont('Serif', 7, QFont.Light)
        qp.setFont(font)
        # 我们使用一个比默认要小的字体。

        size = self.size()
        w = size.width()
        h = size.height()

        step = int(round(w / 10.0))

        till = int(((w / 750.0) * self.value))
        full = int(((w / 750.0) * 700))
        # 控件采用了动态绘制技术。窗体越大，控件也随之变大；反之亦然。这也是我们需要计算自定义控件的载体控件(即窗体)
        # 尺寸的原因。till参数定义了需要绘制的总尺寸，它根据slider控件计算得出，是整体区域的比例值。full参数定义了红色区域的绘制起点。注意在绘制时为取得较大精度而使用的浮点数运算。

        if self.value >= 700:

            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, full, h)
            qp.setPen(QColor(255, 175, 175))
            qp.setBrush(QColor(255, 175, 175))
            qp.drawRect(full, 0, till - full, h)

        else:

            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, till, h)

        pen = QPen(QColor(20, 20, 20), 1,
                   Qt.SolidLine)

        qp.setPen(pen)
        qp.setBrush(Qt.NoBrush)
        qp.drawRect(0, 0, w - 1, h - 1)

        j = 0

        for i in range(step, 10 * step, step):
            qp.drawLine(i, 0, i, 5)
            metrics = qp.fontMetrics()
            fw = metrics.width(str(self.num[j]))
            qp.drawText(i - fw / 2, h / 2, str(self.num[j]))
            j = j + 1
        # 我们使用字体度量来绘制文本。我们必须知道文本的宽度, 以中心垂直线。


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setRange(1, 750)
        sld.setValue(75)
        sld.setGeometry(30, 40, 150, 30)

        self.c = Communicate()
        self.wid = BurningWidget()
        self.c.updateBW[int].connect(self.wid.setValue)

        sld.valueChanged[int].connect(self.changeValue)
        hbox = QHBoxLayout()
        hbox.addWidget(self.wid)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 390, 210)
        self.setWindowTitle('Burning widget')
        self.show()

    def changeValue(self, value):
        self.c.updateBW.emit(value)
        self.wid.repaint()

    # 当滑块发生移动时，changeValue()
    # 方法会被调用。在方法内我们触发了一个自定义的updateBW信号，其参数是当前滚动条的值。该值被用于计算Burning
    # widget的容量值。然后对控件进行重绘。


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
