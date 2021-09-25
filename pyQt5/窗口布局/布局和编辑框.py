# -*- coding: utf-8 -*-
# @Time    : 2021/9/25 11:25
# @Author  : B612
# @File    : 布局和编辑框.py

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QGridLayout, QLineEdit, QWidget, QTextEdit, QLabel
from PyQt5.QtGui import QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        self.setWindowTitle("caculatorV3")
        self.adjustSize()
        self.setWindowIcon(QIcon("../images/ta.ico"))

        # textEdit
        TitleEdit = QLineEdit()
        AuthorEdit = QLineEdit()
        PreviwEdit = QTextEdit()

        # label
        Title = QLabel("Title")
        Author = QLabel("Author")
        Preview = QLabel("Preview")

        grid = QGridLayout()
        # 方法一
        littlewidgets = [Title, TitleEdit, Author, AuthorEdit, Preview, PreviwEdit]
        positions = [(i, j) for i in range(3) for j in range(2)]
        for littlewidget, position in zip(littlewidgets, positions):
                grid.addWidget(littlewidget, *position)
        # 方法二
        # grid.addWidget(Title, 1, 1)
        # grid.addWidget(TitleEdit, 1, 2)
        # grid.addWidget(Author, 2, 1)
        # grid.addWidget(AuthorEdit, 2, 2)
        # grid.addWidget(Preview, 3, 1)
        # grid.addWidget(PreviwEdit, 3, 2)

        self.setLayout(grid)
        self.move(150, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
