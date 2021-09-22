# -*- coding: utf-8 -*-
# @Time    : 2021/9/22 23:19
# @Author  : B612
# @File    : 对窗口点×关闭的确定.py

import sys
from PyQt5.QtWidgets import QPushButton, QToolTip, QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon

class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGui()

    def initGui(self):
        # 初始化窗体
        self.setWindowTitle("关闭窗口的确认信息demo")
        self.setWindowIcon(QIcon(r"I:\pyqt5_demo\pyQt5\images\love.ico"))
        self.setGeometry(100, 100, 300, 400)
        self.move(100, 200)
        # 添入button关闭控件
        qbtn = QPushButton("close", self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.move(100, 200)
        # 设置提示文本
        self.setToolTip("这是点击关闭button的确认按钮的界面体")
        qbtn.setToolTip("这是关闭界面的按钮")
        self.show()

    # closeEvent(self, a0: QtGui.QCloseEvent) -> None:
    # 所以这是对方法的重写
    def closeEvent(self, event):
        # 设置message box
        reply = QMessageBox.question(self, "Sure??", "Are you sure close the window", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Gui()
    sys.exit(app.exec_())


"""
简易版本，其中closeEvent是对父类方法的重写
import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
"""