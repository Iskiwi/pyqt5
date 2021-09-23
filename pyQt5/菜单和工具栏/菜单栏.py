# -*- coding: utf-8 -*-
# @Time    : 2021/9/23 18:00
# @Author  : B612
# @File    : 菜单栏.py

"""
create a menubar with a exit action
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu()

    def menu(self):
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle("Menubar")
        self.setWindowIcon(QIcon("../images/ta.ico"))

        # 创建菜单栏
        exitAction = QAction(QIcon("520.jpg"), "&Exit", self)
        exitAction.setShortcut("Ctrl+x")
        # 设置状态提示
        exitAction.setStatusTip("ExitApp")
        # 设置提示文本
        # exitAction.setToolTip("这是我设置的关闭动作的提示")
        # 上面都是我们创建的动作信号
        # 下面是我们连接的槽
        exitAction.triggered.connect(qApp.quit)

        self.statusBar().showMessage(
            "菜单栏有一个exit 有快捷键，有图标")
        menubar = self.menuBar()
        filemenu = menubar.addMenu("&File")
        filemenu.addAction(exitAction)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


