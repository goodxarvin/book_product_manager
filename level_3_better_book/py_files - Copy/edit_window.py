from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import re


class Ui_edit_window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self._translate = QtCore.QCoreApplication.translate
        self.server = sqlite3.connect("db_files\\book_database.db")
        self.book_cursor = self.server.cursor()
        self.setObjectName("edit_book")
        self.resize(1100, 400)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setStyleSheet("background-color: rgb(154, 154, 154);")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_search_lineEdit = QtWidgets.QGridLayout()
        self.gridLayout_search_lineEdit.setObjectName(
            "gridLayout_search_lineEdit")
        self.pushButton_start_search = QtWidgets.QPushButton(self)
        self.pushButton_start_search.pressed.connect(self.start_search_clicked)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_start_search.sizePolicy().hasHeightForWidth())
        self.pushButton_start_search.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_start_search.setFont(font)
        self.pushButton_start_search.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_start_search.setStyleSheet("background-color: green;\n"
                                                   "color: white;\n"
                                                   "border-color: white;\n"
                                                   "border-width: 5px;\n"
                                                   "border-radius: 30px;\n"
                                                   "padding: 10px;\n"
                                                   "border-style: solid;")
        self.pushButton_start_search.setObjectName("pushButton_start_search")
        self.gridLayout_search_lineEdit.addWidget(
            self.pushButton_start_search, 0, 0, 1, 1)
        self.lineEdit_search_word = QtWidgets.QLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_search_word.sizePolicy().hasHeightForWidth())
        self.lineEdit_search_word.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_search_word.setFont(font)
        self.lineEdit_search_word.setStyleSheet("background-color: white;\n"
                                                "border-color: black;\n"
                                                "border-width: 5px;\n"
                                                "border-radius: 30px;\n"
                                                "padding: 10px;\n"
                                                "border-style: solid;")
        self.lineEdit_search_word.setObjectName("lineEdit_search_word")
        self.gridLayout_search_lineEdit.addWidget(
            self.lineEdit_search_word, 0, 1, 1, 1)
        self.gridLayout_search_lineEdit.setColumnStretch(0, 1)
        self.gridLayout_search_lineEdit.setColumnStretch(1, 2)
        self.gridLayout.addLayout(self.gridLayout_search_lineEdit, 0, 0, 1, 1)
        self.gridLayout_list_widget = QtWidgets.QGridLayout()
        self.gridLayout_list_widget.setObjectName("gridLayout_list_widget")
        self.listWidget_select_book = QtWidgets.QListWidget(self)
        self.listWidget_select_book.itemSelectionChanged.connect(
            self.show_select_button)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.listWidget_select_book.sizePolicy().hasHeightForWidth())
        self.listWidget_select_book.setSizePolicy(sizePolicy)
        self.listWidget_select_book.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_select_book.setFont(font)
        self.listWidget_select_book.setStyleSheet("background-color: white;\n"
                                                  "border-color: black;\n"
                                                  "border-width: 5px;\n"
                                                  "border-radius: 30px;\n"
                                                  "padding: 10px;\n"
                                                  "border-style: solid;")
        self.listWidget_select_book.setLayoutDirection(
            QtCore.Qt.RightToLeft)
        self.listWidget_select_book.setObjectName("listWidget_select_book")
        self.gridLayout_list_widget.addWidget(
            self.listWidget_select_book, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_list_widget, 1, 0, 1, 1)
        self.gridLayout_close_select_p1 = QtWidgets.QGridLayout()
        self.gridLayout_close_select_p1.setObjectName(
            "gridLayout_close_select_p1")
        self.pushButton_select_book = QtWidgets.QPushButton(self)
        self.pushButton_select_book.pressed.connect(self.select_button_clicked)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_select_book.sizePolicy().hasHeightForWidth())
        self.pushButton_select_book.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_select_book.setFont(font)
        self.pushButton_select_book.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_select_book.setStyleSheet("background-color: green;\n"
                                                  "color: white;\n"
                                                  "border-color: white;\n"
                                                  "border-width: 5px;\n"
                                                  "border-radius: 30px;\n"
                                                  "padding: 10px;\n"
                                                  "border-style: solid;")
        self.pushButton_select_book.setObjectName("pushButton_select_book")
        self.pushButton_select_book.hide()
        self.gridLayout_close_select_p1.addWidget(
            self.pushButton_select_book, 0, 0, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(self)
        self.pushButton_close.pressed.connect(self.close_clicked)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_close.setStyleSheet("background-color: rgb(170, 0, 0);\n"
                                            "color: white;\n"
                                            "border-color: white;\n"
                                            "border-width: 5px;\n"
                                            "border-radius: 30px;\n"
                                            "padding: 10px;\n"
                                            "border-style: solid;")
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout_close_select_p1.addWidget(
            self.pushButton_close, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_close_select_p1, 3, 0, 1, 1)
        self.gridLayout_label_info = QtWidgets.QGridLayout()
        self.gridLayout_label_info.setObjectName("gridLayout_label_info")
        self.label_info = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_info.sizePolicy().hasHeightForWidth())
        self.label_info.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_info.setFont(font)
        self.label_info.setStyleSheet("border-color: black;\n"
                                      "border-width: 5px;\n"
                                      "border-radius: 30px;\n"
                                      "padding: 10px;\n"
                                      "border-style: solid;")
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")
        self.label_info.hide()
        self.gridLayout_label_info.addWidget(self.label_info, 0, 0, 1, 1)

        self.label_notif_handler = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_notif_handler.sizePolicy().hasHeightForWidth())
        self.label_notif_handler.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_notif_handler.setFont(font)
        self.label_notif_handler.setAlignment(QtCore.Qt.AlignCenter)
        self.label_notif_handler.setObjectName("label_notif_handler")
        self.label_notif_handler.hide()

        self.gridLayout.addLayout(self.gridLayout_label_info, 4, 0, 1, 1)
        self.gridLayout_checkBoxes = QtWidgets.QGridLayout()
        self.gridLayout_checkBoxes.setObjectName("gridLayout_checkBoxes")
        self.checkBox_title = QtWidgets.QCheckBox(self)
        self.checkBox_title.stateChanged.connect(self.show_approve_button)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_title.sizePolicy().hasHeightForWidth())
        self.checkBox_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_title.setFont(font)
        self.checkBox_title.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_title.setStyleSheet("background-color: white;\n"
                                          "border-color: black;\n"
                                          "border-width: 5px;\n"
                                          "border-radius: 30px;\n"
                                          "padding: 10px;\n"
                                          "border-style: solid;")
        self.checkBox_title.setObjectName("checkBox_title")
        self.checkBox_title.hide()
        self.gridLayout_checkBoxes.addWidget(self.checkBox_title, 0, 0, 1, 1)
        self.checkBox_writer = QtWidgets.QCheckBox(self)
        self.checkBox_writer.stateChanged.connect(self.show_approve_button)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_writer.sizePolicy().hasHeightForWidth())
        self.checkBox_writer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_writer.setFont(font)
        self.checkBox_writer.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_writer.setStyleSheet("background-color: white;\n"
                                           "border-color: black;\n"
                                           "border-width: 5px;\n"
                                           "border-radius: 30px;\n"
                                           "padding: 10px;\n"
                                           "border-style: solid;")
        self.checkBox_writer.setObjectName("checkBox_writer")
        self.checkBox_writer.hide()
        self.gridLayout_checkBoxes.addWidget(self.checkBox_writer, 0, 1, 1, 1)
        self.checkBox_ISBN = QtWidgets.QCheckBox(self)
        self.checkBox_ISBN.stateChanged.connect(self.show_approve_button)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_ISBN.sizePolicy().hasHeightForWidth())
        self.checkBox_ISBN.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_ISBN.setFont(font)
        self.checkBox_ISBN.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_ISBN.setStyleSheet("background-color: white;\n"
                                         "border-color: black;\n"
                                         "border-width: 5px;\n"
                                         "border-radius: 30px;\n"
                                         "padding: 10px;\n"
                                         "border-style: solid;")
        self.checkBox_ISBN.setObjectName("checkBox_ISBN")
        self.checkBox_ISBN.hide()
        self.gridLayout_checkBoxes.addWidget(self.checkBox_ISBN, 0, 2, 1, 1)
        self.checkBox_year = QtWidgets.QCheckBox(self)
        self.checkBox_year.stateChanged.connect(self.show_approve_button)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_year.sizePolicy().hasHeightForWidth())
        self.checkBox_year.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_year.setFont(font)
        self.checkBox_year.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_year.setStyleSheet("background-color: white;\n"
                                         "border-color: black;\n"
                                         "border-width: 5px;\n"
                                         "border-radius: 30px;\n"
                                         "padding: 10px;\n"
                                         "border-style: solid;")
        self.checkBox_year.setObjectName("checkBox_year")
        self.checkBox_year.hide()
        self.gridLayout_checkBoxes.addWidget(self.checkBox_year, 0, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_checkBoxes, 6, 0, 1, 1)
        self.gridLayout_backp1_approve_ckeck = QtWidgets.QGridLayout()
        self.gridLayout_backp1_approve_ckeck.setObjectName(
            "gridLayout_backp1_approve_ckeck")
        self.pushButton_approve_checkes = QtWidgets.QPushButton(self)
        self.pushButton_approve_checkes.pressed.connect(
            self.approve_checks_clicked)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_approve_checkes.sizePolicy().hasHeightForWidth())
        self.pushButton_approve_checkes.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_approve_checkes.setFont(font)
        self.pushButton_approve_checkes.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_approve_checkes.setStyleSheet("background-color: green;\n"
                                                      "color: white;\n"
                                                      "border-color: white;\n"
                                                      "border-width: 5px;\n"
                                                      "border-radius: 30px;\n"
                                                      "padding: 10px;\n"
                                                      "border-style: solid;")
        self.pushButton_approve_checkes.setObjectName(
            "pushButton_approve_checkes")
        self.pushButton_approve_checkes.hide()
        self.gridLayout_backp1_approve_ckeck.addWidget(
            self.pushButton_approve_checkes, 0, 0, 1, 1)
        self.pushButton_back_to_p1 = QtWidgets.QPushButton(self)
        self.pushButton_back_to_p1.pressed.connect(self.back_to_p1_clicked)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_back_to_p1.sizePolicy().hasHeightForWidth())
        self.pushButton_back_to_p1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_back_to_p1.setFont(font)
        self.pushButton_back_to_p1.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_back_to_p1.setStyleSheet("background-color: rgb(170, 0, 0);\n"
                                                 "color: white;\n"
                                                 "border-color: white;\n"
                                                 "border-width: 5px;\n"
                                                 "border-radius: 30px;\n"
                                                 "padding: 10px;\n"
                                                 "border-style: solid;")
        self.pushButton_back_to_p1.setObjectName("pushButton_back_to_p1")
        self.pushButton_back_to_p1.hide()
        self.gridLayout_backp1_approve_ckeck.addWidget(
            self.pushButton_back_to_p1, 0, 1, 1, 1)
        self.gridLayout.addLayout(
            self.gridLayout_backp1_approve_ckeck, 7, 0, 1, 1)
        self.gridLayout_lienEdits_new_data = QtWidgets.QGridLayout()
        self.gridLayout_lienEdits_new_data.setObjectName(
            "gridLayout_lienEdits_new_data")
        self.lineEdit_new_writer = QtWidgets.QLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_new_writer.sizePolicy().hasHeightForWidth())
        self.lineEdit_new_writer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_new_writer.setFont(font)
        self.lineEdit_new_writer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_new_writer.setStyleSheet("background-color: white;\n"
                                               "border-color: black;\n"
                                               "border-width: 5px;\n"
                                               "border-radius: 30px;\n"
                                               "padding: 10px;\n"
                                               "border-style: solid;")
        self.lineEdit_new_writer.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lineEdit_new_writer.setObjectName("lineEdit_new_writer")
        self.lineEdit_new_writer.hide()
        self.gridLayout_lienEdits_new_data.addWidget(
            self.lineEdit_new_writer, 1, 0, 1, 1)
        self.lineEdi_new_title = QtWidgets.QLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdi_new_title.sizePolicy().hasHeightForWidth())
        self.lineEdi_new_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdi_new_title.setFont(font)
        self.lineEdi_new_title.setStyleSheet("background-color: white;\n"
                                             "border-color: black;\n"
                                             "border-width: 5px;\n"
                                             "border-radius: 30px;\n"
                                             "padding: 10px;\n"
                                             "border-style: solid;")
        self.lineEdi_new_title.setObjectName("lineEdi_new_title")
        self.lineEdi_new_title.hide()
        self.gridLayout_lienEdits_new_data.addWidget(
            self.lineEdi_new_title, 0, 0, 1, 1)
        self.lineEdit_new_ISBN = QtWidgets.QLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_new_ISBN.sizePolicy().hasHeightForWidth())
        self.lineEdit_new_ISBN.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_new_ISBN.setFont(font)
        self.lineEdit_new_ISBN.setStyleSheet("background-color: white;\n"
                                             "border-color: black;\n"
                                             "border-width: 5px;\n"
                                             "border-radius: 30px;\n"
                                             "padding: 10px;\n"
                                             "border-style: solid;")
        self.lineEdit_new_ISBN.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lineEdit_new_ISBN.setObjectName("lineEdit_new_ISBN")
        self.lineEdit_new_ISBN.hide()
        self.gridLayout_lienEdits_new_data.addWidget(
            self.lineEdit_new_ISBN, 2, 0, 1, 1)
        self.lineEdit_new_year = QtWidgets.QLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_new_year.sizePolicy().hasHeightForWidth())
        self.lineEdit_new_year.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_new_year.setFont(font)
        self.lineEdit_new_year.setStyleSheet("background-color: white;\n"
                                             "border-color: black;\n"
                                             "border-width: 5px;\n"
                                             "border-radius: 30px;\n"
                                             "padding: 10px;\n"
                                             "border-style: solid;")
        self.lineEdit_new_year.setObjectName("lineEdit_new_year")
        self.lineEdit_new_year.hide()
        self.gridLayout_lienEdits_new_data.addWidget(
            self.lineEdit_new_year, 3, 0, 1, 1)
        self.gridLayout.addLayout(
            self.gridLayout_lienEdits_new_data, 8, 0, 1, 1)
        self.gridLayout_final_approve_backp2 = QtWidgets.QGridLayout()
        self.gridLayout_final_approve_backp2.setObjectName(
            "gridLayout_final_approve_backp2")
        self.pushButton_final_approve = QtWidgets.QPushButton(self)
        self.pushButton_final_approve.pressed.connect(
            self.final_approve_clicked)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_final_approve.sizePolicy().hasHeightForWidth())
        self.pushButton_final_approve.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_final_approve.setFont(font)
        self.pushButton_final_approve.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_final_approve.setStyleSheet("background-color: green;\n"
                                                    "color: white;\n"
                                                    "border-color: white;\n"
                                                    "border-width: 5px;\n"
                                                    "border-radius: 30px;\n"
                                                    "padding: 10px;\n"
                                                    "border-style: solid;")
        self.pushButton_final_approve.setObjectName("pushButton_final_approve")
        self.pushButton_final_approve.hide()
        self.gridLayout_final_approve_backp2.addWidget(
            self.pushButton_final_approve, 0, 0, 1, 1)
        self.pushButton_back_to_p2 = QtWidgets.QPushButton(self)
        self.pushButton_back_to_p2.pressed.connect(self.back_to_p2_clicked)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_back_to_p2.sizePolicy().hasHeightForWidth())
        self.pushButton_back_to_p2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_back_to_p2.setFont(font)
        self.pushButton_back_to_p2.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_back_to_p2.setStyleSheet("background-color: rgb(170, 0, 0);\n"
                                                 "color: white;\n"
                                                 "border-color: white;\n"
                                                 "border-width: 5px;\n"
                                                 "border-radius: 30px;\n"
                                                 "padding: 10px;\n"
                                                 "border-style: solid;")
        self.pushButton_back_to_p2.setObjectName("pushButton_back_to_p2")
        self.pushButton_back_to_p2.hide()
        self.gridLayout_final_approve_backp2.addWidget(
            self.pushButton_back_to_p2, 0, 1, 1, 1)
        self.gridLayout.addLayout(
            self.gridLayout_final_approve_backp2, 10, 0, 1, 1)

        self.empty_search_message = QMessageBox()
        self.empty_search_message.setIcon(QMessageBox.Information)
        self.empty_search_message.setWindowTitle("empty_entry...")
        self.empty_search_message.setText(
            "شما هیچ چیزی در ورودی برای جستوجو وارد نکرده اید\nلطفا حداقل یک کلمه را برای جستوجو وارد کنید")
        self.empty_search_message.setStandardButtons(QMessageBox.Ok)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 2)
        self.gridLayout.setRowStretch(2, 0)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 0)
        self.gridLayout.setRowStretch(5, 0)
        self.gridLayout.setRowStretch(6, 0)
        self.gridLayout.setRowStretch(7, 0)
        self.gridLayout.setRowStretch(8, 0)
        self.gridLayout.setRowStretch(9, 0)
        self.gridLayout.setRowStretch(10, 0)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def reset_label_notif(self, label_row):
        self.label_notif_handler.hide()
        self.gridLayout.removeWidget(self.label_notif_handler)
        self.gridLayout.setRowStretch(label_row, 0)

    def show_approve_button(self):
        is_checked = [self.checkBox_title.isChecked(),
                      self.checkBox_writer.isChecked(),
                      self.checkBox_ISBN.isChecked(),
                      self.checkBox_year.isChecked()]
        if any(is_checked):
            self.pushButton_approve_checkes.show()
        else:
            self.pushButton_approve_checkes.hide()

    def show_select_button(self):
        if self.listWidget_select_book.selectedItems():
            self.pushButton_select_book.show()
        else:
            self.pushButton_select_book.hide()

    def start_search_clicked(self):
        search_key = self.lineEdit_search_word.text()
        if search_key:
            self.book_cursor.execute("SELECT * FROM Books WHERE id LIKE ? OR title LIKE ? OR writer LIKE ? OR ISBN LIKE ? OR year_published LIKE ?",
                                     (f"%{search_key}%", f"%{search_key}%", f"%{search_key}%", f"%{search_key}%", f"%{search_key}%"))
            found_books = self.book_cursor.fetchall()
            if found_books:
                self.listWidget_select_book.clear()
                for data in found_books:
                    self.listWidget_select_book.addItem(
                        f"ID: {data[0]}, ISBN: {data[3]}\nنام: {data[1]}, نویسنده: {data[2]}, سال انتشار: {data[4]}\n")

            else:
                self.lineEdit_search_word.clear()
                self.label_notif_handler.setStyleSheet("border-color: white;\n"
                                                       "color: white;\n"
                                                       "background-color: red;\n"
                                                       "border-radius: 30px;\n"
                                                       "padding: 10px;")
                self.label_notif_handler.setText(self._translate(
                    "edit_book", "جستوجوی شما نتیجه ای نداشت"))
                self.gridLayout.addWidget(self.label_notif_handler, 2, 0, 1, 1)
                self.gridLayout.setRowStretch(2, 1)
                self.label_notif_handler.show()
                try:
                    QtCore.QTimer.singleShot(
                        3000, lambda: self.reset_label_notif(2))
                except Exception as e:
                    print(e)
        else:
            self.empty_search_message.exec_()

    def select_button_clicked(self):
        self.selected_book = self.listWidget_select_book.currentItem()
        self.label_notif_handler.hide()
        self.lineEdit_search_word.hide()
        self.pushButton_start_search.hide()
        self.pushButton_select_book.hide()
        self.pushButton_close.hide()
        self.listWidget_select_book.hide()
        self.gridLayout.setRowStretch(0, 0)
        self.gridLayout.setRowStretch(1, 0)
        self.gridLayout.setRowStretch(2, 0)
        self.gridLayout.setRowStretch(3, 0)
        self.gridLayout.setRowStretch(4, 3)
        self.gridLayout.setRowStretch(6, 3)
        self.gridLayout.setRowStretch(7, 3)
        self.pushButton_back_to_p1.show()
        self.label_info.show()
        self.checkBox_title.show()
        self.checkBox_writer.show()
        self.checkBox_ISBN.show()
        self.checkBox_year.show()

    def approve_checks_clicked(self):
        is_title_selected = self.checkBox_title.isChecked()
        is_writer_selected = self.checkBox_writer.isChecked()
        is_ISBN_checked = self.checkBox_ISBN.isChecked()
        is_year_checked = self.checkBox_year.isChecked()
        new_title = self.lineEdi_new_title
        new_writer = self.lineEdit_new_writer
        new_ISBN = self.lineEdit_new_ISBN
        new_year = self.lineEdit_new_year
        new_lineEdits = [new_title, new_writer, new_ISBN, new_year]
        selectable_items = {"title": is_title_selected,
                            "writer": is_writer_selected,
                            "ISBN": is_ISBN_checked,
                            "year_published": is_year_checked}
        item_keys = list(selectable_items.keys())
        item_values = list(selectable_items.values())
        if all(item_values):
            self.resize(1100, 500)
        if any(item_values):
            self.label_notif_handler.hide()
            self.label_info.hide()
            self.checkBox_title.hide()
            self.checkBox_writer.hide()
            self.checkBox_ISBN.hide()
            self.checkBox_year.hide()
            self.pushButton_back_to_p1.hide()
            self.pushButton_approve_checkes.hide()
            self.checkBox_title.setChecked(False)
            self.checkBox_writer.setChecked(False)
            self.checkBox_ISBN.setChecked(False)
            self.checkBox_year.setChecked(False)
            self.gridLayout.setRowStretch(4, 0)
            self.gridLayout.setRowStretch(5, 0)
            self.gridLayout.setRowStretch(6, 0)
            self.gridLayout.setRowStretch(7, 0)
            self.gridLayout.setRowStretch(8, 10)
            self.gridLayout.setRowStretch(9, 0)
            self.gridLayout.setRowStretch(10, 4)
            self.pushButton_back_to_p2.show()
            self.pushButton_final_approve.show()
            self.selected_list = []
            for item_name, item_selected, new_lineEdit in zip(item_keys, item_values, new_lineEdits):
                if item_selected:
                    new_lineEdit.show()
                    self.selected_list.append([item_name, new_lineEdit])
                else:
                    new_lineEdit.hide()

        else:
            self.label_notif_handler.setStyleSheet("border-color: white;\n"
                                                   "color: white;\n"
                                                   "background-color: red;\n"
                                                   "border-radius: 30px;\n"
                                                   "padding: 10px;")
            self.label_notif_handler.setText(self._translate(
                "edit_book", "لطفا حداقل یکی از گزینه هارا انتخاب کنید"))
            self.gridLayout.addWidget(self.label_notif_handler, 5, 0, 1, 1)
            self.gridLayout.setRowStretch(5, 2)
            self.label_notif_handler.show()
            QtCore.QTimer.singleShot(3000, lambda: self.reset_label_notif(5))

    def final_approve_clicked(self):
        try:
            selected_book_str = self.selected_book.text()
            find_id = re.search(r"ID:\s*(\d+)", selected_book_str)
            selected_id = find_id.group(1)
            new_specifications = []
            sql_update_str = "UPDATE Books SET "
            for indicate_what_change in self.selected_list:
                sql_update_str += f"{indicate_what_change[0]} = ?, "
                new_specifications.append(indicate_what_change[1].text())

            new_specifications.append(selected_id)
            new_specifications = tuple(new_specifications)
            if all(new_specifications):
                sql_update_str = sql_update_str[:-2] + " WHERE id = ?"
                self.book_cursor.execute(sql_update_str, new_specifications)
                self.server.commit()
                self.gridLayout.setRowStretch(0, 1)
                self.gridLayout.setRowStretch(1, 2)
                self.gridLayout.setRowStretch(2, 1)
                self.gridLayout.setRowStretch(3, 1)
                self.gridLayout.setRowStretch(4, 0)
                self.gridLayout.setRowStretch(5, 0)
                self.gridLayout.setRowStretch(6, 0)
                self.gridLayout.setRowStretch(7, 0)
                self.gridLayout.setRowStretch(8, 0)
                self.gridLayout.setRowStretch(9, 0)
                self.gridLayout.setRowStretch(10, 0)
                self.pushButton_final_approve.hide()
                self.lineEdi_new_title.hide()
                self.lineEdit_new_writer.hide()
                self.lineEdit_new_ISBN.hide()
                self.lineEdit_new_year.hide()
                self.pushButton_back_to_p2.hide()
                self.lineEdit_search_word.show()
                self.pushButton_start_search.show()
                self.listWidget_select_book.show()
                self.pushButton_close.show()
                self.pushButton_select_book.show()
                self.listWidget_select_book.clear()
                self.lineEdit_search_word.clear()
                self.label_notif_handler.setStyleSheet("border-color: white;\n"
                                                       "color: white;\n"
                                                       "background-color: green;\n"
                                                       "border-radius: 30px;\n"
                                                       "padding: 10px;")
                self.label_notif_handler.setText(
                    "مشخصات کتاب با موفقیت تغییر یافت")
                self.gridLayout.addWidget(self.label_notif_handler, 2, 0, 1, 1)
                self.label_notif_handler.show()
                QtCore.QTimer.singleShot(
                    3000, lambda: self.reset_label_notif(2))

            else:
                is_title_visible = self.lineEdi_new_title.isVisible()
                is_writer_visible = self.lineEdit_new_writer.isVisible()
                is_ISBN_visible = self.lineEdit_new_ISBN.isVisible()
                is_year_visible = self.lineEdit_new_year.isVisible()
                is_title_em = self.lineEdi_new_title.text()
                is_writer_em = self.lineEdit_new_writer.text()
                is_ISBN_em = self.lineEdit_new_ISBN.text()
                is_year_em = self.lineEdit_new_year.text()
                empty_ones_list = ["نام", "نویسنده", "ISBN", "سال انتشار"]
                visible_em_new_specifications = [[is_title_visible, is_title_em], [is_writer_visible, is_writer_em],
                                                 [is_ISBN_visible, is_ISBN_em], [is_year_visible, is_year_em]]
                empties_str = "شما "
                for fulls, em_item in zip(visible_em_new_specifications, empty_ones_list):
                    if fulls[0] and not fulls[1]:
                        empties_str += f"{em_item} و "
                empties_str = empties_str[:-2] + \
                    "را خالی گذاشته اید\nلطفا قبل از تغییر مشخصات همه اطلاعات را وارد کنید"

                self.label_notif_handler.setStyleSheet("border-color: white;\n"
                                                       "color: white;\n"
                                                       "background-color: red;\n"
                                                       "border-radius: 30px;\n"
                                                       "padding: 10px;")
                self.label_notif_handler.setText(
                    self._translate("edit_book", empties_str))
                self.gridLayout.addWidget(self.label_notif_handler, 9, 0, 1, 1)
                self.gridLayout.setRowStretch(9, 1)
                self.label_notif_handler.show()
                QtCore.QTimer.singleShot(
                    3000, lambda: self.reset_label_notif(9))
        except Exception as e:
            print(e)

    def back_to_p1_clicked(self):
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 2)
        self.gridLayout.setRowStretch(2, 0)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 0)
        self.gridLayout.setRowStretch(5, 0)
        self.gridLayout.setRowStretch(6, 0)
        self.gridLayout.setRowStretch(7, 0)
        self.label_info.hide()
        self.label_notif_handler.hide()
        self.checkBox_title.hide()
        self.checkBox_writer.hide()
        self.checkBox_ISBN.hide()
        self.checkBox_year.hide()
        self.pushButton_approve_checkes.hide()
        self.pushButton_back_to_p1.hide()
        self.lineEdit_search_word.show()
        self.pushButton_start_search.show()
        self.listWidget_select_book.show()
        self.pushButton_close.show()
        self.pushButton_select_book.show()
        self.listWidget_select_book.clear()
        self.checkBox_title.setChecked(False)
        self.checkBox_writer.setChecked(False)
        self.checkBox_ISBN.setChecked(False)
        self.checkBox_year.setChecked(False)

    def back_to_p2_clicked(self):
        try:
            self.resize(1100, 400)
            self.gridLayout.setRowStretch(10, 0)
            self.gridLayout.setRowStretch(9, 0)
            self.gridLayout.setRowStretch(8, 0)
            self.gridLayout.setRowStretch(7, 3)
            self.gridLayout.setRowStretch(6, 3)
            self.gridLayout.setRowStretch(4, 3)
            self.label_notif_handler.hide()
            self.lineEdi_new_title.hide()
            self.lineEdit_new_writer.hide()
            self.lineEdit_new_ISBN.hide()
            self.lineEdit_new_year.hide()
            self.pushButton_final_approve.hide()
            self.pushButton_back_to_p2.hide()
            self.label_info.show()
            self.checkBox_title.show()
            self.checkBox_writer.show()
            self.checkBox_ISBN.show()
            self.checkBox_year.show()
            self.pushButton_back_to_p1.show()
            self.checkBox_title.setChecked(False)
            self.checkBox_writer.setChecked(False)
            self.checkBox_ISBN.setChecked(False)
            self.checkBox_year.setChecked(False)
        except Exception as e:
            print(e)

    def close_clicked(self):
        self.server.close()
        self.close()

    def retranslateUi(self):
        self.setWindowTitle(self._translate("edit_book", "edit_book"))
        self.pushButton_start_search.setText(
            self._translate("edit_book", "شروع جستوجو"))
        self.lineEdit_search_word.setPlaceholderText(self._translate(
            "edit_book", "لطفا کلمه ای را برای جستوجو و انتخاب کتاب برای تغییر مشخصات وارد کنید"))
        self.pushButton_select_book.setText(
            self._translate("edit_book", "انتخاب کتاب"))
        self.pushButton_close.setText(self._translate("edit_book", "بستن"))
        self.label_info.setText(self._translate(
            "edit_book", "لطفا اطلاعاتی که می خواهید تغییر دهید را از پایین انتخاب کنید"))
        self.checkBox_title.setText(
            self._translate("edit_book", "تغییر نام"))
        self.checkBox_writer.setText(
            self._translate("edit_book", "تغییر نویسنده"))
        self.checkBox_ISBN.setText(
            self._translate("edit_book", "ISBN تغییر"))
        self.checkBox_year.setText(self._translate(
            "edit_book", "تغییر سال انتشار"))
        self.pushButton_approve_checkes.setText(
            self._translate("edit_book", "تایید گزینه های انتخابی"))
        self.pushButton_back_to_p1.setText(
            self._translate("edit_book", "برگشت به صفحه اول"))
        self.lineEdit_new_writer.setPlaceholderText(
            self._translate("edit_book", "نویسنده ی جدید را وارد کنید"))
        self.lineEdi_new_title.setPlaceholderText(
            self._translate("edit_book", "نام جدید را وارد کنید"))
        self.lineEdit_new_ISBN.setPlaceholderText(
            self._translate("edit_book", "اینجا ISBN جدید را وارد کنید"))
        self.lineEdit_new_year.setPlaceholderText(
            self._translate("edit_book", "سال انتشار جدید را وارد کنید"))
        self.pushButton_final_approve.setText(
            self._translate("edit_book", "تایید تغییرات و ثبت نهایی"))
        self.pushButton_back_to_p2.setText(
            self._translate("edit_book", "برگشت به صفحه دوم"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    edit_window = Ui_edit_window()
    edit_window.show()
    sys.exit(app.exec_())
