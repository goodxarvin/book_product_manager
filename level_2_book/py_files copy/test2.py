import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from delete_book import Ui_delete_book

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(870, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.open_delete_window_button = QtWidgets.QPushButton("باز کردن پنجره حذف", self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.open_delete_window_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.open_delete_window_button.setFont(font)
        self.open_delete_window_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.open_delete_window_button.setObjectName("open_delete_window_button")
        self.gridLayout_2.addWidget(self.open_delete_window_button, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.open_delete_window_button.clicked.connect(self.open_delete_window)

    def open_delete_window(self):
        self.delete_window = Ui_delete_book()
        self.delete_window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())