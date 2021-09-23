# -*- coding: utf-8 -*-
# @Time    : 2021/9/23 17:32
# @Author  : B612
# @File    : 状态栏.py

"""
    状态栏是用来显示状态信息的部件
    状态栏由QMainWindow 帮助创建

    注意：
    1、
    statusBar由QMainWindow 创建，第一次调用这个方法，就可以创建一个状态栏，随后返回一个状态栏对象，然后用showMessage()方法显示一些信息。
    2、
    状态栏就是软件的下层显示
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class StatusBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.status()

    def status(self):
        # 创建窗口
        self.setWindowTitle("learn状态栏")
        self.setGeometry(100, 100, 300, 300)
        self.statusBar().showMessage("statusBar由QMainWindow 创建，第一次调用这个方法，就可以创建一个状态栏，随后返回一个状态栏对象，然后用showMessage()方法显示一些信息。")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = StatusBar()
    sys.exit(app.exec_())


