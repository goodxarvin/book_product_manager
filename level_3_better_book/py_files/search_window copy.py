from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView
import sqlite3


class Ui_search_widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("search_widget")
        self.resize(830, 360)
        self.setAcceptDrops(True)
        self.setStyleSheet("background-color: rgb(154, 154, 154);")
        self.gridLayout_window = QtWidgets.QGridLayout(self)
        self.gridLayout_window.setObjectName("gridLayout_window")
        self.gridLayout_SS_LE = QtWidgets.QGridLayout()
        self.gridLayout_SS_LE.setObjectName("gridLayout_SS_LE")
        self.gridLayout_labels = QtWidgets.QGridLayout()
        self.gridLayout_labels.setObjectName("gridLayout_labels")
        self.gridLayout_close = QtWidgets.QGridLayout()
        self.gridLayout_close.setObjectName("gridLayout_close")
        self.pushButton_start_search = QtWidgets.QPushButton(
            self, clicked=lambda: self.start_search_clicked())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
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
        self.pushButton_start_search.setStyleSheet("color: white;\n"
                                                   "background-color: green;\n"
                                                   "border-color: white;\n"
                                                   "border-width: 5px;\n"
                                                   "border-radius: 30px;\n"
                                                   "border-style: solid;\n"
                                                   "padding: 10px;")
        self.pushButton_start_search.setObjectName("pushButton_start_search")
        self.gridLayout_close.addWidget(
            self.pushButton_start_search, 0, 0, 1, 1)

        self.pushButton_back = QtWidgets.QPushButton(
            self, clicked=lambda: self.back_clicked())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_back.sizePolicy().hasHeightForWidth())
        self.pushButton_back.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_back.setStyleSheet("color: white;\n"
                                           "background-color: green;\n"
                                           "border-color: white;\n"
                                           "border-width: 5px;\n"
                                           "border-radius: 30px;\n"
                                           "border-style: solid;\n"
                                           "padding: 10px;")
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_back.hide()
        self.gridLayout_SS_LE.addWidget(self.pushButton_back, 3, 0, 1, 1)

        self.pushButton_close = QtWidgets.QPushButton(
            self, clicked=lambda: self.close_clicked())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
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
        self.pushButton_close.setStyleSheet("color: white;\n"
                                            "background-color: rgb(170, 0, 0);\n"
                                            "border-color: white;\n"
                                            "border-width: 5px;\n"
                                            "border-radius: 30px;\n"
                                            "border-style: solid;\n"
                                            "padding: 10px;")
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout_close.addWidget(self.pushButton_close, 0, 1, 1, 1)
        self.gridLayout_window.addLayout(self.gridLayout_close, 3, 0, 1, 1)

        self.gridLayout_close.setColumnStretch(0, 2)
        self.gridLayout_close.setColumnStretch(1, 2)

        self.lineEdit_search_key = QtWidgets.QLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_search_key.sizePolicy().hasHeightForWidth())
        self.lineEdit_search_key.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_search_key.setFont(font)
        self.lineEdit_search_key.setStyleSheet("background-color: white;\n"
                                               "padding: 10px;\n"
                                               "border-color: black;\n"
                                               "border-width: 5px;\n"
                                               "border-radius: 30px;\n"
                                               "border-style: solid;")
        self.lineEdit_search_key.setObjectName("lineEdit_search_key")
        self.gridLayout_SS_LE.addWidget(self.lineEdit_search_key, 0, 1, 1, 1)
        self.gridLayout_window.addLayout(self.gridLayout_SS_LE, 0, 0, 1, 1)
        self.gridLayout_window.addLayout(self.gridLayout_labels, 1, 0, 1, 1)
        self.label_error = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_error.sizePolicy().hasHeightForWidth())
        self.label_error.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_error.setFont(font)
        self.label_error.setStyleSheet("background-color: red;\n"
                                       "color: white;\n"
                                       "border-radius: 30px;\n"
                                       "padding: 10px;\n"
                                       "border-style: solid;")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.label_error.hide()
        self.gridLayout_window.setRowStretch(0, 1)
        self.gridLayout_window.setRowStretch(3, 1)

        self.label_result = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_result.sizePolicy().hasHeightForWidth())
        self.label_result.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("background-color: rgb(154, 154, 154);\n"
                                        "border-color: black;\n"
                                        "border-radius: 30px;\n"
                                        "border-width: 5px;\n"
                                        "border-style: solid;\n"
                                        "padding: 15px;\n"
                                        "color: white;")
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.gridLayout_SS_LE.addWidget(self.label_result, 1, 0, 1, 1)
        self.label_result.hide()

        self.result_table = QTableWidget()
        self.result_table.setColumnCount(5)
        self.result_table.hide()
        self.result_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.result_table.setSelectionBehavior(QAbstractItemView.SelectItems)
        column_header = self.result_table.horizontalHeader()
        column_header.setSectionResizeMode(QHeaderView.Stretch)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result_table.setFont(font)
        self.gridLayout_SS_LE.addWidget(self.result_table, 2, 0, 1, 1)

        self.message_box_em = QMessageBox()
        self.message_box_em.setIcon(QMessageBox.Information)
        self.message_box_em.setWindowTitle("empty_entry...")
        self.message_box_em.setStandardButtons(QMessageBox.Ok)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def reset_label(self):
        self.label_error.hide()
        self.gridLayout_window.removeWidget(self.label_error)
        self.gridLayout_window.setRowStretch(1, 0)

    def start_search_clicked(self):
        self.label_error.hide()
        try:
            search_key = self.lineEdit_search_key.text()
            if search_key:
                self.server = sqlite3.connect("db_files\\book_database.db")
                self.book_cursor = self.server.cursor()
                self.book_cursor.execute(
                    "SELECT * FROM Books WHERE id LIKE ? OR title LIKE ? OR writer LIKE ? OR ISBN LIKE ? OR year_published LIKE ?",
                    (f"%{search_key}%", f"%{search_key}%", f"%{search_key}%", f"%{search_key}%", f"%{search_key}%"))
                all_found_data = self.book_cursor.fetchall()
                row_count = len(all_found_data)
                if all_found_data:
                    self.pushButton_start_search.hide()
                    self.lineEdit_search_key.hide()
                    self.pushButton_close.hide()
                    self.result_table.setRowCount(row_count)
                    self.result_table.setHorizontalHeaderLabels(
                        ["ID", "نام", "نویسنده", "ISBN", "سال انتشار"])

                    for row, all_info in enumerate(all_found_data):
                        for column, info in enumerate(all_info):
                            item = QTableWidgetItem(str(info))
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.result_table.setItem(row, column, item)

                    row_header = self.result_table.verticalHeader()
                    row_header.setSectionResizeMode(QHeaderView.Stretch)
                    self.label_result.show()
                    self.result_table.show()
                    self.gridLayout_SS_LE.setRowStretch(2, 3)
                    self.gridLayout_SS_LE.setRowStretch(3, 1)
                    self.gridLayout_window.setRowStretch(3, 0)
                    self.pushButton_back.show()
                else:
                    self.lineEdit_search_key.clear()
                    self.gridLayout_labels.addWidget(
                        self.label_error, 0, 0, 1, 1)
                    self.gridLayout_window.setRowStretch(1, 1)
                    self.label_error.show()
                    QtCore.QTimer.singleShot(3000, self.reset_label)
            else:
                self.message_box_em.exec_()
        except Exception as e:
            print(e)

    def back_clicked(self):
        self.result_table.clear()
        self.lineEdit_search_key.clear()
        self.label_result.hide()
        self.result_table.hide()
        self.pushButton_back.hide()
        self.gridLayout_SS_LE.setRowStretch(1, 0)
        self.gridLayout_SS_LE.setRowStretch(2, 0)
        self.gridLayout_SS_LE.setRowStretch(3, 0)
        self.gridLayout_window.setRowStretch(3, 1)
        self.pushButton_close.show()
        self.pushButton_start_search.show()
        self.lineEdit_search_key.show()

    def close_clicked(self):
        self.close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(
            _translate("search_widget", "search_book"))
        self.pushButton_start_search.setText(
            _translate("search_widget", "شروع جستوجو"))
        self.pushButton_back.setText(
            _translate("search_widget", "برگشت به صفحه ی اول"))
        self.pushButton_close.setText(
            _translate("search_widget", "بستن"))
        self.lineEdit_search_key.setPlaceholderText(_translate(
            "search_widget", "لطفا اینجا کلمه ای را برای جستوجوی کتاب بنویسید"))
        self.label_error.setText(_translate(
            "search_widget", "جستجوی شما نتیجه ای نداشت"))
        self.label_result.setText(_translate(
            "search_widget", "نتایج:"))
        self.message_box_em.setText(_translate(
            "search_widget", "شما در ورودی هیچ چیزی برای جستوجو وارد نکرده اید"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    search_widget = Ui_search_widget()
    search_widget.show()
    sys.exit(app.exec_())
