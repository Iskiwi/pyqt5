# -*- coding: utf-8 -*-
# @Time    : 2021/9/20 20:35
# @Author  : B612
# @File    : 提示文本.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QToolTip
# import PyQt5.Qtcore
from PyQt5.QtGui import QIcon, QFont


class Tooltip(QWidget):
    def __init__(self):
        super().__init__()
        self.tooltip()

    def tooltip(self):
        # 设置窗口
        self.setWindowTitle("设置提示文本")
        self.setWindowIcon(QIcon(r"I:\pyqt5_demo\pyQt5\images\ta....ico"))
        self.setGeometry(100, 100, 400, 500)
        # 设置button
        btn = QPushButton("close button", self)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        # 设置提示文本, 分别给窗口和button 设置提示文本
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')  # 一种富文本写法
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # tip 是实例化的窗口
    tip = Tooltip()
    sys.exit(app.exec_())

