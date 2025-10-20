from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView
import sqlite3
import os


class data_base_actions:
    def __init__(self):
        self.folder_path = "db_files"
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
        self.server = sqlite3.connect("db_files\\book_database.db")
        self.cursor = self.server.cursor()
        self.create_database()

    def create_database(self):
        file = open("db_files\\book_database.db", "a")
        file.close()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Books(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT,
                            writer TEXT,
                            ISBN TEXT,
                            year_published TEXT);
                            """)
        self.server.commit()

    def insert_into(self, data):
        try:
            self.data = data
            self.cursor.execute(
                "INSERT INTO Books (title, writer, ISBN, year_published) VALUES (?, ?, ?, ?);", self.data)
            self.server.commit()
        except Exception as e:
            print(e)
        finally:
            self.server.close()

    def show_all_datas(self):
        try:
            self.cursor.execute("SELECT * FROM Books;")
            all_data = self.cursor.fetchall()
            return all_data

        except Exception as e:
            print(e)

        finally:
            self.server.close()


class Ui_MainWindow_book(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.db_path = "db_files"
        self.db_file = "book_database.db"
        self.file_path = os.path.join(self.db_path, self.db_file)
        self.setObjectName("MainWindow_book")
        self.resize(1100, 750)
        self.setStyleSheet("background-color: rgb(154, 154, 154);")
        self.centralwidget = QtWidgets.QWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_main_window = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_main_window.setObjectName("gridLayout_main_window")
        self.gridLayout_buttons = QtWidgets.QGridLayout()
        self.gridLayout_buttons.setObjectName("gridLayout_buttons")
        self.pushButton_edit_book = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.edit_book_clicked())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_edit_book.sizePolicy().hasHeightForWidth())
        self.pushButton_edit_book.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_edit_book.setFont(font)
        self.pushButton_edit_book.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_edit_book.setStyleSheet("background-color: green;\n"
                                                "color: white;\n"
                                                "border-color: white;\n"
                                                "border-radius: 30px;\n"
                                                "border-width: 5px;\n"
                                                "border-style: solid;\n"
                                                "padding: 15px;")
        self.pushButton_edit_book.setObjectName("pushButton_edit_book")
        self.gridLayout_buttons.addWidget(
            self.pushButton_edit_book, 4, 0, 1, 1)
        self.pushButto_search_book = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.search_book_clicked())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButto_search_book.sizePolicy().hasHeightForWidth())
        self.pushButto_search_book.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButto_search_book.setFont(font)
        self.pushButto_search_book.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButto_search_book.setStyleSheet("background-color: green;\n"
                                                 "color: white;\n"
                                                 "border-color: white;\n"
                                                 "border-radius: 30px;\n"
                                                 "border-width: 5px;\n"
                                                 "border-style: solid;\n"
                                                 "padding: 15px;")
        self.pushButto_search_book.setObjectName("pushButto_search_book")
        self.gridLayout_buttons.addWidget(
            self.pushButto_search_book, 3, 0, 1, 1)
        self.pushButton_close_ui = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.close_window_clicked())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_close_ui.sizePolicy().hasHeightForWidth())
        self.pushButton_close_ui.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_close_ui.setFont(font)
        self.pushButton_close_ui.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_close_ui.setStyleSheet("background-color: green;\n"
                                               "color: white;\n"
                                               "border-color: white;\n"
                                               "border-radius: 30px;\n"
                                               "border-width: 5px;\n"
                                               "border-style: solid;\n"
                                               "padding: 15px;")
        self.pushButton_close_ui.setObjectName("pushButton_close_ui")
        self.gridLayout_buttons.addWidget(self.pushButton_close_ui, 6, 0, 1, 1)
        self.pushButton_show_all_books = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.show_all_books_clicked())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_show_all_books.sizePolicy().hasHeightForWidth())
        self.pushButton_show_all_books.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_show_all_books.setFont(font)
        self.pushButton_show_all_books.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_show_all_books.setStyleSheet("background-color: green;\n"
                                                     "color: white;\n"
                                                     "border-color: white;\n"
                                                     "border-radius: 30px;\n"
                                                     "border-width: 5px;\n"
                                                     "border-style: solid;\n"
                                                     "padding: 15px;")
        self.pushButton_show_all_books.setObjectName(
            "pushButton_show_all_books")
        self.gridLayout_buttons.addWidget(
            self.pushButton_show_all_books, 2, 0, 1, 1)
        self.pushButton_add_book = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add_book.pressed.connect(self.add_book_clicked)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_add_book.sizePolicy().hasHeightForWidth())
        self.pushButton_add_book.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_add_book.setFont(font)
        self.pushButton_add_book.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_add_book.setStyleSheet("background-color: green;\n"
                                               "color: white;\n"
                                               "border-color: white;\n"
                                               "border-radius: 30px;\n"
                                               "border-width: 5px;\n"
                                               "border-style: solid;\n"
                                               "padding: 15px;")
        self.pushButton_add_book.setObjectName("pushButton_add_book")
        self.gridLayout_buttons.addWidget(self.pushButton_add_book, 1, 0, 1, 1)
        self.pushButton_delete_book = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.delete_book_clicked())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_delete_book.sizePolicy().hasHeightForWidth())
        self.pushButton_delete_book.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_delete_book.setFont(font)
        self.pushButton_delete_book.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_delete_book.setStyleSheet("background-color: green;\n"
                                                  "color: white;\n"
                                                  "border-color: white;\n"
                                                  "border-radius: 30px;\n"
                                                  "border-width: 5px;\n"
                                                  "border-style: solid;\n"
                                                  "padding: 15px;")
        self.pushButton_delete_book.setObjectName("pushButton_delete_book")

        self.pushButton_clear_show_all = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.clear_table_clicked())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_clear_show_all.sizePolicy().hasHeightForWidth())
        self.pushButton_clear_show_all.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_clear_show_all.setFont(font)
        self.pushButton_clear_show_all.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_clear_show_all.setStyleSheet("background-color: green;\n"
                                                     "color: white;\n"
                                                     "border-color: white;\n"
                                                     "border-radius: 30px;\n"
                                                     "border-width: 5px;\n"
                                                     "border-style: solid;\n"
                                                     "padding: 15px;")
        self.pushButton_clear_show_all.setObjectName(
            "pushButton_clear_show_all")
        self.pushButton_clear_show_all.hide()

        self.gridLayout_buttons.addWidget(
            self.pushButton_delete_book, 5, 0, 1, 1)
        self.gridLayout_main_window.addLayout(
            self.gridLayout_buttons, 2, 1, 1, 1)
        self.gridLayout_label = QtWidgets.QGridLayout()
        self.gridLayout_label.setObjectName("gridLayout_label")

        self.gridLayout_label.addWidget(
            self.pushButton_clear_show_all, 2, 0, 1, 1)

        self.label = QtWidgets.QLabel(self.centralwidget)
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
        self.label.setStyleSheet("background-color: rgb(154, 154, 154);\n"
                                 "border-color: black;\n"
                                 "border-radius: 30px;\n"
                                 "border-width: 5px;\n"
                                 "border-style: solid;\n"
                                 "padding: 15px;\n"
                                 "color: white;")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_label.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_main_window.addLayout(
            self.gridLayout_label, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_main_window.addItem(spacerItem, 1, 1, 1, 1)
        self.gridLayout_lineEdits = QtWidgets.QGridLayout()
        self.gridLayout_lineEdits.setObjectName("gridLayout_lineEdits")
        self.lineEdit_year = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_year.sizePolicy().hasHeightForWidth())
        self.lineEdit_year.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_year.setFont(font)
        self.lineEdit_year.setStyleSheet("background-color: white;\n"
                                         "border-color: black;\n"
                                         "border-radius: 30px;\n"
                                         "border-width: 5px;\n"
                                         "border-style: solid;\n"
                                         "padding: 15px;")
        self.lineEdit_year.setObjectName("lineEdit_year")
        self.gridLayout_lineEdits.addWidget(self.lineEdit_year, 3, 0, 1, 1)
        self.lineEdit_ISBN = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_ISBN.sizePolicy().hasHeightForWidth())
        self.lineEdit_ISBN.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_ISBN.setFont(font)
        self.lineEdit_ISBN.setStyleSheet("background-color: white;\n"
                                         "border-color: black;\n"
                                         "border-radius: 30px;\n"
                                         "border-width: 5px;\n"
                                         "border-style: solid;\n"
                                         "padding: 15px;")
        self.lineEdit_ISBN.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_ISBN.setObjectName("lineEdit_ISBN")
        self.gridLayout_lineEdits.addWidget(self.lineEdit_ISBN, 3, 1, 1, 1)
        self.lineEdit_writer = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_writer.sizePolicy().hasHeightForWidth())
        self.lineEdit_writer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_writer.setFont(font)
        self.lineEdit_writer.setStyleSheet("background-color: white;\n"
                                           "border-color: black;\n"
                                           "border-radius: 30px;\n"
                                           "border-width: 5px;\n"
                                           "border-style: solid;\n"
                                           "padding: 15px;")
        self.lineEdit_writer.setObjectName("lineEdit_writer")
        self.gridLayout_lineEdits.addWidget(self.lineEdit_writer, 0, 1, 1, 1)
        self.lineEdit_title = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_title.sizePolicy().hasHeightForWidth())
        self.lineEdit_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_title.setFont(font)
        self.lineEdit_title.setStyleSheet("background-color: white;\n"
                                          "border-width: 5px;\n"
                                          "border-color: black;\n"
                                          "border-radius: 30px;\n"
                                          "border-style: solid;\n"
                                          "padding: 15px;")
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.gridLayout_lineEdits.addWidget(self.lineEdit_title, 0, 0, 1, 1)
        self.gridLayout_main_window.addLayout(
            self.gridLayout_lineEdits, 0, 0, 1, 2)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.show_all_table = QTableWidget()
        self.show_all_table.setColumnCount(5)
        self.show_all_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.show_all_table.setSelectionBehavior(QAbstractItemView.SelectItems)
        column_header = self.show_all_table.horizontalHeader()
        column_header.setSectionResizeMode(QHeaderView.Stretch)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.show_all_table.setFont(font)
        self.gridLayout_label.addWidget(
            self.show_all_table, 1, 0, 1, 1)
        self.show_all_table.hide()

        self.field_empty_message = QMessageBox()
        self.field_empty_message.setIcon(QMessageBox.Information)
        self.field_empty_message.setWindowTitle("empty_entry...")
        self.field_empty_message.setStandardButtons(QMessageBox.Ok)

        self.no_database_message = QMessageBox()
        self.no_database_message.setIcon(QMessageBox.Information)
        self.no_database_message.setWindowTitle("databas_no_exist...")
        self.no_database_message.setText("هیچ دیتابیسی برای انجام عملیات ها وجود ندارد , لطفا ابتدا "
                                         "با پر کردن ورودی های نام , نویسنده, ISBN و سال انتشار "
                                         "و سپس زدن دکمه ی (اضافه کردن کتاب) ابتدا یک دیتابیس برای کتاب ها ایجاد کنید")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def reset_to_default_label(self):
        self.label.clear()
        self.label.setStyleSheet("background-color: rgb(154, 154, 154);\n"
                                 "border-color: black;\n"
                                 "border-radius: 30px;\n"
                                 "border-width: 5px;\n"
                                 "border-style: solid;\n"
                                 "padding: 15px;\n"
                                 "color: white;")

    def resize_to_default(self):
        self.gridLayout_label.setRowStretch(1, 0)
        self.gridLayout_label.setRowStretch(2, 0)

    def add_book_clicked(self):
        try:
            title = self.lineEdit_title.text()
            writer = self.lineEdit_writer.text()
            ISBN = self.lineEdit_ISBN.text()
            year = self.lineEdit_year.text()
            data_to_add = (title, writer, ISBN, year)
            if title and writer and ISBN and year:
                add_data = data_base_actions()
                add_data.insert_into(data_to_add)
                self.lineEdit_title.clear()
                self.lineEdit_writer.clear()
                self.lineEdit_ISBN.clear()
                self.lineEdit_year.clear()
                self.resize_to_default()
                self.show_all_table.hide()
                self.pushButton_clear_show_all.hide()
                self.label.show()
                self.label.setStyleSheet("background-color: white;\n"
                                         "border-color: green;\n"
                                         "border-radius: 30px;\n"
                                         "border-width: 5px;\n"
                                         "border-style: solid;\n"
                                         "padding: 15px;\n"
                                         "color: green;")
                self.label.setText("کتاب با موفقیت اضافه شد")
                QtCore.QTimer.singleShot(3000, self.reset_to_default_label)
            else:
                dict_data = {"(تایتل)": title, "(نویسنده)": writer,
                             "(ISBN)": ISBN, "(سال انتشار)": year}
                empty_string = ""
                for empty in dict_data:
                    if not dict_data[empty]:
                        empty_string += f"{empty} و "

                empty_string = empty_string[:-3]
                self.field_empty_message.setText(
                    f"شما مقداری برای {empty_string} وارد نکرده اید لطفا برای اضافه کردن کتاب همه فیلد هارا پر کنید")
                self.field_empty_message.exec_()

        except Exception as e:
            print(e)

    def show_all_books_clicked(self):
        if os.path.exists(self.file_path):
            try:
                self.show_all_table.setHorizontalHeaderLabels(
                    ["ID", "نام", "نویسنده", "ISBN", "سال انتشار"])
                data = data_base_actions()
                show_all_data = data.show_all_datas()
                row_count = len(show_all_data)
                self.show_all_table.setRowCount(row_count)
                for row, every_data in enumerate(show_all_data):
                    for column, data in enumerate(every_data):
                        item = QTableWidgetItem(str(data))
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.show_all_table.setItem(row, column, item)

                self.gridLayout_label.setRowStretch(1, 5)
                self.gridLayout_label.setRowStretch(2, 1)
                self.show_all_table.show()
                self.pushButton_clear_show_all.show()
                self.label.hide()
            except Exception as e:
                print(e)
        else:
            self.no_database_message.exec_()

    def search_book_clicked(self):
        if os.path.exists(self.file_path):
            try:
                from search_window import Ui_search_widget
                self.window_s = Ui_search_widget()
                self.window_s.show()
            except Exception as e:
                print(e)
        else:
            self.no_database_message.exec_()

    def delete_book_clicked(self):
        if os.path.exists(self.file_path):
            try:
                from delete_window import Ui_delete_book
                self.window_d = Ui_delete_book()
                self.window_d.show()
            except Exception as e:
                print(e)
        else:
            self.no_database_message.exec_()

    def edit_book_clicked(self):
        if os.path.exists(self.file_path):
            try:
                from edit_window import Ui_edit_window
                self.window_e = Ui_edit_window()
                self.window_e.show()
            except Exception as e:
                print(e)
        else:
            self.no_database_message.exec_()

    def clear_table_clicked(self):
        self.resize_to_default()
        self.pushButton_clear_show_all.hide()
        self.show_all_table.clear()
        self.show_all_table.hide()
        self.label.show()

    def close_window_clicked(self):
        QtCore.QCoreApplication.quit()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(
            _translate("MainWindow_book", "main_window"))
        self.pushButton_edit_book.setText(
            _translate("MainWindow_book", "تغییر مشخصات کتاب"))
        self.pushButto_search_book.setText(
            _translate("MainWindow_book", "جستوجوی کتاب"))
        self.pushButton_clear_show_all.setText(
            _translate("MainWindow_book", "بستن جدول بالا"))
        self.pushButton_close_ui.setText(
            _translate("MainWindow_book", "بستن برنامه"))
        self.pushButton_show_all_books.setText(
            _translate("MainWindow_book", "نمایش همه کتاب ها"))
        self.pushButton_add_book.setText(
            _translate("MainWindow_book", "اضافه کردن کتاب"))
        self.pushButton_delete_book.setText(
            _translate("MainWindow_book", "حذف کتاب"))
        self.lineEdit_year.setPlaceholderText(
            _translate("MainWindow_book", "سال انتشار:"))
        self.lineEdit_ISBN.setPlaceholderText(
            _translate("MainWindow_book", ":ISBN"))
        self.lineEdit_writer.setPlaceholderText(
            _translate("MainWindow_book", "نویسنده:"))
        self.lineEdit_title.setPlaceholderText(
            _translate("MainWindow_book", "عنوان:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_book = Ui_MainWindow_book()
    MainWindow_book.show()
    sys.exit(app.exec_())
