# -*- coding: utf-8 -*-
# @Time    : 2021/9/24 11:34
# @Author  : B612
# @File    : 菜单工具状态栏.py

"""
This program create a window with menubar，statusbar and toolbar and a central widget.
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, qApp, QAction, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class Exceple(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        # 窗口
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle("menu&status&tool bar")
        self.setWindowIcon(QIcon("../images/ta.ico"))
        # 设置动作对象
        action = QAction(QIcon("./520.jpg"), "&File", self)
        action.setShortcut("Ctrl+F")
        # triggered 触发的意思
        # 第一种关闭窗口
        # action.triggered.connect(qApp.quit)
        action.triggered.connect(QCoreApplication.instance().quit)
        # 第二种关闭窗口

        # menubar
        menubar = self.menuBar()
        filemenu = menubar.addMenu("&File")
        filemenu.addAction(action)

        # statusbar
        self.statusBar().showMessage("statusbar 由QMainWindow创建")
        self.statusBar().setToolTip("这是状态栏")

        # toolbar
        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(action)

        # 加一个textedit部件
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Exceple()
    sys.exit(app.exec_())
