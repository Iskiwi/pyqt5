# -*- coding: utf-8 -*-
# @Time    : 2021/10/3 13:24
# @Author  : B612
# @File    : 切换键.py

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QFrame, QApplication)
from PyQt5.QtGui import QColor

"""
    这个例子是创建三个button，三个按键可以按下和弹起，　三个按键可以混合成一种颜色，在frame 中显示出这种颜色。
    frame中的颜色是三种颜色调和后的状态
"""


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.col = QColor(0, 0, 0)

        redb = QPushButton('Red', self)
        redb.setCheckable(True)  # 创建QPushButton，并且调用setCheckable()方法让它可被选中。
        redb.move(10, 10)

        redb.clicked[bool].connect(self.setColor)  # 把clicked信号连接到我们定义的方法上。我们使用clicked信号来操作布尔值。

        redb = QPushButton('Green', self)
        redb.setCheckable(True)
        redb.move(10, 60)

        redb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.col.name())

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')
        self.show()

    def setColor(self, pressed):

        source = self.sender()  # 返回发送信号的对象
        # 获得发生状态切换的按钮
        print(pressed)  # bool值 True False都会传递过来
        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame { background-color: %s }" %
                                  self.col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())