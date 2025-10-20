from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


def database_connect():
    open("save_product.db", "a")
    server = sqlite3.connect("save_product.db")
    cursor = server.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Products(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   number INTEGER,
                   buy_price INTEGER,
                   sell_price INTEGER);
                   """)
    server.commit()
    server.close()


def insert_to_database(add):
    database_connect()
    server = sqlite3.connect("save_product.db")
    cursor = server.cursor()
    cursor.execute(
        "INSERT INTO Products (name , number, buy_price, sell_price) VALUES(?, ?, ?, ?);", add)
    server.commit()
    server.close()


class product():
    name = None
    number = None
    buy_price = None
    sell_price = None


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_buy_price = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_buy_price.sizePolicy().hasHeightForWidth())
        self.lineEdit_buy_price.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_buy_price.setFont(font)
        self.lineEdit_buy_price.setObjectName("lineEdit_buy_price")
        self.gridLayout.addWidget(self.lineEdit_buy_price, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.lineEdit_number = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_number.sizePolicy().hasHeightForWidth())
        self.lineEdit_number.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_number.setFont(font)
        self.lineEdit_number.setText("")
        self.lineEdit_number.setObjectName("lineEdit_number")
        self.gridLayout.addWidget(self.lineEdit_number, 1, 1, 1, 1)
        self.lineEdit_sell_price = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_sell_price.sizePolicy().hasHeightForWidth())
        self.lineEdit_sell_price.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_sell_price.setFont(font)
        self.lineEdit_sell_price.setObjectName("lineEdit_sell_price")
        self.gridLayout.addWidget(self.lineEdit_sell_price, 1, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setStyleSheet("text-size: 36;")
        self.lineEdit_name.setText("")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_product = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.click_add_product())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.add_product.sizePolicy().hasHeightForWidth())
        self.add_product.setSizePolicy(sizePolicy)
        self.add_product.setObjectName("add_product")
        self.verticalLayout.addWidget(self.add_product)
        self.search_product = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.click_search_product())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.search_product.sizePolicy().hasHeightForWidth())
        self.search_product.setSizePolicy(sizePolicy)
        self.search_product.setObjectName("search_product")
        self.verticalLayout.addWidget(self.search_product)
        self.delete_product = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.click_delete_product())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.delete_product.sizePolicy().hasHeightForWidth())
        self.delete_product.setSizePolicy(sizePolicy)
        self.delete_product.setObjectName("delete_product")
        self.verticalLayout.addWidget(self.delete_product)
        self.edit_product = QtWidgets.QPushButton(self.centralwidget)
        self.edit_product.pressed.connect(self.click_edit_product)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.edit_product.sizePolicy().hasHeightForWidth())
        self.edit_product.setSizePolicy(sizePolicy)
        self.edit_product.setObjectName("edit_product")
        self.verticalLayout.addWidget(self.edit_product)
        self.close_button = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.close_window())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy)
        self.close_button.setObjectName("close_button")
        self.verticalLayout.addWidget(self.close_button)
        self.gridLayout_2.addLayout(self.verticalLayout, 2, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_show = QtWidgets.QLabel(self.centralwidget)
        self.label_show.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_show.setText("")
        self.label_show.setObjectName("label_show")
        self.verticalLayout_2.addWidget(self.label_show)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1050, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def click_add_product(self):
        try:
            product_class = product()
            product_class.name = self.lineEdit_name.text()
            product_class.number = self.lineEdit_number.text()
            product_class.buy_price = self.lineEdit_buy_price.text()
            product_class.sell_price = self.lineEdit_sell_price.text()
            adding_list = [product_class.name, product_class.number,
                           product_class.buy_price, product_class.sell_price]
            insert_to_database(adding_list)
            self.label_show.setText("adding successful")
            QtCore.QTimer.singleShot(3000, self.label_show.clear)
        except Exception as e:
            print(e)

    def click_delete_product(self):
        try:
            from delete_product import Ui_MainWindow
            self.window_d = QtWidgets.QMainWindow()
            self.ui_d = Ui_MainWindow()
            self.ui_d.setupUi(self.window_d)
            self.window_d.show()
        except Exception as e:
            print(e)

    def click_edit_product(self):
        try:
            from edit_product import Ui_MainWindow
            self.window_e = QtWidgets.QMainWindow()
            self.ui_e = Ui_MainWindow()
            self.ui_e.setupUi(self.window_e)
            self.window_e.show()
        except Exception as e:
            print(e)

    def click_search_product(self):
        try:
            from search_product import Ui_MainWindow
            self.window_s = QtWidgets.QMainWindow()
            self.ui_s = Ui_MainWindow()
            self.ui_s.setupUi(self.window_s)
            self.window_s.show()
        except Exception as e:
            print(e)

    def close_window(self):
        QtWidgets.QApplication.quit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "مدیریت کتاب خانه"))
        self.lineEdit_buy_price.setPlaceholderText(
            _translate("MainWindow", "قیمت خرید "))
        self.lineEdit_number.setPlaceholderText(
            _translate("MainWindow", "تعداد"))
        self.lineEdit_sell_price.setPlaceholderText(
            _translate("MainWindow", "قیمت فروش"))
        self.lineEdit_name.setPlaceholderText(
            _translate("MainWindow", "نام کالا"))
        self.add_product.setText(_translate("MainWindow", "اضافه کردن کالا"))
        self.search_product.setText(
            _translate("MainWindow", "جست و جو ی کالا"))
        self.delete_product.setText(_translate("MainWindow", "حذف کالا"))
        self.edit_product.setText(_translate(
            "MainWindow", "تغییر مشخصات کالا"))
        self.close_button.setText(_translate("MainWindow", "خروج"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
