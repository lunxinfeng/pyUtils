import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyFirstGUI:
    """第一个GUI界面"""
    def __init__(self):
        # 创建了一个QWidget()对象，它是PyQt5中所有的图形用户界面的基类
        self.window = QWidget()
        self.initUI()

    def initUI(self):
        self.window.setWindowTitle("Hello PyQt5")  # 设置窗口标题


if __name__ == "__main__":
    # 在PyQt5中，每个应用程序都必须实例化一个QApplication()
    app = QApplication([])
    gui = MyFirstGUI()
    gui.window.show()

    # 调用应用程序对象的exec_()方法来运行程序的主循环，并使用sys.exit()方法确保程序能够完美的退出。
    sys.exit(app.exec_())
