# -*- coding: utf-8 -*-
# @Time    : 2021/9/25 14:00
# @Author  : B612
# @File    : 信号发送者.py

"""
    sender()
    获取信号发送者的信息
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle("发送自定义信号")
        self.setWindowIcon(QIcon("../images/ta.ico"))
        btn1 = QPushButton("btn1", self)
        btn2 = QPushButton("btn2", self)
        btn1.clicked.connect(self.btnclicked)
        btn2.clicked.connect(self.btnclicked)
        btn1.move(30, 30)
        btn2.move(80, 80)
        self.show()

    def btnclicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + "was clicked.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
