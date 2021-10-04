# -*- coding: utf-8 -*-
# @Time    : 2021/10/4 9:36
# @Author  : B612
# @File    : 分割框.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSplitter, QFrame, QHBoxLayout
from PyQt5.QtCore import Qt

"""
    分割框
"""


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)  # 使Frame显示出边框
        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(bottom)
        splitter2.addWidget(splitter1)
        hbox = QHBoxLayout(self)
        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        self.setWindowTitle("分割框")
        self.setGeometry(100, 100, 300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())