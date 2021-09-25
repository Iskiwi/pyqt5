# -*- coding: utf-8 -*-
# @Time    : 2021/9/25 15:01
# @Author  : B612
# @File    : 重写事件处理函数.py

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('重写事件处理函数')
        self.show()

    # 这个一个键盘事件的类
    # 通过下面的方法，当我们按下ESC键时程序就会结束。
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
