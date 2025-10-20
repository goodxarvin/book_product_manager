from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import re


class newBook:
    def __init__(
            self, new_title=None, new_author=None, new_ISBN=None, new_year=None):
        self.new_title = new_title
        self.new_author = new_author
        self.new_ISBN = new_ISBN
        self.new_year = new_year

    def return_list(self):
        return [self.new_title, self.new_author, self.new_ISBN, self.new_year]


class Ui_edit_book(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, edit_book):
        edit_book.setObjectName("edit_book")
        edit_book.resize(960, 400)
        self.gridLayout_window = QtWidgets.QGridLayout(edit_book)
        self.gridLayout_window.setObjectName("gridLayout_window")
        self.gridLayout_label = QtWidgets.QGridLayout()
        self.gridLayout_label.setObjectName("gridLayout_label")

        self.listWidget = QtWidgets.QListWidget(edit_book)
        font = QtGui.QFont()
        self.listWidget.setStyleSheet("color: black;\n"
                                      "background-color: white;\n"
                                      "border-radius: 30px;\n"
                                      "border-color: grey;\n"
                                      "border-width: 5px;\n"
                                      "border-style: solid;\n"
                                      "padding: 20px;\n")
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_checkBoxes = QtWidgets.QGridLayout()
        self.gridLayout_window.addWidget(self.listWidget, 2, 0, 1, 1)

        self.lineEdit_search = QtWidgets.QLineEdit(edit_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.lineEdit_search.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "border-color: black;\n"
                                           "border-style: solid;\n"
                                           "border-width: 5;\n"
                                           "border-radius: 30px;\n"
                                           "padding: 20px;")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_search.setFont(font)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_search.sizePolicy().hasHeightForWidth())
        self.lineEdit_search.setSizePolicy(sizePolicy)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.gridLayout_label.addWidget(self.lineEdit_search, 0, 5, 1, 1)

        self.label_errors = QtWidgets.QLabel(edit_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_errors.sizePolicy().hasHeightForWidth())
        self.label_errors.setSizePolicy(sizePolicy)
        self.label_errors.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_errors.setFont(font)
        self.label_errors.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 30px;\n"
                                        "border-color: black;\n"
                                        "border-width: 5px;\n"
                                        "border-style: solid;\n"
                                        "padding: 10px;")
        self.label_errors.setObjectName("label_errors")
        self.label_errors.hide()

        self.label = QtWidgets.QLabel(edit_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                 "border-radius: 30px;\n"
                                 "border-color: black;\n"
                                 "border-width: 5px;\n"
                                 "border-style: solid;\n"
                                 "padding: 10px;")
        self.label.setObjectName("label")
        self.label.hide()
        self.gridLayout_label.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_window.addLayout(self.gridLayout_label, 0, 0, 1, 1)
        self.gridLayout_checkBoxes.setObjectName("gridLayout_checkBoxes")

        self.pushButton_approve_search = QtWidgets.QPushButton(
            edit_book)
        self.pushButton_approve_search.pressed.connect(self.start_search)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_approve_search.sizePolicy().hasHeightForWidth())
        self.pushButton_approve_search.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.pushButton_approve_search.setFont(font)
        self.pushButton_approve_search.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_approve_search.setStyleSheet("background-color: green;\n"
                                                     "color: white;\n"
                                                     "border-color: grey;\n"
                                                     "border-width: 5px;\n"
                                                     "padding: 20px;\n"
                                                     "border-style: solid;\n"
                                                     "border-radius: 30px;\n")
        self.pushButton_approve_search.setObjectName(
            "pushButton_approve_search")
        self.gridLayout_label.addWidget(
            self.pushButton_approve_search, 0, 0, 1, 2)

        self.pushButton_approve_book = QtWidgets.QPushButton(
            edit_book, clicked=lambda: self.approve_book_clicked())
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
                                                   "border-color: grey;\n"
                                                   "border-width: 5px;\n"
                                                   "padding: 20px;\n"
                                                   "border-style: solid;\n"
                                                   "border-radius: 30px;\n")
        self.pushButton_approve_book.setObjectName(
            "pushButton_approve_book")
        self.gridLayout_checkBoxes.addWidget(
            self.pushButton_approve_book, 6, 0, 1, 1)

        self.pushButton_approve_changing = QtWidgets.QPushButton(
            edit_book, clicked=lambda: self.approve_changing_clicked())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_approve_changing.sizePolicy().hasHeightForWidth())
        self.pushButton_approve_changing.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_approve_changing.setFont(font)
        self.pushButton_approve_changing.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_approve_changing.setStyleSheet("background-color: green;\n"
                                                       "color: white;\n"
                                                       "border-color: grey;\n"
                                                       "border-width: 5px;\n"
                                                       "padding: 10px;\n"
                                                       "border-style: solid;\n"
                                                       "border-radius: 30px;\n")
        self.pushButton_approve_changing.setObjectName(
            "pushButton_approve_changing")
        self.pushButton_approve_changing.hide()
        self.gridLayout_checkBoxes.addWidget(
            self.pushButton_approve_changing, 6, 0, 1, 1)

        self.pushButton_approve_finally = QtWidgets.QPushButton(
            edit_book, clicked=lambda: self.click_approve_finally())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_approve_finally.sizePolicy().hasHeightForWidth())
        self.pushButton_approve_finally.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_approve_finally.setFont(font)
        self.pushButton_approve_finally.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_approve_finally.setStyleSheet("background-color: green;\n"
                                                      "border-color: grey;\n"
                                                      "border-width: 5px;\n"
                                                      "padding: 10px;\n"
                                                      "border-style: solid;\n"
                                                      "color: white;\n"
                                                      "border-radius: 30px;")
        self.pushButton_approve_finally.setObjectName(
            "pushButton_approve_finally")
        self.gridLayout_checkBoxes.addWidget(
            self.pushButton_approve_finally, 6, 0, 1, 1)
        self.pushButton_approve_finally.hide()

        self.pushButton_back_second = QtWidgets.QPushButton(
            edit_book, clicked=lambda: self.click_back_second())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_back_second.sizePolicy().hasHeightForWidth())
        self.pushButton_back_second.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_back_second.setFont(font)
        self.pushButton_back_second.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_back_second.setStyleSheet("background-color: green;\n"
                                                  "border-color: grey;\n"
                                                  "border-width: 5px;\n"
                                                  "padding: 10px;\n"
                                                  "border-style: solid;\n"
                                                  "color: white;\n"
                                                  "border-radius: 30px;")
        self.pushButton_back_second.setObjectName("pushButton_back_second")
        self.gridLayout_checkBoxes.addWidget(
            self.pushButton_back_second, 6, 1, 1, 1)
        self.pushButton_back_second.hide()

        self.pushButton_close = QtWidgets.QPushButton(
            edit_book)
        self.pushButton_close.pressed.connect(self.click_close)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_close.setStyleSheet("background-color: green;\n"
                                            "border-color: grey;\n"
                                            "border-width: 5px;\n"
                                            "padding: 10px;\n"
                                            "border-style: solid;\n"
                                            "color: white;\n"
                                            "border-radius: 30px;")
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout_checkBoxes.addWidget(
            self.pushButton_close, 6, 4, 1, 1)

        self.pushButton_back_first = QtWidgets.QPushButton(
            edit_book, clicked=lambda: self.click_back_first())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_back_first.sizePolicy().hasHeightForWidth())
        self.pushButton_back_first.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_back_first.setFont(font)
        self.pushButton_back_first.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_back_first.setStyleSheet("background-color: green;\n"
                                                 "border-color: grey;\n"
                                                 "border-width: 5px;\n"
                                                 "padding: 10px;\n"
                                                 "border-style: solid;\n"
                                                 "color: white;\n"
                                                 "border-radius: 30px;")
        self.pushButton_back_first.setObjectName("pushButton_back_first")
        self.gridLayout_checkBoxes.addWidget(
            self.pushButton_back_first, 6, 4, 1, 1)
        self.pushButton_back_first.hide()

        self.checkBox_ISBN = QtWidgets.QCheckBox(edit_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_ISBN.sizePolicy().hasHeightForWidth())
        self.checkBox_ISBN.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_ISBN.setFont(font)
        self.checkBox_ISBN.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_ISBN.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_ISBN.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "padding: 10px;\n"
                                         "border-color: black;\n"
                                         "border-width: 5px;\n"
                                         "border-radius: 30px;\n"
                                         "border-style: solid;")
        self.checkBox_ISBN.setObjectName("checkBox_ISBN")
        self.checkBox_ISBN.hide()
        self.gridLayout_checkBoxes.addWidget(self.checkBox_ISBN, 4, 2, 1, 1)
        self.checkBox_year = QtWidgets.QCheckBox(edit_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_year.sizePolicy().hasHeightForWidth())
        self.checkBox_year.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_year.setFont(font)
        self.checkBox_year.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_year.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border-color: black;\n"
                                         "border-width: 5px;\n"
                                         "padding: 10px;\n"
                                         "border-style: solid;\n"
                                         "border-radius: 30px;")
        self.checkBox_year.setObjectName("checkBox_year")
        self.checkBox_year.hide()
        self.gridLayout_checkBoxes.addWidget(self.checkBox_year, 4, 4, 1, 1)
        self.checkBox_author = QtWidgets.QCheckBox(edit_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_author.sizePolicy().hasHeightForWidth())
        self.checkBox_author.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_author.setFont(font)
        self.checkBox_author.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_author.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_author.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "border-width: 5px;\n"
                                           "border-radius: 30px;\n"
                                           "border-color: black;\n"
                                           "border-style: solid;\n"
                                           "padding: 10px;")
        self.checkBox_author.setObjectName("checkBox_author")
        self.checkBox_author.hide()
        self.gridLayout_checkBoxes.addWidget(self.checkBox_author, 4, 1, 1, 1)
        self.checkBox_title = QtWidgets.QCheckBox(edit_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_title.sizePolicy().hasHeightForWidth())
        self.checkBox_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_title.setFont(font)
        self.checkBox_title.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_title.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "border-color: black;\n"
                                          "border-style: solid;\n"
                                          "border-width: 5;\n"
                                          "border-radius: 30px;\n"
                                          "padding: 20px;")
        self.checkBox_title.setTristate(False)
        self.checkBox_title.setObjectName("checkBox_title")
        self.checkBox_title.hide()
        self.gridLayout_checkBoxes.addWidget(self.checkBox_title, 4, 0, 1, 1)
        self.gridLayout_window.addLayout(
            self.gridLayout_checkBoxes, 4, 0, 1, 1)

        self.lineEdit_year = QtWidgets.QLineEdit(edit_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.lineEdit_year.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border-color: black;\n"
                                         "border-style: solid;\n"
                                         "border-width: 5;\n"
                                         "border-radius: 30px;\n"
                                         "padding: 20px;")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_year.setFont(font)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_year.sizePolicy().hasHeightForWidth())
        self.lineEdit_year.setSizePolicy(sizePolicy)
        self.lineEdit_year.setObjectName("lineEdit_year")
        self.gridLayout_label.addWidget(self.lineEdit_year, 3, 0, 1, 5)
        self.lineEdit_year.hide()

        self.lineEdit_ISBN = QtWidgets.QLineEdit(edit_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.lineEdit_ISBN.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border-color: black;\n"
                                         "border-style: solid;\n"
                                         "border-width: 5;\n"
                                         "border-radius: 30px;\n"
                                         "padding: 20px;")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_ISBN.setFont(font)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_ISBN.sizePolicy().hasHeightForWidth())
        self.lineEdit_ISBN.setSizePolicy(sizePolicy)
        self.lineEdit_ISBN.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_ISBN.setObjectName("lineEdit_ISBN")
        self.gridLayout_label.addWidget(self.lineEdit_ISBN, 2, 0, 1, 5)
        self.lineEdit_ISBN.hide()

        self.lineEdit_title = QtWidgets.QLineEdit(edit_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.lineEdit_title.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "border-color: black;\n"
                                          "border-style: solid;\n"
                                          "border-width: 5;\n"
                                          "border-radius: 30px;\n"
                                          "padding: 20px;")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_title.setFont(font)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_title.sizePolicy().hasHeightForWidth())
        self.lineEdit_title.setSizePolicy(sizePolicy)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.gridLayout_label.addWidget(self.lineEdit_title, 0, 0, 1, 5)
        self.lineEdit_title.hide()

        self.lineEdit_author = QtWidgets.QLineEdit(edit_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.lineEdit_author.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "border-color: black;\n"
                                           "border-style: solid;\n"
                                           "border-width: 5;\n"
                                           "border-radius: 30px;\n"
                                           "padding: 20px;")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_author.setFont(font)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_author.sizePolicy().hasHeightForWidth())
        self.lineEdit_author.setSizePolicy(sizePolicy)
        self.lineEdit_author.setObjectName("lineEdit_author")
        self.gridLayout_label.addWidget(self.lineEdit_author, 1, 0, 1, 5)
        self.lineEdit_author.hide()

        self.message_box_ns = QMessageBox()
        self.message_box_ns.setIcon(QMessageBox.Information)
        self.message_box_ns.setWindowTitle("nothing is chosen...")
        self.message_box_ns.setText(
            "هیچ آیتمی برای تغییر انتخاب نشده , لطفا حداقل یکی از گذینه ها را تیک بزنید")
        self.message_box_ns.setStandardButtons(QMessageBox.Ok)

        self.message_box_em = QMessageBox()
        self.message_box_em.setIcon(QMessageBox.Information)
        self.message_box_em.setWindowTitle("empty entry...")
        self.message_box_em.setStandardButtons(QMessageBox.Ok)

        self.spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.retranslateUi(edit_book)
        QtCore.QMetaObject.connectSlotsByName(edit_book)

        self.gridLayout_window.setRowStretch(0, 2)
        self.gridLayout_window.setRowStretch(1, 0)
        self.gridLayout_window.setRowStretch(2, 3)
        self.gridLayout_window.setRowStretch(3, 0)
        self.gridLayout_window.setRowStretch(4, 2)
        self.server = sqlite3.connect("db_files\\book_database.db")

    def reset_label(self):
        self.label_errors.hide()
        self.gridLayout_window.removeWidget(self.label)

    def show_label_error(self):
        self.gridLayout_window.addWidget(self.label_errors, 1, 0, 1, 1)
        self.label_errors.setStyleSheet("background-color: red;\n"
                                        "border-radius: 30px;\n"
                                        "border-color: red;\n"
                                        "border-width: 5px;\n"
                                        "border-style: solid;\n"
                                        "color: white;\n"
                                        "padding: 10px;")
        self.label_errors.setText(
            "لطفا در کادر بالا کلمه ای برای جستجوی کتاب بنویسید")
        self.label_errors.show()

    def show_label_error_nf(self):
        self.gridLayout_window.addWidget(self.label_errors, 1, 0, 1, 1)
        self.label_errors.setStyleSheet("background-color: red;\n"
                                        "border-radius: 30px;\n"
                                        "border-color: red;\n"
                                        "border-width: 5px;\n"
                                        "border-style: solid;\n"
                                        "color: white;\n"
                                        "padding: 10px;")
        self.label_errors.setText("جستوجوی شما نتیجه ای نداشت")
        self.label_errors.show()

    def show_label_error_Nchosen(self):
        self.gridLayout_window.addWidget(self.label_errors, 3, 0, 1, 1)
        self.label_errors.setStyleSheet("background-color: red;\n"
                                        "border-radius: 30px;\n"
                                        "border-color: red;\n"
                                        "border-width: 5px;\n"
                                        "border-style: solid;\n"
                                        "color: white;\n"
                                        "padding: 10px;")
        self.label_errors.setText("لطفا از لیست بالا یک کتاب را انتخاب کنید")
        self.label_errors.show()

    def fanal_label_success(self):
        self.gridLayout_window.addWidget(self.label_errors, 3, 0, 1, 1)
        self.label_errors.setStyleSheet("background-color: green;\n"
                                        "border-radius: 30px;\n"
                                        "border-color: green;\n"
                                        "border-width: 5px;\n"
                                        "border-style: solid;\n"
                                        "color: white;\n"
                                        "padding: 10px;")
        self.label_errors.setText("تغییر مشخصات با موفقیت انجام شد")
        self.label_errors.show()

    def start_search(self):
        search_key = self.lineEdit_search.text()
        self.book_cursor = self.server.cursor()
        if search_key:
            self.book_cursor.execute(
                "SELECT * FROM Books WHERE id LIKE ? OR title LIKE ? OR author LIKE ? OR isbn LIKE ? OR year_published LIKE ?",
                (f"%{search_key}%", f"%{search_key}%", f"%{search_key}%", f"%{search_key}%", f"%{search_key}%"))
            found_books = self.book_cursor.fetchall()
            if found_books:
                self.listWidget.clear()
                for index, book in enumerate(found_books):
                    self.listWidget.addItem(
                        f"{index+1}--->  نام: {book[1]}, نویسنده: {book[2]}, سال انتشار: {book[4]}\nid: {book[0]}, ISBN: {book[3]}\n")
            else:
                self.show_label_error_nf()
                QtCore.QTimer.singleShot(3000, self.reset_label)
        else:
            self.show_label_error()
            QtCore.QTimer.singleShot(3000, self.reset_label)

    def approve_book_clicked(self):
        try:
            self.label_errors.hide()
            self.chosen = self.listWidget.currentItem()
            if self.chosen:
                self.gridLayout_window.addItem(self.spacerItem, 1, 0, 1, 1)
                self.lineEdit_search.hide()
                self.pushButton_close.hide()
                self.pushButton_approve_book.hide()
                self.listWidget.hide()
                self.pushButton_approve_search.hide()
                self.label.show()
                self.checkBox_title.show()
                self.checkBox_author.show()
                self.checkBox_ISBN.show()
                self.checkBox_year.show()
                self.pushButton_approve_changing.show()
                self.pushButton_back_first.show()
            elif not self.chosen and self.listWidget.count():
                self.show_label_error_Nchosen()
                QtCore.QTimer.singleShot(3000, self.reset_label)
            else:
                self.show_label_error()
                QtCore.QTimer.singleShot(3000, self.reset_label)
        except Exception as e:
            print(e)

    def approve_changing_clicked(self):
        check_title = self.checkBox_title.isChecked()
        check_author = self.checkBox_author.isChecked()
        check_ISBN = self.checkBox_ISBN.isChecked()
        check_year = self.checkBox_year.isChecked()
        show_title = self.lineEdit_title
        show_author = self.lineEdit_author
        show_year = self.lineEdit_year
        show_isbn = self.lineEdit_ISBN
        check_dict = {"title": [check_title, show_title], "author": [check_author, show_author],
                      "isbn": [check_ISBN, show_isbn], "year_published": [check_year, show_year]}
        check_list = list()
        for trues in check_dict:
            if check_dict.get(trues)[0]:
                check_list.append(trues)
                check_dict[trues][1].show()
                self.pushButton_approve_changing.hide()
        if check_list:
            self.checkBox_title.hide()
            self.checkBox_author.hide()
            self.checkBox_year.hide()
            self.checkBox_ISBN.hide()
            self.pushButton_back_first.hide()
            self.label.hide()
            self.pushButton_approve_finally.show()
            self.pushButton_back_second.show()
        else:
            self.message_box_ns.exec_()

    def click_approve_finally(self):
        try:
            new_title = self.lineEdit_title.text()
            new_author = self.lineEdit_author.text()
            new_ISBN = self.lineEdit_ISBN.text()
            new_year = self.lineEdit_year.text()
            title_visibility = self.lineEdit_title.isVisible()
            author_visibility = self.lineEdit_author.isVisible()
            ISBN_visibility = self.lineEdit_ISBN.isVisible()
            year_visibility = self.lineEdit_year.isVisible()
            visibility_list = [
                title_visibility, author_visibility, ISBN_visibility, year_visibility]
            new_book = newBook(new_title, new_author, new_ISBN, new_year)
            list_new_book = new_book.return_list()
            result_list = list(zip(visibility_list, list_new_book))
            empty_str_list = ["تایتل", "نویسنده", "ISBN", "سال انتشار"]
            db_new_items_list = ["title", "author", "isbn", "year_published"]
            all_emptys = []
            new_items = []
            for index_em, empty_check in enumerate(result_list):
                if empty_check[0] and not empty_check[1]:
                    empty_item = empty_str_list[index_em]
                    all_emptys.append(empty_item)
                elif empty_check[0] and empty_check[1]:
                    new_items.append(db_new_items_list[index_em])
            if all_emptys:
                all_emptys_str = ""
                for empty_str in all_emptys:
                    all_emptys_str += f"{empty_str} و "
                all_emptys_str = all_emptys_str[:-3]
                self.message_box_em.setText(
                    f"شما {all_emptys_str} جدید را وارد نکرده اید")
                self.message_box_em.exec_()
            else:
                all_new_lineEdits = []
                all_change_items_str = ""
                list_new_book = [item for item in list_new_book if item]
                for index, sql_code in enumerate(new_items):
                    all_change_items_str += f"{sql_code} = ?, "
                    all_new_lineEdits.append(list_new_book[index])
                title = self.chosen.text()
                book_title = re.search(r"نام:\s*([^,]+)", title)
                str_book_title = book_title.group(1)
                all_new_lineEdits.append(str_book_title)
                all_new_lineEdits = tuple(all_new_lineEdits)
                all_change_items_str = all_change_items_str[:-2] + " "
                self.book_cursor.execute(
                    f"UPDATE Books SET {all_change_items_str} WHERE title = ?", all_new_lineEdits)
                self.server.commit()
                self.fanal_label_success()
                QtCore.QTimer.singleShot(3000, self.reset_label)

        except Exception as e:
            print(e)

    def click_back_first(self):
        self.label.hide()
        self.checkBox_title.hide()
        self.checkBox_author.hide()
        self.checkBox_ISBN.hide()
        self.checkBox_year.hide()
        self.pushButton_approve_changing.hide()
        self.pushButton_back_first.hide()
        self.gridLayout_window.removeItem(self.spacerItem)
        self.checkBox_title.setChecked(False)
        self.checkBox_author.setChecked(False)
        self.checkBox_ISBN.setChecked(False)
        self.checkBox_year.setChecked(False)
        self.listWidget.clear()
        self.lineEdit_search.clear()
        self.pushButton_close.show()
        self.pushButton_approve_book.show()
        self.pushButton_approve_search.show()
        self.listWidget.show()
        self.lineEdit_search.show()

    def click_back_second(self):
        self.label_errors.hide()
        self.lineEdit_title.hide()
        self.lineEdit_author.hide()
        self.lineEdit_ISBN.hide()
        self.lineEdit_year.hide()
        self.lineEdit_title.clear()
        self.lineEdit_author.clear()
        self.lineEdit_ISBN.clear()
        self.lineEdit_year.clear()
        self.pushButton_approve_finally.hide()
        self.pushButton_back_second.hide()
        self.label.show()
        self.checkBox_title.setChecked(False)
        self.checkBox_author.setChecked(False)
        self.checkBox_ISBN.setChecked(False)
        self.checkBox_year.setChecked(False)
        self.checkBox_title.show()
        self.checkBox_author.show()
        self.checkBox_ISBN.show()
        self.checkBox_year.show()
        self.pushButton_approve_changing.show()
        self.pushButton_back_first.show()

    def click_close(self):
        try:
            self.server.close()
            self.close()

        except Exception as e:
            print(e)

    def retranslateUi(self, edit_book):
        _translate = QtCore.QCoreApplication.translate
        edit_book.setWindowTitle(_translate("edit_book", "edit_book"))
        self.label.setText(_translate(
            "edit_book", "لطفا مقادیری که می خواهید برای کتاب تغییر دهید را از پایین تیک بزنید:"))
        self.pushButton_approve_search.setText(
            _translate("edit_book", "شروع جستوجو"))
        self.pushButton_approve_book.setText(_translate(
            "edit_book", "تایید کتاب برای اعمال تغییرات"))
        self.pushButton_approve_changing.setText(
            _translate("edit_book", "تایید برای تغییر"))
        self.pushButton_approve_finally.setText(
            _translate("edit_book", "اعمال تغییر و ثبت نهایی"))
        self.pushButton_back_second.setText(_translate(
            "edit_book", "برگشت به صفحه ی دوم"))
        self.pushButton_back_first.setText(
            _translate("edit_book", "برگشت به صفحه ی اول"))
        self.pushButton_close.setText(_translate("edit_book", "بستن"))
        self.checkBox_ISBN.setText(_translate("edit_book", "ISBN"))
        self.checkBox_year.setText(_translate("edit_book", "سال انتشار"))
        self.checkBox_author.setText(_translate("edit_book", "نویسنده"))
        self.checkBox_title.setText(_translate("edit_book", "نام/تایتل"))
        self.lineEdit_search.setPlaceholderText(_translate(
            "edit_book", "لطفا کتابی که میخواهید تغییری روی آن ایجاد کنید را اینجا جستوجو کنید"))
        self.lineEdit_title.setPlaceholderText(
            _translate("edit_book", "نام جدید را وارد کنید"))
        self.lineEdit_author.setPlaceholderText(
            _translate("edit_book", "نویسنده ی جدید را وارد کنید"))
        self.lineEdit_ISBN.setPlaceholderText(
            _translate("edit_book", "ISBN جدید را وارد کنید"))
        self.lineEdit_year.setPlaceholderText(_translate(
            "edit_book", "سال انتشار جدید را وارد کنید"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    edit_book = Ui_edit_book()
    edit_book.show()
    sys.exit(app.exec_())
