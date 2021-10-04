# -*- coding: utf-8 -*-
# @Time    : 2021/10/4 9:18
# @Author  : B612
# @File    : 单行文本编辑框.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit

"""
    例子中，在单行文本编辑框中编辑的文本会同步到标签中
"""


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        self.lbl = QLabel(self)
        lineEdit = QLineEdit(self)
        self.lbl.move(20, 20)
        lineEdit.move(20, 80)
        lineEdit.textChanged[str].connect(self.showLine)
        self.setGeometry(120, 120, 200, 200)
        self.setWindowTitle("LineEdit")
        self.show()

    def showLine(self, text):
        self.lbl.setText(str(text))
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())