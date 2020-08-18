#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Py40 PyQt5 tutorial

This program creates a menubar. The
menubar has one menu with an exit action.

author: Jan Bodnar
website: py40.com
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        # QAction可以操作菜单栏, 工具栏, 或自定义键盘快捷键。上面三行, 我们创建一个事件和一个特定的图标和一个“退出”的标签。然后, 在定义该操作的快捷键。
        exitAction.triggered.connect(qApp.quit)
        # 当我们点击菜单的时候，调用qApp.quit, 终止应用程序。

        self.statusBar()

        # 创建一个菜单栏
        menubar = self.menuBar()
        # 添加菜单
        fileMenu = menubar.addMenu('&File')
        # 添加事件
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
