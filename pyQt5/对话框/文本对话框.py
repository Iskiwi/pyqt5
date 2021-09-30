# -*- coding: utf-8 -*-
# @Time    : 2021/9/25 17:45
# @Author  : B612
# @File    : 文本对话框.py

"""
    创建一个窗口， 中间设置一个编辑文本，设置一个菜单栏，加上一个open的功能，将选择的文件和窗口中心联系。
"""

import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('../简单的例子/love.ico'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        # print(fname)  # ('D:/量化.md', 'All Files (*)')
        # getOpenFileName 第三个参数是默认打开的路径
        # /home 是桌面

        if fname[0]:
            f = open(fname[0], 'r', encoding="utf-8")

            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())