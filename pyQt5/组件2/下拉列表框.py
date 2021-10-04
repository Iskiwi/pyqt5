# -*- coding: utf-8 -*-
# @Time    : 2021/10/4 9:36
# @Author  : B612
# @File    : 下拉列表框.py

import sys
from PyQt5.QtWidgets import (QWidget, QComboBox,  QLabel, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel("Ubuntu", self)
        self.lbl.move(20, 50)
        combox = QComboBox(self)
        combox.move(20, 100)
        combox.addItem("Ubuntu")
        combox.addItem("Mandriva")
        combox.addItem("Fedora")
        combox.addItem("Arch")
        combox.addItem("Gentoo")
        combox.activated[str].connect(self.show_in_lbl)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('下拉列表框')
        self.show()

    def show_in_lbl(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())