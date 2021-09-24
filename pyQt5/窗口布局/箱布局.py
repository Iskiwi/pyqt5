# -*- coding: utf-8 -*-
# @Time    : 2021/9/24 22:08
# @Author  : B612
# @File    : 箱布局.py

"""
    箱布局中，有两个基本的布局类
    QHBoxlayout 水平布局
    QVBoxlayout 垂直布局
"""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton)
from PyQt5.QtGui import QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):

        # 创建两个按键
        btn1 = QPushButton("Yes", self)
        btn2 = QPushButton("No", self)

        # 创建一个水平布局，添入一个可伸长因素，和两个button 按钮
        hbox = QHBoxLayout()
        hbox.addStretch(3)
        hbox.addWidget(btn1)
        hbox.addStretch(7)
        hbox.addWidget(btn2)

        # 垂直布局
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowIcon(QIcon(r"../images/ta.ico"))
        self.setWindowTitle("箱布局")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
