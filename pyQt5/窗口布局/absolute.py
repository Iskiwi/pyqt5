# -*- coding: utf-8 -*-
# @Time    : 2021/9/24 21:57
# @Author  : B612
# @File    : absolute.py

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel


class Exceple(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        label1 = QLabel("ok", self)
        label2 = QLabel("no", self)
        label3 = QLabel("yes", self)

        label1.move(50, 30)
        label2.move(150, 30)
        label3.move(100, 30)

        self.setGeometry(100, 100, 200, 300)
        self.setWindowTitle("绝对布局")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Exceple()
    sys.exit(app.exec_())
