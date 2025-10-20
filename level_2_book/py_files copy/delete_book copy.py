from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import re


class Ui_delete_book(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, delete_book):
        delete_book.setObjectName("delete_book")
        delete_book.resize(780, 450)
        self.gridLayout_4 = QtWidgets.QGridLayout(delete_book)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_search = QtWidgets.QPushButton(
            delete_book, clicked=lambda: self.search_func())
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
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout_3.addWidget(self.pushButton_search, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(delete_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 2)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(delete_book)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_delete = QtWidgets.QPushButton(delete_book)
        self.pushButton_delete.pressed.connect(self.deleting)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_delete.sizePolicy().hasHeightForWidth())
        self.pushButton_delete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.gridLayout_2.addWidget(self.pushButton_delete, 0, 0, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(
            delete_book, clicked=lambda: self.close_window())
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
        self.gridLayout_2.addWidget(self.pushButton_close, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 3, 0, 1, 1)

        self.message_box_em = QMessageBox()
        self.message_box_em.setIcon(QMessageBox.Information)
        self.message_box_em.setWindowTitle("entry is empty...")
        self.message_box_em.setText("شما در ورودی چیزی وارد نکرده اید...")
        self.message_box_em.setStandardButtons(QMessageBox.Ok)

        self.message_box_nf = QMessageBox()
        self.message_box_nf.setIcon(QMessageBox.Information)
        self.message_box_nf.setWindowTitle("no result found...")
        self.message_box_nf.setText("جستوجوی شما نتیجه ای نداشت...")
        self.message_box_nf.setStandardButtons(QMessageBox.Ok)

        self.label_em = QtWidgets.QLabel(delete_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_em.sizePolicy().hasHeightForWidth())
        self.label_em.setSizePolicy(sizePolicy)
        self.label_em.setStyleSheet("""background-color: red;
                                       color: white;""")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_em.setFont(font)
        self.label_em.setText("")
        self.label_em.setAlignment(QtCore.Qt.AlignCenter)
        self.label_em.setObjectName("label_em")
        self.gridLayout_4.addWidget(self.label_em, 1, 0, 1, 1)
        self.label_em.setText("شما در ورودی بالا چیزی وارد نکرده اید")
        self.label_em.hide()

        self.label_success = QtWidgets.QLabel(delete_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_success.sizePolicy().hasHeightForWidth())
        self.label_success.setSizePolicy(sizePolicy)
        self.label_success.setStyleSheet("""background-color: green;
                                       color: white;""")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_success.setFont(font)
        self.label_success.setText("")
        self.label_success.setAlignment(QtCore.Qt.AlignCenter)
        self.label_success.setObjectName("label_success")
        self.label_success.hide()

        self.label_ns = QtWidgets.QLabel(delete_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_ns.sizePolicy().hasHeightForWidth())
        self.label_ns.setSizePolicy(sizePolicy)
        self.label_ns.setStyleSheet("""background-color: red;
                                       color: white;""")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ns.setFont(font)
        self.label_ns.setText("")
        self.label_ns.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ns.setObjectName("label_ns")
        self.label_ns.hide()

        self.retranslateUi(delete_book)
        QtCore.QMetaObject.connectSlotsByName(delete_book)

    def hide_label(self, label_name):
        label_name.hide()
        self.gridLayout.removeWidget(label_name)
        self.gridLayout.setRowStretch(0, 5)
        self.gridLayout.setRowStretch(1, 0)

    def search_func(self):
        try:
            text = self.lineEdit.text()
            self.server = sqlite3.connect("db_files\\book_database.db")
            self.cursor = self.server.cursor()
            self.cursor.execute(
                "SELECT * FROM Books WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ? OR year_published LIKE ?",
                (f"%{text}%", f"%{text}%", f"%{text}%", f"%{text}%"))
            self.search_key = self.cursor.fetchall()
            if text and self.search_key:
                self.listWidget.clear()
                for index, row in enumerate(self.search_key):
                    self.listWidget.addItem(
                        f"{index+1}---> title:{row[1]}, author:{row[2]}, isbn:{row[3]}, year_published:{row[4]}\n")
            elif text:
                self.message_box_nf.exec_()
                self.lineEdit.clear()
                self.server.close()
            else:
                self.listWidget.clear()
                self.label_em.show()
                QtCore.QTimer.singleShot(
                    3000, lambda: self.hide_label(self.label_em))
                self.server.close()

        except Exception as e:
            print(e)

    def deleting(self):
        try:
            selected = self.listWidget.currentItem()
            if selected:
                deleting_item_all = selected.text()
                match_item = re.search(r"title:([^,]+)", deleting_item_all)
                deleting_item_title = match_item.group(1).strip()
                self.cursor.execute(
                    "DELETE FROM Books WHERE title = ?", (deleting_item_title,))
                self.server.commit()
                self.gridLayout.addWidget(self.label_success, 1, 1, 1, 1)
                self.gridLayout.setRowStretch(0, 4)
                self.gridLayout.setRowStretch(1, 1)
                self.label_success.setText("حذف کتاب با موفقیت انجام شد")
                self.label_success.show()
                QtCore.QTimer.singleShot(
                    3000, lambda: self.hide_label(self.label_success))
                self.listWidget.clear()
                self.lineEdit.clear()
                self.server.close()
            elif not selected and self.listWidget.count() != 0:
                self.gridLayout.addWidget(self.label_ns, 1, 1, 1, 1)
                self.gridLayout.setRowStretch(0, 4)
                self.gridLayout.setRowStretch(1, 1)
                self.label_ns.setText(
                    "لطفا از لیست بالا یک کتاب را برای حذف انتخاب کنید")
                self.label_ns.show()
                QtCore.QTimer.singleShot(
                    3000, lambda: self.hide_label(self.label_ns))
            else:
                self.label_em.show()
                QtCore.QTimer.singleShot(
                    3000, lambda: self.hide_label(self.label_em))
        except Exception as e:
            print(e)

    def close_window(self):
        try:
            self.close()
        except Exception as e:
            print(e)

    def retranslateUi(self, delete_book):
        _translate = QtCore.QCoreApplication.translate
        delete_book.setWindowTitle(_translate("delete_book", "delete_book"))
        self.pushButton_search.setText(
            _translate("delete_book", "  شروع جستوجو"))
        self.lineEdit.setPlaceholderText(_translate(
            "delete_book", " لطفا اطلاعاتی از کتاب را برای جستوجو و حذف کتاب اینجا وارد کنید"))
        self.pushButton_delete.setText(_translate("delete_book", "حذف کتاب"))
        self.pushButton_close.setText(_translate("delete_book", "بستن"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    delete_book = Ui_delete_book()
    delete_book.show()
    sys.exit(app.exec_())
