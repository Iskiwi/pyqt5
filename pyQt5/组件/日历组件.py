# -*- coding: utf-8 -*-
# @Time    : 2021/10/3 22:42
# @Author  : B612
# @File    : 日历组件.py

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QCalendarWidget, QLabel
from PyQt5.QtCore import QDate

"""
    例子展示一个日历组件和标签组件。功能是日历中选择的日期会显示在标签组件中。
"""


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        date = cal.selectedDate()  # 在日历上寻找日期，显示在标签上
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())