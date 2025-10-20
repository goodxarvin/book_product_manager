from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import re


class Ui_delete_book(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self._translate = QtCore.QCoreApplication.translate
        self.server = sqlite3.connect("db_files\\book_database.db")
        self.book_cursor = self.server.cursor()
        self.setObjectName("delete_book")
        self.resize(810, 410)
        self.setStyleSheet("background-color: rgb(154, 154, 154);")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_lineEdit = QtWidgets.QGridLayout()
        self.gridLayout_lineEdit.setObjectName("gridLayout_lineEdit")
        self.pushButton_start_search = QtWidgets.QPushButton(
            self, clicked=lambda: self.start_search_clicked())
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
        self.lineEdit = QtWidgets.QLineEdit(self)
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
        self.listWidget_show_found_books = QtWidgets.QListWidget(self)
        self.listWidget_show_found_books.itemSelectionChanged.connect(
            self.show_select_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.listWidget_show_found_books.sizePolicy().hasHeightForWidth())
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_show_found_books.setFont(font)
        self.listWidget_show_found_books.setSizePolicy(sizePolicy)
        self.listWidget_show_found_books.setStyleSheet("background-color: white;\n"
                                                       "border-color: black;\n"
                                                       "border-width: 5px;\n"
                                                       "border-radius: 30px;\n"
                                                       "padding: 10px;\n"
                                                       "border-style: solid;")
        self.listWidget_show_found_books.setLayoutDirection(
            QtCore.Qt.RightToLeft)
        self.listWidget_show_found_books.setObjectName(
            "listWidget_show_found_books")
        self.gridLayout_list_widget.addWidget(
            self.listWidget_show_found_books, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_list_widget, 1, 0, 1, 1)
        self.gridLayout_buttons_p1 = QtWidgets.QGridLayout()
        self.gridLayout_buttons_p1.setObjectName("gridLayout_buttons_p1")
        self.pushButton_select_book = QtWidgets.QPushButton(
            self, clicked=lambda: self.button_selected_clicked())
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
        self.pushButton_select_book.hide()
        self.gridLayout_buttons_p1.addWidget(
            self.pushButton_select_book, 0, 0, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(
            self, clicked=lambda: self.close_clicked())
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
        self.gridLayout.addLayout(self.gridLayout_buttons_p1, 3, 0, 1, 1)
        self.gridLayout_label = QtWidgets.QGridLayout()
        self.gridLayout_label.setObjectName("gridLayout_label")
        self.label_show_approve_book = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_show_approve_book.sizePolicy().hasHeightForWidth())
        self.label_show_approve_book.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_show_approve_book.setFont(font)
        self.label_show_approve_book.setStyleSheet("background-color: rgb(154, 154, 154);\n"
                                                   "border-color: black;\n"
                                                   "border-width: 5px;\n"
                                                   "border-radius: 30px;\n"
                                                   "padding: 10px;\n"
                                                   "border-style: solid;")
        self.label_show_approve_book.setText("")
        self.label_show_approve_book.setObjectName("label_show_approve_book")
        self.label_show_approve_book.hide()
        self.gridLayout_label.addWidget(
            self.label_show_approve_book, 0, 0, 1, 1)

        self.label_notif_handler = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_notif_handler.sizePolicy().hasHeightForWidth())
        self.label_notif_handler.setSizePolicy(sizePolicy)
        self.label_notif_handler.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_notif_handler.setFont(font)
        self.label_notif_handler.setText("")
        self.label_notif_handler.setObjectName("label_notif_handler")
        self.label_notif_handler.hide()

        self.gridLayout_buttons_p2 = QtWidgets.QGridLayout()
        self.gridLayout_buttons_p2.setObjectName("gridLayout_buttons_p2")
        self.pushButton_approve_book = QtWidgets.QPushButton(
            self, clicked=lambda: self.approve_delete_clicked())
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
        self.pushButton_approve_book.hide()
        self.gridLayout_buttons_p2.addWidget(
            self.pushButton_approve_book, 0, 0, 1, 1)

        self.pushButton_back = QtWidgets.QPushButton(
            self, clicked=lambda: self.back_clicked())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_back.sizePolicy().hasHeightForWidth())
        self.pushButton_back.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_back.setStyleSheet("background-color: rgb(170, 0, 0);\n"
                                           "color: white;\n"
                                           "border-color: white;\n"
                                           "border-width: 5px;\n"
                                           "border-radius: 30px;\n"
                                           "border-style: solid;\n"
                                           "padding: 10px;")
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_back.hide()
        self.gridLayout_buttons_p2.addWidget(self.pushButton_back, 0, 1, 1, 1)

        self.messageBox_em = QMessageBox()
        self.messageBox_em.setIcon(QMessageBox.Information)
        self.messageBox_em.setWindowTitle("empty_entry...")
        self.messageBox_em.setText(
            "شما هیچ چیزی در ورودی برای جستوجوی کتاب وارد نکرده اید")
        self.messageBox_em.setStandardButtons(QMessageBox.Ok)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 2)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(5, 0)
        self.gridLayout.setRowStretch(6, 0)
        self.gridLayout.addLayout(self.gridLayout_label, 5, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_buttons_p2, 6, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def reset_handler_label(self):
        self.label_notif_handler.hide()
        self.gridLayout.removeWidget(self.label_notif_handler)
        self.gridLayout.setRowStretch(2, 0)

    def show_select_book(self):
        if self.listWidget_show_found_books.selectedItems():
            self.pushButton_select_book.show()
        else:
            self.pushButton_select_book.hide()

    def start_search_clicked(self):
        check_empty_lineEdit = self.lineEdit.text()
        if check_empty_lineEdit:
            self.listWidget_show_found_books.clear()
            self.book_cursor.execute(
                "SELECT * FROM Books WHERE id LIKE ? OR title LIKE ? OR writer LIKE ? OR ISBN LIKE ? OR year_published LIKE ?",
                (f"%{check_empty_lineEdit}%", f"%{check_empty_lineEdit}%", f"%{check_empty_lineEdit}%",
                 f"%{check_empty_lineEdit}%", f"%{check_empty_lineEdit}%"))
            found_data = self.book_cursor.fetchall()
            if found_data:
                for index, item in enumerate(found_data):
                    self.listWidget_show_found_books.addItem(
                        f"کتاب شماره{index+1}:\nid: {item[0]}\nنام: {item[1]}, نویسنده: {item[2]}, سال انتشار: {item[4]}\nISBN: {item[3]}\n")
            else:
                self.pushButton_select_book.hide()
                self.lineEdit.clear()
                self.label_notif_handler.setStyleSheet("background-color: red;\n"
                                                       "color: white;\n"
                                                       "border-radius: 30px;\n"
                                                       "padding: 10px;\n"
                                                       "border-style: solid;")
                self.label_notif_handler.setText(self._translate(
                    "edit_book", "جستوجوی شما نتیجه ای نداشت"))
                self.gridLayout.addWidget(
                    self.label_notif_handler, 2, 0, 1, 1)
                self.gridLayout.setRowStretch(2, 1)
                self.label_notif_handler.show()
                QtCore.QTimer.singleShot(3000, self.reset_handler_label)
        else:
            self.messageBox_em.exec_()

    def button_selected_clicked(self):
        selected_item = self.listWidget_show_found_books.currentItem()
        if selected_item:
            self.listWidget_show_found_books.hide()
            self.pushButton_close.hide()
            self.pushButton_select_book.hide()
            self.pushButton_start_search.hide()
            self.lineEdit.hide()
            self.label_notif_handler.hide()
            self.gridLayout.setRowStretch(0, 0)
            self.gridLayout.setRowStretch(1, 0)
            self.gridLayout.setRowStretch(2, 0)
            self.gridLayout.setRowStretch(3, 0)
            self.label_show_approve_book.show()
            self.pushButton_approve_book.show()
            self.pushButton_back.show()
            self.selected_item_text = selected_item.text()[13:]
            self.label_show_approve_book.setText(self._translate(
                "delete_book", f"کتاب مورد نظر برای حذف:\n{self.selected_item_text}آیا از حذف این کتاب مطمعن هستید؟"))
        else:
            self.gridLayout.setRowStretch(2, 1)
            self.gridLayout.addWidget(self.label_notif_handler, 2, 0, 1, 1)
            self.label_notif_handler.show()
            self.label_notif_handler.setStyleSheet("background-color: red;\n"
                                                   "color: white;\n"
                                                   "border-radius: 30px;\n"
                                                   "padding: 10px;\n"
                                                   "border-style: solid;")
            self.label_notif_handler.setText(self._translate(
                "delete_book", "شما هیچ کتابی از لیست بالا انتخاب نکرده اید , لطفا یک کتاب را انتخاب کنید"))
            QtCore.QTimer.singleShot(3000, self.reset_handler_label)

    def approve_delete_clicked(self):
        try:
            deleting_id = re.search(r"id: (\d+)", self.selected_item_text)
            deleting_id = deleting_id.group(1)
            self.book_cursor.execute(
                "DELETE FROM Books WHERE id=?", (deleting_id,))
            self.server.commit()
            self.pushButton_approve_book.hide()
            self.label_show_approve_book.hide()
            self.pushButton_back.hide()
            self.label_show_approve_book.clear()
            self.gridLayout.setRowStretch(0, 1)
            self.gridLayout.setRowStretch(1, 2)
            self.gridLayout.setRowStretch(3, 1)
            self.gridLayout.setRowStretch(5, 0)
            self.gridLayout.setRowStretch(6, 0)
            self.listWidget_show_found_books.show()
            self.pushButton_close.show()
            self.pushButton_start_search.show()
            self.lineEdit.show()
            self.listWidget_show_found_books.clear()
            self.lineEdit.clear()
            self.label_notif_handler.setStyleSheet("background-color: green;\n"
                                                   "color: white;\n"
                                                   "border-radius: 30px;\n"
                                                   "padding: 10px;")
            self.label_notif_handler.setText("کتاب با موفقیت حذف شد :)")
            self.gridLayout.addWidget(self.label_notif_handler, 2, 0, 1, 1)
            self.gridLayout.setRowStretch(2, 1)
            self.label_notif_handler.show()
            QtCore.QTimer.singleShot(3000, self.reset_handler_label)
        except Exception as e:
            print(e)

    def back_clicked(self):
        self.label_show_approve_book.hide()
        self.pushButton_approve_book.hide()
        self.pushButton_back.hide()
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 2)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(5, 0)
        self.gridLayout.setRowStretch(6, 0)
        self.lineEdit.show()
        self.pushButton_close.show()
        self.listWidget_show_found_books.show()
        self.pushButton_select_book.show()
        self.pushButton_start_search.show()
        self.listWidget_show_found_books.clearSelection()

    def close_clicked(self):
        self.server.close()
        self.close()

    def retranslateUi(self):
        self.setWindowTitle(
            self._translate("delete_book", "delete_book"))
        self.pushButton_start_search.setText(
            self._translate("delete_book", "شروع جستوجو"))
        self.lineEdit.setPlaceholderText(self._translate(
            "delete_book", "لطفا کلمه ای را برای پیدا کردن کتابی که می خواهید حذف کنید ایتجا وارد کنید"))
        self.pushButton_select_book.setText(
            self._translate("delete_book", "انتخاب کتاب"))
        self.pushButton_close.setText(self._translate("delete_book", "بستن"))
        self.pushButton_back.setText(self._translate(
            "delete_book", "برگشت به صفحه اول"))
        self.pushButton_approve_book.setText(
            self._translate("delete_book", "تایید و حدف کتاب"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    delete_book = Ui_delete_book()
    delete_book.show()
    sys.exit(app.exec_())
