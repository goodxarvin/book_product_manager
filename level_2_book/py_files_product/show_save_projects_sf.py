import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017")
db_name = my_client["resource_saver"]
resource_col = db_name["resource"]
len_show = resource_col.estimated_document_count()
amount = 4
estimated_price = 5
result_list = []


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        global len_show
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.toolButton = QtWidgets.QToolButton(
            self.centralwidget, clicked=lambda: self.close_show_save())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.toolButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton.setFont(font)
        self.toolButton.setStyleSheet("background-color: white;\n"
                                      "color: black;\n"
                                      "border-color: black;\n"
                                      "border-width: 10px;\n"
                                      "border-radius: 20px;\n"
                                      "border-style: solid;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/close/close.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(75, 75))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_2.addWidget(self.toolButton, 2, 1, 1, 1)
        self.toolButton_show_result = QtWidgets.QToolButton(
            self.centralwidget, clicked=lambda: self.show_result())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.toolButton_show_result.sizePolicy().hasHeightForWidth())
        self.toolButton_show_result.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.toolButton_show_result.setFont(font)
        self.toolButton_show_result.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_show_result.setStyleSheet("background-color: white;\n"
                                                  "color: black;\n"
                                                  "border-color: black;\n"
                                                  "border-width: 10px;\n"
                                                  "border-radius: 20px;\n"
                                                  "border-style: solid;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resource_image/show.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_show_result.setIcon(icon)
        self.toolButton_show_result.setIconSize(QtCore.QSize(75, 75))
        self.toolButton_show_result.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_show_result.setObjectName("toolButton_show_result")
        self.gridLayout_2.addWidget(self.toolButton_show_result, 1, 1, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_2.setRowStretch(0, 4)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.tableWidget_p = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_p.cellChanged.connect(self.handle_cell_change)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tableWidget_p.setFont(font)
        self.tableWidget_p.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableWidget_p.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableWidget_p.setAcceptDrops(False)
        self.tableWidget_p.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_p.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_p.setObjectName("tableWidget")
        self.tableWidget_p.setColumnCount(6)
        self.tableWidget_p.setRowCount(len_show)
        for create_row in range(len_show):
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(12)
            item.setFont(font)
            self.tableWidget_p.setVerticalHeaderItem(create_row, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(21)
        item.setFont(font)
        self.tableWidget_p.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(21)
        item.setFont(font)
        self.tableWidget_p.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_p.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(17)
        item.setFont(font)
        self.tableWidget_p.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(17)
        item.setFont(font)
        self.tableWidget_p.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(17)
        item.setFont(font)
        self.tableWidget_p.setHorizontalHeaderItem(5, item)
        for row_item in range(len_show):
            result_list.append(0)
            for clumn_item in range(6):
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(12)
                item.setFont(font)
                self.tableWidget_p.setItem(row_item, clumn_item, item)

        self.tableWidget_p.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_p.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_p.horizontalHeader().setMinimumSectionSize(49)
        self.tableWidget_p.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_p.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_p.verticalHeader().setVisible(True)
        self.tableWidget_p.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_p.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget_p, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 4)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
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

    def close_show_save(self):
        MainWindow.close()

    def show_result(self):
        global result_list
        self.label_result = QtWidgets.QLabel(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_result.setFont(font)
        self.label_result.setMouseTracking(True)
        self.label_result.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "color: green;\n"
                                        "border-color: black;\n"
                                        "border-width: 5px;\n"
                                        "border-radius: 20px;\n"
                                        "border-style: solid;")
        self.label_result.setTextFormat(QtCore.Qt.AutoText)
        self.label_result.setScaledContents(True)
        self.label_result.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_result.setObjectName("label_result")
        self.gridLayout.addWidget(self.label_result, 2, 1, 1, 1)
        self.label_result_toman = QtWidgets.QLabel(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_result_toman.setFont(font)
        self.label_result_toman.setMouseTracking(True)
        self.label_result_toman.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "color: green;\n"
                                              "border-color: black;\n"
                                              "border-width: 5px;\n"
                                              "border-radius: 20px;\n"
                                              "border-style: solid;")
        self.label_result_toman.setTextFormat(QtCore.Qt.AutoText)
        self.label_result_toman.setScaledContents(True)
        self.label_result_toman.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_result_toman.setObjectName("label_result")
        self.gridLayout.addWidget(self.label_result_toman, 3, 1, 1, 1)
        try:
            total_result = 0
            for prices in result_list:
                total_result += prices
            self.label_result.setText(f"قیمت نهایی: {str(total_result)} ریال")
            total_result_toman = int(total_result/10)
            self.label_result_toman.setText(
                f"قیمت نهایی: {str(total_result_toman)} تومان")
        except:
            self.label_result.setText("error")
            self.label_result_toman.setText("error")

    def handle_cell_change(self, row, column):
        num_saved = self.tableWidget_p.item(row, column).text()
        self.row = row
        test_amount = self.tableWidget_p.item(row, 4)
        if test_amount and len(test_amount.text()) > 0 and column != 5:
            amount = self.tableWidget_p.item(self.row, 4).text()
            unit_price = self.tableWidget_p.item(self.row, 2).text()
            try:
                int_unit_price = int(unit_price)
                int_amount = int(amount)
                total_price = int_unit_price * int_amount
                _translate = QtCore.QCoreApplication.translate
                result_list[row] = total_price
                item = self.tableWidget_p.item(row, 5)
                item.setText(_translate(
                    "MainWindow", f"{str(total_price)} ریال"))
            except:
                item = self.tableWidget_p.item(row, 5)
                item.setText("error")

    def retranslateUi(self, MainWindow):
        global len_show
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "final_factor"))
        for give_number in range(len_show):
            item = self.tableWidget_p.verticalHeaderItem(give_number)
            item.setText(_translate(
                "MainWindow", f"  عملیات ذخیره شده{give_number+1}"))
        self.toolButton.setText(_translate("MainWindow", "    بستن"))
        self.toolButton_show_result.setText(
            _translate("Mainwindow", "نمایش نتیجه"))
        item = self.tableWidget_p.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "نام عملیات"))
        item = self.tableWidget_p.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "کد عملیات"))
        item = self.tableWidget_p.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "(ریال)قیمت واحد"))
        item = self.tableWidget_p.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "واحد اندازه گیری"))
        item = self.tableWidget_p.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "میزان"))
        item = self.tableWidget_p.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "جمع کل"))
        row_item = 0
        for items in resource_col.find():
            clumn_item = 0
            for item_value in list(items):
                if item_value != "_id":
                    item = self.tableWidget_p.item(row_item, clumn_item)
                    item.setText(_translate(
                        "MainWindow", items[item_value]))
                    clumn_item += 1
            row_item += 1


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

if __name__ == "__main__":
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
