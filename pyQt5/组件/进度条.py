# -*- coding: utf-8 -*-
# @Time    : 2021/10/3 20:53
# @Author  : B612
# @File    : 进度条.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer

"""
    例子中有一个横向进度条和一个按钮。按钮控制滑块条的开始和停止.
"""


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        # 用计时器对象来激活进度条。
        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()

    def timerEvent(self, e):
        # print(e)  # <PyQt5.QtCore.QTimerEvent object at 0x000001C401B1A280>
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():  # 暂停的时候
            self.timer.stop()
            self.btn.setText('Start')
        else:  # 点击为了开始或者继续的时候执行
            self.timer.start(100, self)  # 这个方法有两个参数：定时时间和接收定时器事件的对象。
            self.btn.setText('Stop')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())