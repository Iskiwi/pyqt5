# -*- coding: utf-8 -*-
# @Time    : 2021/9/25 14:00
# @Author  : B612
# @File    : 信号与槽.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLCDNumber, QSlider, QVBoxLayout
from PyQt5.QtCore import Qt


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):

        # 窗体内的部件和布局
        Lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal, self)
        slider.valueChanged.connect(Lcd.display)

        vbox = QVBoxLayout()
        vbox.addWidget(Lcd)
        vbox.addWidget(slider)
        self.setLayout(vbox)

        self.adjustSize()
        self.setWindowTitle("信号与槽")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
