import project
from PyQt5 import QtCore, QtGui, QtWidgets
import factor_register


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(1016, 714)
        main_window.setLayoutDirection(QtCore.Qt.LeftToRight)
        main_window.setStyleSheet("background-color: white;\n"
                                  "\n"
                                  "")
        self.gridLayout_2 = QtWidgets.QGridLayout(main_window)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.toolButton_info = QtWidgets.QToolButton(main_window)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.toolButton_info.sizePolicy().hasHeightForWidth())
        self.toolButton_info.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.toolButton_info.setFont(font)
        self.toolButton_info.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_info.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "color: black;\n"
                                           "border-color: black;\n"
                                           "border-width: 10px;\n"
                                           "border-radius: 20px;\n"
                                           "border-style: solid;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/project/report.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_info.setIcon(icon)
        self.toolButton_info.setIconSize(QtCore.QSize(120, 100))
        self.toolButton_info.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_info.setObjectName("toolButton_info")
        self.gridLayout.addWidget(self.toolButton_info, 0, 1, 1, 1)
        self.toolButton_register_fuck = QtWidgets.QToolButton(
            main_window, clicked=lambda: self.press_fuck())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.toolButton_register_fuck.sizePolicy().hasHeightForWidth())
        self.toolButton_register_fuck.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.toolButton_register_fuck.setFont(font)
        self.toolButton_register_fuck.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_register_fuck.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                    "color: black;\n"
                                                    "border-color: black;\n"
                                                    "border-width: 10px;\n"
                                                    "border-radius: 20px;\n"
                                                    "border-style: solid;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/project/factor.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_register_fuck.setIcon(icon1)
        self.toolButton_register_fuck.setIconSize(QtCore.QSize(95, 100))
        self.toolButton_register_fuck.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_register_fuck.setObjectName("toolButton_register_fuck")
        self.gridLayout.addWidget(self.toolButton_register_fuck, 0, 2, 1, 1)
        self.toolButton_stock = QtWidgets.QToolButton(main_window)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.toolButton_stock.sizePolicy().hasHeightForWidth())
        self.toolButton_stock.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.toolButton_stock.setFont(font)
        self.toolButton_stock.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_stock.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "color: black;\n"
                                            "border-color: black;\n"
                                            "border-width: 10px;\n"
                                            "border-radius: 20px;\n"
                                            "border-style: solid;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/project/inventory.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_stock.setIcon(icon2)
        self.toolButton_stock.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_stock.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_stock.setObjectName("toolButton_stock")
        self.gridLayout.addWidget(self.toolButton_stock, 1, 0, 1, 1)
        self.toolButton_resource = QtWidgets.QToolButton(
            main_window, clicked=lambda: self.press_resource())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.toolButton_resource.sizePolicy().hasHeightForWidth())
        self.toolButton_resource.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.toolButton_resource.setFont(font)
        self.toolButton_resource.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_resource.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                               "color: black;\n"
                                               "border-color: black;\n"
                                               "border-width: 10px;\n"
                                               "border-radius: 20px;\n"
                                               "border-style: solid;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/project/recourse.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_resource.setIcon(icon3)
        self.toolButton_resource.setIconSize(QtCore.QSize(140, 130))
        self.toolButton_resource.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_resource.setObjectName("toolButton_recourse")
        self.gridLayout.addWidget(self.toolButton_resource, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.toolButton_ask_storage = QtWidgets.QToolButton(main_window)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.toolButton_ask_storage.sizePolicy().hasHeightForWidth())
        self.toolButton_ask_storage.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setKerning(True)
        self.toolButton_ask_storage.setFont(font)
        self.toolButton_ask_storage.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_ask_storage.setContextMenuPolicy(
            QtCore.Qt.DefaultContextMenu)
        self.toolButton_ask_storage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_ask_storage.setAutoFillBackground(False)
        self.toolButton_ask_storage.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                  "color: black;\n"
                                                  "border-color: black;\n"
                                                  "border-width: 10px;\n"
                                                  "border-radius: 20px;\n"
                                                  "border-style: solid;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(
            ":/project/icons8-storage-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_ask_storage.setIcon(icon4)
        self.toolButton_ask_storage.setIconSize(QtCore.QSize(80, 160))
        self.toolButton_ask_storage.setCheckable(False)
        self.toolButton_ask_storage.setPopupMode(
            QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_ask_storage.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_ask_storage.setAutoRaise(False)
        self.toolButton_ask_storage.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_ask_storage.setObjectName("toolButton_ask_storage")
        self.gridLayout.addWidget(self.toolButton_ask_storage, 1, 2, 1, 1)
        self.toolButton_projects = QtWidgets.QToolButton(
            main_window, clicked=lambda: self.press_projects())
        self.toolButton_projects.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.toolButton_projects.sizePolicy().hasHeightForWidth())
        self.toolButton_projects.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.toolButton_projects.setFont(font)
        self.toolButton_projects.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_projects.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_projects.setAutoFillBackground(False)
        self.toolButton_projects.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                               "color: black;\n"
                                               "border-color: black;\n"
                                               "border-width: 10px;\n"
                                               "border-radius: 20px;\n"
                                               "border-style: solid;")
        self.toolButton_projects.setInputMethodHints(QtCore.Qt.ImhNone)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/project/project.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_projects.setIcon(icon5)
        self.toolButton_projects.setIconSize(QtCore.QSize(120, 120))
        self.toolButton_projects.setCheckable(False)
        self.toolButton_projects.setAutoRepeat(False)
        self.toolButton_projects.setAutoExclusive(False)
        self.toolButton_projects.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_projects.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_projects.setObjectName("toolButton_projects")
        self.gridLayout.addWidget(self.toolButton_projects, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def press_fuck(self):
        from factor_register import Ui_register_factor, register_factor
        ui = Ui_register_factor()
        ui.setupUi(register_factor)
        register_factor.show()

    def press_resource(self):
        from resource import Ui_MainWindow, MainWindow
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def press_projects(self):
        from projects import Ui_MainWindow, MainWindow        
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()


    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "main_window"))
        self.toolButton_info.setText(_translate("main_window", "  گزارش"))
        self.toolButton_register_fuck.setText(
            _translate("main_window", " ثبت فاکتور"))
        self.toolButton_stock.setText(
            _translate("main_window", " موجودی انبار"))
        self.toolButton_resource.setText(_translate("main_window", " منابع"))
        self.toolButton_ask_storage.setText(
            _translate("main_window", " درخواست انبار"))
        self.toolButton_projects.setText(
            _translate("main_window", " پروژه ها"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QWidget()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
