# -*- coding: utf-8 -*-
# @Time    : 2021/9/25 0:07
# @Author  : B612
# @File    : caculatorV3.py

"""
    Create a window only with the layout ,have no the connect slots and signals
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QGridLayout, QPushButton, QWidget, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        self.setWindowTitle("caculatorV3")
        self.adjustSize()
        self.setWindowIcon(QIcon("../images/ta.ico"))

        # GridLayout
        Grid = QGridLayout()
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        position = [(i, j) for i in range(5) for j in range(4)]
        # print(position)
        for pos, name in zip(position, names):
            # print(pos, name)
            if name == "":
                continue
            button = QPushButton(name)
            # print(*position)
            Grid.addWidget(button, *pos)

        vbox = QVBoxLayout()
        textEdit = QTextEdit()
        vbox.addWidget(textEdit)
        vbox.addLayout(Grid)

        self.setLayout(vbox)
        self.move(150, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
