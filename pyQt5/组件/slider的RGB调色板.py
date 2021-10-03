# -*- coding: utf-8 -*-
# @Time    : 2021/10/3 14:05
# @Author  : B612
# @File    : slider的RGB调色板.py

import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QPushButton, QHBoxLayout, QGridLayout,
                             QLabel, QApplication, QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

"""
    这个例子是通过slider来创建一个RGB的调色板
    思路：
    1、slider的value是0-99 /int型， RGB的取值是0-255
    value/100*256 可能结果会是float型，所以取整
    2、可以直接 QColor(a, b, c)
    但是可以复习切换按键 
    3、包括 slider button 标签显示各元素的大小 frame 
"""


import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QPushButton, QHBoxLayout, QGridLayout,
                             QLabel, QApplication, QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

"""
    这个例子是通过slider来创建一个RGB的调色板
    思路：
    1、slider的value是0-99 /int型， RGB的取值是0-255
    value/100*256 可能结果会是float型，所以取整
    2、可以直接 QColor(a, b, c)
    但是可以复习切换按键 
    3、包括 slider button 标签显示各元素的大小 frame 
"""


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.r = 0
        self.g = 0
        self.b = 0
        self.initUI()

    def initUI(self):
        # 滑动条
        Rslider = QSlider(Qt.Horizontal, self)
        Rslider.setGeometry(100, 60, 100, 20)
        Rslider.valueChanged[int].connect(self.setR)
        Gslider = QSlider(Qt.Horizontal, self)
        Gslider.setGeometry(100, 90, 100, 20)
        Gslider.valueChanged[int].connect(self.setG)
        Bslider = QSlider(Qt.Horizontal, self)
        Bslider.setGeometry(100, 120, 100, 20)
        Bslider.valueChanged[int].connect(self.setB)

        # 按键
        RGB = QPushButton("混合三种颜色", self)
        RGB.clicked.connect(self.RGB_)

        self.frame = QFrame(self)
        self.col = QColor(0, 0, 0)
        self.frame.setGeometry(350, 50, 150, 150)
        self.frame.setStyleSheet("QFrame { background-color: %s }" %
                                  self.col.name())

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Slider的RGB调色板')
        self.show()

    def setR(self, value):
        self.r = int(value * 256 / 100)

    def setG(self, value):
        self.g = int(value * 256 / 100)

    def setB(self, value):
        self.b = int(value * 256 / 100)

    def RGB_(self):
        self.col = QColor(self.r, self.g, self.b)
        self.frame.setStyleSheet("QFrame { background-color: %s }" %
                                 self.col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())