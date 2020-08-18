#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Py40 PyQt5 tutorial

In this example, we position two push
buttons in the bottom-right corner
of the window.

author: Jan Bodnar
website: py40.com
last edited: January 2015
"""
# 我们使用QHBoxLayout和QVBoxLayout，来分别创建横向布局和纵向布局。
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        # addStretch加一段空白
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)
        # 我们创建一个水平布局和添加一个伸展因子和两个按钮。两个按钮前的伸展增加了一个可伸缩的空间。这将推动他们靠右显示。

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        # 创建一个垂直布局，并添加伸展因子，让水平布局显示在窗口底部

        self.setLayout(vbox)
        # 最后, 我们设置窗口的布局界面

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

# 创建一个垂直布局，并添加伸展因子，让水平布局显示在窗口底部
