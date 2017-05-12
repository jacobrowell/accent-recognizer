import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import qtawesome as qta
import os


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # define widgets
        self.screen_1 = QWidget(self)
        self.screen_2 = QWidget(self)
        self.screen_3 = QWidget(self)
        self.screen_4 = QWidget(self)
        self.load_file = None
        self.method_select = None
        self.method_proceed = None
        self.spinner = None
        self.status = None
        self.accent_label = None
        self.result_text = None
        self.finish_button = None

        self.width = 500
        self.height = 300

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Accent recognition system")

        self.screen_1.setFixedSize(self.width, self.height)
        self.screen_2.setFixedSize(self.width, self.height)
        self.screen_3.setFixedSize(self.width, self.height)
        self.screen_4.setFixedSize(self.width, self.height)

        self.screen_2.setVisible(False)
        self.screen_3.setVisible(False)
        self.screen_4.setVisible(False)

        # screen 1 setup

        self.load_file = QPushButton("Load file", self.screen_1)
        self.load_file.setMinimumHeight(50)
        self.load_file.setMinimumWidth(160)
        self.load_file.clicked.connect(self.load_audio)

        v1 = QVBoxLayout()
        h1 = QHBoxLayout()
        h1.addStretch()
        h1.addWidget(self.load_file)
        h1.addStretch()
        v1.addLayout(h1)
        self.screen_1.setLayout(v1)

        # screen 2 setup

        self.method_select = QComboBox(self.screen_2)
        self.method_select.addItem("MFCC-NN")
        self.method_select.addItem("LPCC-NN")
        self.method_select.addItem("MFCC-GMM")
        self.method_select.addItem("LPCC-GMM")
        self.method_select.addItem("MFCC-HMM")
        self.method_select.addItem("LPCC-HMM")

        self.method_proceed = QPushButton("Proceed", self.screen_2)
        self.method_proceed.clicked.connect(self.recognize_audio)

        h2 = QHBoxLayout()
        v2 = QVBoxLayout()
        v2.addStretch()
        v2.addWidget(self.method_select)
        v2.addWidget(self.method_proceed)
        v2.addStretch()
        h2.addStretch()
        h2.addLayout(v2)
        h2.addStretch()
        self.screen_2.setLayout(h2)

        # screen 3 setup

        self.spinner = QPushButton()
        spin_icon = qta.icon("fa.spinner", animation=qta.Spin(self.spinner))
        self.spinner.setIcon(spin_icon)
        self.spinner.setFlat(True)
        self.spinner.setIconSize(QSize(64, 64))
        self.status = QLabel("recognizing...")

        h3 = QHBoxLayout()
        v3 = QVBoxLayout()
        v3.addStretch()
        v3.addWidget(self.spinner)
        v3.addWidget(self.status)
        v3.addStretch()
        h3.addStretch()
        h3.addLayout(v3)
        h3.addStretch()
        self.screen_3.setLayout(h3)

        # screen 4 setup
        self.accent_label = QLabel("Accent:")
        self.accent_label.setAlignment(Qt.AlignCenter)
        f = self.accent_label.font()
        f.setBold(True)
        self.accent_label.setFont(f)
        self.result_text = QLabel("RU\t\t0.8")
        self.result_text.setAlignment(Qt.AlignCenter)
        f = self.result_text.font()
        f.setPointSize(24)
        self.result_text.setFont(f)
        self.finish_button = QPushButton("Done")
        self.finish_button.clicked.connect(self.close)

        h4 = QHBoxLayout()
        v4 = QVBoxLayout()
        v4.addStretch()
        v4.addWidget(self.accent_label)
        v4.addWidget(self.result_text)
        v4.addWidget(self.finish_button)
        v4.addStretch()
        h4.addStretch()
        h4.addLayout(v4)
        h4.addStretch()
        self.screen_4.setLayout(h4)

        self.setFixedSize(self.width, self.height)
        r = self.geometry()
        r.moveCenter(QApplication.desktop().availableGeometry().center())
        self.setGeometry(r)

        self.show()

    def proceed_to_2(self):
        self.screen_1.setVisible(False)
        self.screen_2.setVisible(True)

    def proceed_to_3(self):
        self.screen_2.setVisible(False)
        self.screen_3.setVisible(True)

    def proceed_to_4(self):
        self.screen_3.setVisible(False)
        self.screen_4.setVisible(True)

    def load_audio(self):
        print "loading file..."
        file_dialog = QFileDialog(self)
        file_name = file_dialog.getOpenFileName(self, "Select audio", os.path.expanduser('~'), "*.wav")[0]
        print file_name
        if len(file_name) > 0:
            self.proceed_to_2()
        else:
            alert = QMessageBox()
            alert.setText("Select a *.wav file")
            alert.exec_()

    def recognize_audio(self):
        method = self.method_select.currentText()
        if method != "MFCC-NN":
            alert = QMessageBox()
            alert.setText("The method is not supported yet")
            alert.exec_()
            self.method_select.setCurrentIndex(0)
        else:
            print "recognizing..."
            self.proceed_to_3()
            t = QTimer()
            t.singleShot(3000, self.proceed_to_4)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
