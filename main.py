import sys
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)
    win = QWidget()
    lab = QLabel(win)
    lab.setText("Hello")
    win.setGeometry(100, 100, 200, 50)
    lab.move(50, 20)
    win.setWindowTitle("i'm a window")
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()
