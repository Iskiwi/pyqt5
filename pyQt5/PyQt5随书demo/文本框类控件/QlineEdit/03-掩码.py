# -*- coding: utf-8 -*-
# @Time    : 2021/10/6 20:01
# @Author  : B612
# @File    : 03-掩码.py

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QFormLayout
from PyQt5.Qt import QRegExp
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        e1 = QLineEdit(self)
        e2 = QLineEdit(self)
        e3 = QLineEdit(self)
        e4 = QLineEdit(self)
        e1.setInputMask("99-9999-999999")
        e2.setInputMask("HH:HH:HH:HH:HH:HH;_")
        e3.setInputMask("0000-00-00")
        e4.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")

        FormLayout = QFormLayout()
        FormLayout.addRow("数字掩码", e1)
        FormLayout.addRow("MAC掩码", e2)
        FormLayout.addRow("日期掩码", e3)
        FormLayout.addRow("许可证掩码", e4)
        self.setLayout(FormLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


