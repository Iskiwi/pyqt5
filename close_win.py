# -*- coding: utf-8 -*-
# @Time    : 2021/9/20 17:42
# @Author  : B612
# @File    : close_win.py

# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget
from PyQt5.QtCore import QCoreApplication


class QuitButton(QWidget):
    def __init__(self):
        super().__init__()
        self.press()

    def press(self):

        self.setGeometry(100, 200, 300, 300)
        self.setWindowTitle("这是我的关闭按钮程序")

        btn = QPushButton("close the window", self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(150, 200)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    button = QuitButton()
    sys.exit(app.exec_())



