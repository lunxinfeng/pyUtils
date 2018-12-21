import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, pyqtSignal, QBasicTimer, QFile
from gui.boot import Ui_Form
from gui.helper.QSSHelper import QSSHelper
from gui.home_controller import Home_Window


class MyWindow(QWidget, Ui_Form):
    close_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        # 设置窗体无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 设置背景透明
        # self.setAttribute(Qt.WA_TranslucentBackground)

        self.step = 0
        # 创建一个计时器，20ms一跳，触发timerEvent方法
        self.timer = QBasicTimer()
        self.timer.start(20, self)

    def timerEvent(self, *args, **kwargs):
        if self.step >= 100:
            self.timer.stop()
            return
        self.step = self.step + 1
        self.progressBar.setValue(self.step)
        if self.progressBar.value() >= 100:
            self.close_signal.emit()
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    qss = "./ui.css"
    app.setStyleSheet(open(qss).read())

    home_window = Home_Window()
    myWin.close_signal.connect(home_window.open)

    # file = QFile('css.qss')
    # file.open(QFile.ReadOnly)
    # styleSheet = file.readAll()
    # styleSheet = unicode(styleSheet, encoding='utf8')
    # app.setStyleSheet(styleSheet)

    myWin.show()
    sys.exit(app.exec_())
