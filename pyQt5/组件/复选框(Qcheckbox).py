# -*- coding: utf-8 -*-
# @Time    : 2021/10/3 10:59
# @Author  : B612
# @File    : 复选框(Qcheckbox).py

import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt

"""
    cb是复选框
    cb.stateChanged.connect(self.changeTitle)
"""


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()  # 使复选框默认被选中
        # 我们需要设置窗口标题，所以我们必须选中复选框。如果不选中复选框，默认情况下复选框不会被选中所以窗口标题也不会被设置。
        cb.stateChanged.connect(self.changeTitle)
        # 复选框组件的状态会传入changeTitle()
        # 方法的state参数。如果复选框被选中，我们设置窗口标题。否则，我们把窗口标题设置成一个空字符串。

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())