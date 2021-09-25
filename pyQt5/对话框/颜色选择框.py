# -*- coding: utf-8 -*-
# @Time    : 2021/9/25 17:48
# @Author  : B612
# @File    : 颜色选择框.py


"""
    QColorDialog   颜色对话框
    1、先设置frame 的颜色
    2、创建一个btn, connect颜色对话框，将ｂｔｎ选择的clo 重新赋值给frame的背景颜色

"""
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame,
                             QColorDialog, QApplication)
from PyQt5.QtGui import QColor


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        col = QColor(250, 0, 0)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()
        # print(col)  # <PyQt5.QtGui.QColor object at 0x000002599E7953C8>
        # print(col.name)  # <built-in method name of QColor object at 0x0000017547C153C8>
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
