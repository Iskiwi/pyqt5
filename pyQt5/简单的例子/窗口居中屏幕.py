import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QDesktopWidget


# 任务：
# 1 实现窗口的居中显示
# 2 相对路径的图片导入
# 3 模仿窗口的居中显示，试着实现close button的居中显示
# 经查阅资料： ../   表示上一级目录
#             ./      当前目录
#             /      根目录


class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.example()

    def example(self):
        # 设置窗口
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("窗口居中")
        # 相对路径的第一种表示
        # self.setWindowIcon(QIcon("./love.ico"))
        # 相对路径的第二种表示
        self.setWindowIcon(QIcon("../images/ta.ico"))
        self.center()
        self.qbtnclose(self.center()[0], self.center()[1])
        self.show()

    def center(self):
        # 窗口的几何大小
        ui_size = self.frameGeometry()  # PyQt5.QtCore.QRect(100, 100, 400, 500)
        # screen 的大小
        screen = QDesktopWidget().screenGeometry()  # # PyQt5.QtCore.QRect(0, 0, 1920, 1080)
        width = ui_size.width()
        height = ui_size.height()

        self.move(int((screen.width() - ui_size.width()) / 2),
                  int((screen.height() - ui_size.height()) / 2))
        return width, height

    def qbtnclose(self, width, height):
        # button居中于窗口
        qbtn = QPushButton("close", self)
        qbtn.resize(50, 30)
        qbtn.clicked.connect(QApplication.instance().quit)
        # print(type(width))
        # print(width)
        # print(type(qbtn.width()))
        # print(qbtn.width())
        # print(qbtn.size())
        # print(type(screen-qbtn.width()))   unsupported operand type(s) for -: 'QRect' and 'int'

        # qbtn.move(int(width-qbtn.width()/2),
        #           int(height-qbtn.height()/2))
        # qbtn.move(int(width/2),
        #           int(height/2))
        qbtn.move(150, 200)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    UI = Gui()
    sys.exit(app.exec_())
