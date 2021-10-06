# -*- coding: utf-8 -*-
# @Time    : 2021/10/6 20:08
# @Author  : B612
# @File    : 04-单行文本编辑框常用方法.py

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator, QFont
from PyQt5.QtCore import Qt

"""
    e1  四位数的Int验证器, 右对齐，修改了字体
    e2  小数点后两位的float
    e3  setInputMask 掩码
    e4  e4.textChanged[str].connect(text_changed) 常用方法【1】
    e5  setechomode 密码的显示 和悬浮的文本  常用方法 【2】
    e6  setReadonly 
    
"""


class LineEditDemo(QWidget):
    def __init__(self, parent=None):
        super(LineEditDemo, self).__init__(parent)
        Form = QFormLayout()
        self.setLayout(Form)
        e1 = QLineEdit()
        e1.setValidator(QIntValidator())
        e1.setMaxLength(4)
        e1.setAlignment(Qt.AlignRight)  # 文本编辑框中的文字从右边开始显示
        e1.setFont(QFont("Arial", 20))
        e2 = QLineEdit()
        e2.setValidator(QDoubleValidator(0.99, 99.99, 2))
        Form.addRow("Integer validator", e1)
        Form.addRow("Double validator", e2)
        e3 = QLineEdit()
        # 设置掩码, Mask （面具，隐藏）
        e3.setInputMask("+99-9999-999999")
        Form.addRow("Input Mask", e3)
        e4 = QLineEdit()
        e4.textChanged[str].connect(text_changed)
        Form.addRow("Text changed", e4)
        e5 = QLineEdit()
        e5.setEchoMode(QLineEdit.Password)
        e5.setPlaceholderText("Password")
        e5.editingFinished.connect(enterpress)
        Form.addRow("Password", e5)

        e6 = QLineEdit("PyQt5 GUI")
        e6.setReadOnly(True)
        # 必须要有参数
        Form.addRow("Read only", e6)


def text_changed(text):
    print("输入的内容为："+text)


def enterpress():
    print("已输入值")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = LineEditDemo()
    ex.show()
    sys.exit(app.exec_())