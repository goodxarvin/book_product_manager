from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1041, 810)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_Author_2 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_Author_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_Author_2.setSizePolicy(sizePolicy)
        self.lineEdit_Author_2.setInputMask("")
        self.lineEdit_Author_2.setText("")
        self.lineEdit_Author_2.setObjectName("lineEdit_Author_2")
        self.gridLayout.addWidget(self.lineEdit_Author_2, 0, 0, 1, 1)
        self.lineEdit_Author = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_Author.sizePolicy().hasHeightForWidth())
        self.lineEdit_Author.setSizePolicy(sizePolicy)
        self.lineEdit_Author.setInputMask("")
        self.lineEdit_Author.setText("")
        self.lineEdit_Author.setObjectName("lineEdit_Author")
        self.gridLayout.addWidget(self.lineEdit_Author, 0, 1, 1, 1)
        self.lineEdit_Author_3 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_Author_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_Author_3.setSizePolicy(sizePolicy)
        self.lineEdit_Author_3.setInputMask("")
        self.lineEdit_Author_3.setText("")
        self.lineEdit_Author_3.setObjectName("lineEdit_Author_3")
        self.gridLayout.addWidget(self.lineEdit_Author_3, 1, 0, 1, 1)
        self.lineEdit_ISBN = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_ISBN.sizePolicy().hasHeightForWidth())
        self.lineEdit_ISBN.setSizePolicy(sizePolicy)
        self.lineEdit_ISBN.setInputMask("")
        self.lineEdit_ISBN.setText("")
        self.lineEdit_ISBN.setObjectName("lineEdit_ISBN")
        self.gridLayout.addWidget(self.lineEdit_ISBN, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_view_all = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.view_all())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_view_all.sizePolicy().hasHeightForWidth())
        self.pushButton_view_all.setSizePolicy(sizePolicy)
        self.pushButton_view_all.setObjectName("pushButton_view_all")
        self.gridLayout_4.addWidget(self.pushButton_view_all, 0, 0, 1, 1)
        self.pushButton_update_book = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_update_book.sizePolicy().hasHeightForWidth())
        self.pushButton_update_book.setSizePolicy(sizePolicy)
        self.pushButton_update_book.setObjectName("pushButton_update_book")
        self.gridLayout_4.addWidget(self.pushButton_update_book, 3, 0, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy)
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout_4.addWidget(self.pushButton_close, 5, 0, 1, 1)
        self.pushButton_add_book = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_add_book.sizePolicy().hasHeightForWidth())
        self.pushButton_add_book.setSizePolicy(sizePolicy)
        self.pushButton_add_book.setObjectName("pushButton_add_book")
        self.gridLayout_4.addWidget(self.pushButton_add_book, 2, 0, 1, 1)
        self.pushButton_delete_book = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_delete_book.sizePolicy().hasHeightForWidth())
        self.pushButton_delete_book.setSizePolicy(sizePolicy)
        self.pushButton_delete_book.setObjectName("pushButton_delete_book")
        self.gridLayout_4.addWidget(self.pushButton_delete_book, 4, 0, 1, 1)
        self.pushButton_search_book = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_search_book.sizePolicy().hasHeightForWidth())
        self.pushButton_search_book.setSizePolicy(sizePolicy)
        self.pushButton_search_book.setObjectName("pushButton_search_book")
        self.gridLayout_4.addWidget(self.pushButton_search_book, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 1, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1041, 26))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        def view_all(self):
            sqlite3.connect("sql.db")

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "library_control"))
        self.lineEdit_Author_2.setPlaceholderText(
            _translate("mainWindow", "Title"))
        self.lineEdit_Author.setPlaceholderText(
            _translate("mainWindow", "Author"))
        self.lineEdit_Author_3.setPlaceholderText(
            _translate("mainWindow", "Year"))
        self.lineEdit_ISBN.setPlaceholderText(_translate("mainWindow", "ISNB"))
        self.pushButton_view_all.setText(_translate("mainWindow", "View All"))
        self.pushButton_update_book.setText(
            _translate("mainWindow", "update book"))
        self.pushButton_close.setText(_translate("mainWindow", "close"))
        self.pushButton_add_book.setText(_translate("mainWindow", "add book"))
        self.pushButton_delete_book.setText(
            _translate("mainWindow", "delete book"))
        self.pushButton_search_book.setText(
            _translate("mainWindow", "search book"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
