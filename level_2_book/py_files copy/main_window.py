from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class In_To_Database:
    def __init__(self):
        self.server = sqlite3.connect("db_files\\book_database.db")
        self.cursor = self.server.cursor()
        self.create_database()

    def create_database(self):
        open("db_files\\book_database.db", "a")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Books(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       title TEXT,
                       author TEXT,
                       isbn TEXT,
                       year_published TEXT);
                       """)
        self.server.commit()

    def insert_data(self, data):
        try:
            self.data = data
            self.cursor.execute(
                "INSERT INTO Books (title, author, isbn, year_published) VALUES (?, ?, ?, ?);", self.data)
            self.server.commit()
        except Exception as e:
            print(e)
        finally:
            self.server.close()

    def show_all_data(self):
        try:
            get_all_data = self.cursor.execute("SELECT * FROM Books;")
            all_data = get_all_data.fetchall()
        except Exception as e:
            print(e)
        finally:
            self.server.close()

        return all_data


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
        self.label_show_all = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_show_all.sizePolicy().hasHeightForWidth())
        self.label_show_all.setSizePolicy(sizePolicy)
        self.label_show_all.setStyleSheet("background-color: white;")
        self.label_show_all.setText("")
        self.label_show_all.setAlignment(QtCore.Qt.AlignCenter)
        self.label_show_all.setObjectName("label_show_all")
        self.gridLayout_2.addWidget(self.label_show_all, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_delete = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.go_to_delete())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_delete.sizePolicy().hasHeightForWidth())
        self.pushButton_delete.setSizePolicy(sizePolicy)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.gridLayout.addWidget(self.pushButton_delete, 5, 0, 1, 1)
        self.pushButton_edit = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.go_to_edit())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_edit.sizePolicy().hasHeightForWidth())
        self.pushButton_edit.setSizePolicy(sizePolicy)
        self.pushButton_edit.setObjectName("pushButton_edit")
        self.gridLayout.addWidget(self.pushButton_edit, 4, 0, 1, 1)
        self.pushButton_show_all = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_show_all.pressed.connect(self.show_all)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_show_all.sizePolicy().hasHeightForWidth())
        self.pushButton_show_all.setSizePolicy(sizePolicy)
        self.pushButton_show_all.setObjectName("pushButton_show_all")
        self.gridLayout.addWidget(self.pushButton_show_all, 3, 0, 1, 1)
        self.pushButton_search = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.go_to_search())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_search.sizePolicy().hasHeightForWidth())
        self.pushButton_search.setSizePolicy(sizePolicy)
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout.addWidget(self.pushButton_search, 2, 0, 1, 1)

        self.pushButton_clear = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.clear_label())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_clear.sizePolicy().hasHeightForWidth())
        self.pushButton_clear.setSizePolicy(sizePolicy)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout_2.addWidget(self.pushButton_clear, 1, 0, 1, 1)
        self.pushButton_clear.setVisible(False)

        self.pushButton_quit = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.quit())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_quit.sizePolicy().hasHeightForWidth())
        self.pushButton_quit.setSizePolicy(sizePolicy)
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.gridLayout.addWidget(self.pushButton_quit, 6, 0, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.add_book())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_title = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_title.sizePolicy().hasHeightForWidth())
        self.lineEdit_title.setSizePolicy(sizePolicy)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.gridLayout_3.addWidget(self.lineEdit_title, 0, 0, 1, 1)
        self.lineEdit_author = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_author.sizePolicy().hasHeightForWidth())
        self.lineEdit_author.setSizePolicy(sizePolicy)
        self.lineEdit_author.setObjectName("lineEdit_author")
        self.gridLayout_3.addWidget(self.lineEdit_author, 0, 1, 1, 1)
        self.lineEdit_year = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_year.sizePolicy().hasHeightForWidth())
        self.lineEdit_year.setSizePolicy(sizePolicy)
        self.lineEdit_year.setObjectName("lineEdit_year")
        self.gridLayout_3.addWidget(self.lineEdit_year, 1, 0, 1, 1)
        self.lineEdit_ISBN = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_ISBN.sizePolicy().hasHeightForWidth())
        self.lineEdit_ISBN.setSizePolicy(sizePolicy)
        self.lineEdit_ISBN.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_ISBN.setObjectName("lineEdit_ISBN")
        self.gridLayout_3.addWidget(self.lineEdit_ISBN, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 870, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def show_all(self):
        try:
            self.pushButton_clear.setVisible(True)
            counter = 1
            string = ""
            show = In_To_Database()
            get_data = show.show_all_data()
            font = QtGui.QFont()
            font.setPointSize(12)
            self.label_show_all.setFont(font)
            self.label_show_all.setStyleSheet("background-color: white;")
            self.label_show_all.setAlignment(QtCore.Qt.AlignLeft)
            for set_label in get_data:
                adding = f"{counter}--> title:{set_label[1]}, author:{set_label[2]}, ISBN:{set_label[3]}, published year:{set_label[4]}\n\n"
                string += adding
                counter += 1
            self.label_show_all.setText(string)

        except Exception as e:
            print(e)

    def add_book(self):
        try:
            self.name = self.lineEdit_title.text()
            self.author = self.lineEdit_author.text()
            self.isbn = self.lineEdit_ISBN.text()
            self.year = self.lineEdit_year.text()
            info_dict = [self.name, self.author, self.isbn, self.year]
            insert = In_To_Database()
            insert.insert_data(info_dict)
            self.label_show_all.setStyleSheet("""color: green;
                                              background-color: white;""")
            self.label_show_all.setText("کتاب با موفقیت اضافه شد")
            self.lineEdit_title.clear()
            self.lineEdit_author.clear()
            self.lineEdit_ISBN.clear()
            self.lineEdit_year.clear()
            QtCore.QTimer.singleShot(3000, self.label_show_all.clear)
        except Exception as e:
            print(e)

    def go_to_search(self):
        try:
            from search_book import Ui_search
            self.window_search = Ui_search()
            self.window_search.show()
        except Exception as e:
            print(e)

    def go_to_delete(self):
        try:
            from delete_book import Ui_delete_book
            self.window_del = Ui_delete_book()
            self.window_del.show()
        except Exception as e:
            print(e)

    def go_to_edit(self):
        try:
            from edit_book import Ui_edit_book
            self.window_edit = Ui_edit_book()
            self.window_edit.show()
        except Exception as e:
            print(e)

    def clear_label(self):
        self.label_show_all.clear()
        self.pushButton_clear.setVisible(False)

    def quit(self):
        QtCore.QCoreApplication.quit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "book_saver"))
        self.pushButton_clear.setText(_translate(
            "MainWindow", "ریست کردن لیبل به حالت اولیه"))
        self.pushButton_delete.setText(_translate("MainWindow", "حذف کتاب"))
        self.pushButton_edit.setText(
            _translate("MainWindow", "تغییر مشخصات کتاب"))
        self.pushButton_show_all.setText(
            _translate("MainWindow", "نمایش همه کتاب ها"))
        self.pushButton_search.setText(_translate("MainWindow", "جستجوی کتاب"))
        self.pushButton_quit.setText(_translate("MainWindow", "بستن"))
        self.pushButton_add.setText(
            _translate("MainWindow", "اضاقه کردن کتاب"))
        self.lineEdit_title.setPlaceholderText(
            _translate("MainWindow", "عنوان :"))
        self.lineEdit_author.setPlaceholderText(
            _translate("MainWindow", "نویسنده :"))
        self.lineEdit_year.setPlaceholderText(
            _translate("MainWindow", "سال انتشار :"))
        self.lineEdit_ISBN.setPlaceholderText(
            _translate("MainWindow", ": ISBN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
