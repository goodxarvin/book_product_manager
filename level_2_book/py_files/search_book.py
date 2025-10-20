from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3


class Ui_search(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, search):
        search.setObjectName("search")
        search.resize(1000, 250)
        self.gridLayout_main_window = QtWidgets.QGridLayout(search)
        self.gridLayout_main_window.setObjectName("gridLayout_main_window")
        self.gridLayout_lineEdit = QtWidgets.QGridLayout()
        self.gridLayout_lineEdit.setObjectName("gridLayout_lineEdit")

        self.label = QtWidgets.QLabel(search)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: white;")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_lineEdit.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_main_window.addLayout(
            self.gridLayout_lineEdit, 0, 1, 1, 1)
        self.label.setVisible(False)

        self.lineEdit = QtWidgets.QLineEdit(search)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_lineEdit.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.gridLayout_main_window.addLayout(
            self.gridLayout_lineEdit, 0, 1, 1, 1)
        self.gridLayout_button = QtWidgets.QGridLayout()
        self.gridLayout_button.setObjectName("gridLayout_button")
        self.pushButton_search = QtWidgets.QPushButton(
            search, clicked=lambda: self.start_search())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_search.sizePolicy().hasHeightForWidth())
        self.pushButton_search.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_search.setObjectName("pushButton")
        self.gridLayout_button.addWidget(self.pushButton_search, 0, 0, 1, 1)

        self.pushButton_close = QtWidgets.QPushButton(
            search, clicked=lambda: self.close_search())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout_button.addWidget(self.pushButton_close, 0, 1, 1, 1)
        self.pushButton_close.setVisible(True)

        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_button.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_main_window.addLayout(
            self.gridLayout_button, 1, 1, 1, 1)

        self.pushButton_back = QtWidgets.QPushButton(
            search, clicked=lambda: self.back())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_back.sizePolicy().hasHeightForWidth())
        self.pushButton_back.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_back.setObjectName("pushButton")
        self.pushButton_back.setVisible(False)
        self.gridLayout_button.addWidget(self.pushButton_back, 0, 0, 1, 1)

        self.retranslateUi(search)
        QtCore.QMetaObject.connectSlotsByName(search)

    def start_search(self):
        try:
            string = ""
            search_key = self.lineEdit.text()
            server = sqlite3.connect("db_files\\book_database.db")
            cursor = server.cursor()
            cursor.execute(
                """SELECT * FROM Books WHERE id LIKE ? OR title LIKE ? OR author LIKE ? OR isbn LIKE ? OR year_published LIKE ?""",
                (f"%{search_key}%", f"%{search_key}%", f"%{search_key}%", f"%{search_key}%", f"%{search_key}%"))
            books_found = cursor.fetchall()
            if len(books_found) != 0:
                self.pushButton_search.setVisible(False)
                self.lineEdit.setVisible(False)
                self.pushButton_close.setVisible(False)
                self.label.setVisible(True)
                self.pushButton_back.setVisible(True)
                for index, book in enumerate(books_found):
                    book_info = f"{book[4]}:سال انتشار, {book[2]}:نویسنده, {book[1]}:نام  <--- {index+1}\nid: {book[0]}, ISBN:{book[3]}\n\n"
                    string += book_info
                self.label.setText(string)
            else:
                self.message_box = QMessageBox()
                self.message_box.setIcon(QMessageBox.Information)
                self.message_box.setWindowTitle("no results")
                self.message_box.setText("جستوجوی شمل نتیجه ای نداشت...")
                self.message_box.setStandardButtons(QMessageBox.Ok)
                self.message_box.exec_()
                self.lineEdit.clear()
            server.close()
        except Exception as e:
            print(e)

    def back(self):
        self.pushButton_search.setVisible(True)
        self.lineEdit.setVisible(True)
        self.pushButton_close.setVisible(True)
        self.lineEdit.clear()
        self.label.clear()
        self.label.setVisible(False)
        self.pushButton_back.setVisible(False)

    def close_search(self):
        self.close()

    def retranslateUi(self, search):
        _translate = QtCore.QCoreApplication.translate
        search.setWindowTitle(_translate("search", "search_book"))
        self.lineEdit.setPlaceholderText(_translate(
            "search_book", "لطفا کلید جستوجو را وارد کنید"))
        self.pushButton_search.setText(_translate("search", "شروع جستوجو"))
        self.pushButton_back.setText(_translate("search", "برگشت"))
        self.pushButton_close.setText(_translate("search", "بستن"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    search = Ui_search()
    search.show()
    sys.exit(app.exec_())
