from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_delete_book(object):
    def setupUi(self, delete_book):
        delete_book.setObjectName("delete_book")
        delete_book.resize(801, 401)
        delete_book.setStyleSheet("background-color: rgb(154, 154, 154);")
        self.gridLayout = QtWidgets.QGridLayout(delete_book)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_lineEdit = QtWidgets.QGridLayout()
        self.gridLayout_lineEdit.setObjectName("gridLayout_lineEdit")
        self.pushButton_start_search = QtWidgets.QPushButton(delete_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_start_search.sizePolicy().hasHeightForWidth())
        self.pushButton_start_search.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_start_search.setFont(font)
        self.pushButton_start_search.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_start_search.setStyleSheet("background-color: green;\n"
                                                   "color: white;\n"
                                                   "border-color: white;\n"
                                                   "border-width: 5px;\n"
                                                   "border-radius: 30px;\n"
                                                   "border-style: solid;\n"
                                                   "padding: 10px;")
        self.pushButton_start_search.setObjectName("pushButton_start_search")
        self.gridLayout_lineEdit.addWidget(
            self.pushButton_start_search, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(delete_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: white;\n"
                                    "border-color: black;\n"
                                    "border-width: 5px;\n"
                                    "border-radius: 30px;\n"
                                    "padding: 10px;\n"
                                    "border-style: solid;")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_lineEdit.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.gridLayout_lineEdit.setColumnStretch(0, 1)
        self.gridLayout_lineEdit.setColumnStretch(1, 2)
        self.gridLayout.addLayout(self.gridLayout_lineEdit, 0, 0, 1, 1)
        self.gridLayout_list_widget = QtWidgets.QGridLayout()
        self.gridLayout_list_widget.setObjectName("gridLayout_list_widget")
        self.listWidget_show_found_books = QtWidgets.QListWidget(delete_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.listWidget_show_found_books.sizePolicy().hasHeightForWidth())
        self.listWidget_show_found_books.setSizePolicy(sizePolicy)
        self.listWidget_show_found_books.setLayoutDirection(
            QtCore.Qt.RightToLeft)
        self.listWidget_show_found_books.setStyleSheet("background-color: white;\n"
                                                       "border-color: black;\n"
                                                       "border-width: 5px;\n"
                                                       "border-radius: 30px;\n"
                                                       "padding: 10px;\n"
                                                       "border-style: solid;")
        self.listWidget_show_found_books.setObjectName(
            "listWidget_show_found_books")
        self.gridLayout_list_widget.addWidget(
            self.listWidget_show_found_books, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_list_widget, 1, 0, 1, 1)
        self.gridLayout_buttons_p1 = QtWidgets.QGridLayout()
        self.gridLayout_buttons_p1.setObjectName("gridLayout_buttons_p1")
        self.pushButton_select_book = QtWidgets.QPushButton(delete_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_select_book.sizePolicy().hasHeightForWidth())
        self.pushButton_select_book.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_select_book.setFont(font)
        self.pushButton_select_book.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_select_book.setStyleSheet("background-color: green;\n"
                                                  "color: white;\n"
                                                  "border-color: white;\n"
                                                  "border-width: 5px;\n"
                                                  "border-radius: 30px;\n"
                                                  "border-style: solid;\n"
                                                  "padding: 10px;")
        self.pushButton_select_book.setObjectName("pushButton_select_book")
        self.gridLayout_buttons_p1.addWidget(
            self.pushButton_select_book, 0, 0, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(delete_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_close.setStyleSheet("background-color: rgb(170, 0, 0);\n"
                                            "color: white;\n"
                                            "border-color: white;\n"
                                            "border-width: 5px;\n"
                                            "border-radius: 30px;\n"
                                            "border-style: solid;\n"
                                            "padding: 10px;")
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout_buttons_p1.addWidget(self.pushButton_close, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_buttons_p1, 2, 0, 1, 1)
        self.gridLayout_label = QtWidgets.QGridLayout()
        self.gridLayout_label.setObjectName("gridLayout_label")
        self.label_show_approve_book = QtWidgets.QLabel(delete_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_show_approve_book.sizePolicy().hasHeightForWidth())
        self.label_show_approve_book.setSizePolicy(sizePolicy)
        self.label_show_approve_book.setStyleSheet("background-color: rgb(154, 154, 154);\n"
                                                   "border-color: black;\n"
                                                   "border-width: 5px;\n"
                                                   "border-radius: 30px;\n"
                                                   "padding: 10px;\n"
                                                   "border-style: solid;")
        self.label_show_approve_book.setText("")
        self.label_show_approve_book.setObjectName("label_show_approve_book")
        self.gridLayout_label.addWidget(
            self.label_show_approve_book, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_label, 3, 0, 1, 1)
        self.gridLayout_buttons_p2 = QtWidgets.QGridLayout()
        self.gridLayout_buttons_p2.setObjectName("gridLayout_buttons_p2")
        self.pushButton_approve_book = QtWidgets.QPushButton(delete_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_approve_book.sizePolicy().hasHeightForWidth())
        self.pushButton_approve_book.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_approve_book.setFont(font)
        self.pushButton_approve_book.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_approve_book.setStyleSheet("background-color: green;\n"
                                                   "color: white;\n"
                                                   "border-color: white;\n"
                                                   "border-width: 5px;\n"
                                                   "border-radius: 30px;\n"
                                                   "border-style: solid;\n"
                                                   "padding: 10px;")
        self.pushButton_approve_book.setObjectName("pushButton_approve_book")
        self.gridLayout_buttons_p2.addWidget(
            self.pushButton_approve_book, 0, 0, 1, 1)
        self.pushButton_return_to_p1 = QtWidgets.QPushButton(delete_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_return_to_p1.sizePolicy().hasHeightForWidth())
        self.pushButton_return_to_p1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_return_to_p1.setFont(font)
        self.pushButton_return_to_p1.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_return_to_p1.setStyleSheet("background-color: rgb(170, 0, 0);\n"
                                                   "color: white;\n"
                                                   "border-color: white;\n"
                                                   "border-width: 5px;\n"
                                                   "border-radius: 30px;\n"
                                                   "border-style: solid;\n"
                                                   "padding: 10px;")
        self.pushButton_return_to_p1.setObjectName("pushButton_return_to_p1")
        self.gridLayout_buttons_p2.addWidget(
            self.pushButton_return_to_p1, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_buttons_p2, 4, 0, 1, 1)

        self.retranslateUi(delete_book)
        QtCore.QMetaObject.connectSlotsByName(delete_book)

    def retranslateUi(self, delete_book):
        _translate = QtCore.QCoreApplication.translate
        delete_book.setWindowTitle(_translate("delete_book", "delete_book"))
        self.pushButton_start_search.setText(
            _translate("delete_book", "شروع جستوجو"))
        self.lineEdit.setPlaceholderText(_translate(
            "delete_book", "لطفا کلمه ای را برای پیدا کردن کتابی که می خواهید حذف کنید ایتجا وارد کنید"))
        self.pushButton_select_book.setText(
            _translate("delete_book", "انتخاب کتاب"))
        self.pushButton_close.setText(_translate("delete_book", "بستن"))
        self.pushButton_approve_book.setText(
            _translate("delete_book", "تایید و حدف کتاب"))
        self.pushButton_return_to_p1.setText(
            _translate("delete_book", "برگشت به صفحه اول"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    delete_book = QtWidgets.QWidget()
    ui = Ui_delete_book()
    ui.setupUi(delete_book)
    delete_book.show()
    sys.exit(app.exec_())
