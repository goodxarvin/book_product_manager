from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.name_clicked = False
        self.number_clicked = False
        self.buy_clicked = False
        self.sell_clicked = False
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.lineEdit_search = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_search.sizePolicy().hasHeightForWidth())
        self.lineEdit_search.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_search.setFont(font)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.gridLayout.addWidget(self.lineEdit_search, 0, 0, 1, 0)
        self.lineEdit_search.setVisible(False)

        self.pushButton_approve = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.begin_search())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_approve.sizePolicy().hasHeightForWidth())
        self.pushButton_approve.setSizePolicy(sizePolicy)
        self.pushButton_approve.setObjectName("pushButton_approve")
        self.gridLayout.addWidget(self.pushButton_approve, 1, 0, 3, 2)
        self.pushButton_approve.setVisible(False)

        self.pushButton_back = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.back())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_back.sizePolicy().hasHeightForWidth())
        self.pushButton_back.setSizePolicy(sizePolicy)
        self.pushButton_back.setObjectName("pushButton_back")
        self.gridLayout.addWidget(self.pushButton_back, 1, 2, 3, 2)
        self.pushButton_back.setVisible(False)

        self.pushButton_name = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.name_search())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_name.sizePolicy().hasHeightForWidth())
        self.pushButton_name.setSizePolicy(sizePolicy)
        self.pushButton_name.setObjectName("pushButton_name")
        self.gridLayout.addWidget(self.pushButton_name, 0, 3, 1, 1)
        self.pushButton_sell = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sell.pressed.connect(self.sell_search)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_sell.sizePolicy().hasHeightForWidth())
        self.pushButton_sell.setSizePolicy(sizePolicy)
        self.pushButton_sell.setObjectName("pushButton_sell")
        self.gridLayout.addWidget(self.pushButton_sell, 0, 0, 1, 1)
        self.pushButton_number = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.number_search())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_number.sizePolicy().hasHeightForWidth())
        self.pushButton_number.setSizePolicy(sizePolicy)
        self.pushButton_number.setObjectName("pushButton_number")
        self.gridLayout.addWidget(self.pushButton_number, 0, 2, 1, 1)
        self.pushButton_buy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_buy.pressed.connect(self.buy_search)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_buy.sizePolicy().hasHeightForWidth())
        self.pushButton_buy.setSizePolicy(sizePolicy)
        self.pushButton_buy.setObjectName("pushButton_buy")
        self.gridLayout.addWidget(self.pushButton_buy, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
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
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignHCenter |
                                QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_3.setRowStretch(0, 2)
        self.gridLayout_3.setRowStretch(1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def name_search(self):
        self.name_clicked = True
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_name.setVisible(False)
        self.pushButton_number.setVisible(False)
        self.pushButton_buy.setVisible(False)
        self.pushButton_sell.setVisible(False)
        self.lineEdit_search.setPlaceholderText(
            _translate("MainWindow", "نام کالا را وارد کنید"))
        self.lineEdit_search.setVisible(True)
        self.pushButton_approve.setVisible(True)
        self.pushButton_back.setVisible(True)

    def number_search(self):
        _translate = QtCore.QCoreApplication.translate
        self.number_clicked = True
        self.pushButton_name.setVisible(False)
        self.pushButton_number.setVisible(False)
        self.pushButton_buy.setVisible(False)
        self.pushButton_sell.setVisible(False)
        self.lineEdit_search.setPlaceholderText(
            _translate("MainWindow", "تعداد را وارد کنید"))
        self.lineEdit_search.setVisible(True)
        self.pushButton_approve.setVisible(True)
        self.pushButton_back.setVisible(True)

    def buy_search(self):
        self.buy_clicked = True
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_name.setVisible(False)
        self.pushButton_number.setVisible(False)
        self.pushButton_buy.setVisible(False)
        self.pushButton_sell.setVisible(False)
        self.lineEdit_search.setPlaceholderText(_translate(
            "MainWindow", "قیمت خرید را وارد کنید"))
        self.lineEdit_search.setVisible(True)
        self.pushButton_approve.setVisible(True)
        self.pushButton_back.setVisible(True)

    def sell_search(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_name.setVisible(False)
        self.pushButton_number.setVisible(False)
        self.pushButton_buy.setVisible(False)
        self.pushButton_sell.setVisible(False)
        self.lineEdit_search.setPlaceholderText(
            _translate("MainWindow", "قیمت فروش را وارد کنید"))
        self.lineEdit_search.setVisible(True)
        self.pushButton_approve.setVisible(True)
        self.pushButton_back.setVisible(True)

    def begin_search(self):
        if self.name_clicked:
            indicator = "name"
        elif self.number_clicked:
            indicator = "number"
        elif self.buy_clicked:
            indicator = "buy_price"
        else:
            indicator = "sell_price"
        name_indicator = self.lineEdit_search.text()
        server = sqlite3.connect("save_product.db")
        cursor = server.cursor()
        cursor.execute(f"SELECT * FROM products WHERE {indicator} = ?",
                       (name_indicator,))
        infos = cursor.fetchall()
        self.label.setText("نتایج: \n")
        result = self.label.text()
        for info in infos:
            self.label.setText(
                result + f"id: {info[0]}, نام: {info[1]}, تعداد: {info[2]}, قیمت خرید: {info[3]}, قیمت فروش: {info[4]}\n")
            result = self.label.text()

    def back(self):
        self.name_clicked = False
        self.number_clicked = False
        self.buy_clicked = False
        self.sell_clicked = False
        self.pushButton_name.setVisible(True)
        self.pushButton_number.setVisible(True)
        self.pushButton_buy.setVisible(True)
        self.pushButton_sell.setVisible(True)
        self.lineEdit_search.setVisible(False)
        self.pushButton_approve.setVisible(False)
        self.pushButton_back.setVisible(False)
        self.label.setText("")
        self.lineEdit_search.setText("")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "جست و جوی کالا"))
        self.pushButton_back.setText(_translate("MainWindow", "برگشت"))
        self.pushButton_approve.setText(
            _translate("MainWindow", "شروع جستوجو"))
        self.pushButton_name.setText(
            _translate("MainWindow", "جست و جو با نام"))
        self.pushButton_sell.setText(_translate(
            "MainWindow", "جست و جو با قیمت فزوش"))
        self.pushButton_number.setText(
            _translate("MainWindow", "جست و جو با تعداد"))
        self.pushButton_buy.setText(_translate(
            "MainWindow", "جست و جو با قیمت خرید"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
