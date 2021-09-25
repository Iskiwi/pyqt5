# -*- coding: utf-8 -*-
# @Time    : 2021/9/25 14:00
# @Author  : B612
# @File    : 发送自定义信号.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QIcon


# 从QObejct生成的对象可以发送信号
class Communite(QObject):
    closeApp = pyqtSignal()
    # 信号使用了pyqtSignal()方法创建


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle("发送自定义信号")
        self.setWindowIcon(QIcon("../images/ta.ico"))
        # 实例化自定义的信号，并连接与窗口的关闭连接起来
        self.c = Communite()
        self.c.closeApp.connect(self.close)
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
