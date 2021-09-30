# -*- coding: utf-8 -*-
# @Time    : 2021/9/26 0:06
# @Author  : B612
# @File    : 字体对话框.py

import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
                             QSizePolicy, QLabel, QFontDialog, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        self.lbl = QLabel("这是测试字体对话框选择的文本")
        self.lbl.setSizePolicy(QSizePolicy.Fixed,
                               QSizePolicy.Fixed)

        btn = QPushButton("select the font", self)
        btn.clicked.connect(self.selectFont)
        btn.move(400, 400)

        vbox.addWidget(self.lbl)
        vbox.addWidget(btn)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('字体对话框')
        self.show()

    def selectFont(self):
        Font, ok = QFontDialog.getFont()
        # print(Font)  # (<PyQt5.QtGui.QFont object at 0x000001F153E0AEB0>, True)
        if ok:
            self.lbl.setFont(Font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
