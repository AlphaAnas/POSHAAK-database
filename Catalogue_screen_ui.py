# Form implementation generated from reading ui file 'd:\Third Semester files\database\project POSHAAK final\POSHAAK-database\Catalogue_screen.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(90, 10, 571, 541))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 60, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(360, 60, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(360, 100, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Category_box = QtWidgets.QComboBox(parent=self.groupBox)
        self.Category_box.setGeometry(QtCore.QRect(130, 60, 151, 22))
        self.Category_box.setObjectName("Category_box")
        self.Itemname = QtWidgets.QComboBox(parent=self.groupBox)
        self.Itemname.setGeometry(QtCore.QRect(130, 100, 151, 22))
        self.Itemname.setObjectName("Itemname")
        self.size_box = QtWidgets.QComboBox(parent=self.groupBox)
        self.size_box.setGeometry(QtCore.QRect(410, 60, 69, 22))
        self.size_box.setObjectName("size_box")
        self.color_box = QtWidgets.QComboBox(parent=self.groupBox)
        self.color_box.setGeometry(QtCore.QRect(410, 100, 69, 22))
        self.color_box.setObjectName("color_box")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(30, 190, 511, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.search_but = QtWidgets.QPushButton(parent=self.groupBox)
        self.search_but.setGeometry(QtCore.QRect(380, 140, 91, 23))
        self.search_but.setObjectName("search_but")
        self.close_but = QtWidgets.QPushButton(parent=self.groupBox)
        self.close_but.setGeometry(QtCore.QRect(430, 440, 75, 23))
        self.close_but.setObjectName("close_but")
        self.cart_but = QtWidgets.QPushButton(parent=self.groupBox)
        self.cart_but.setGeometry(QtCore.QRect(40, 450, 121, 31))
        self.cart_but.setObjectName("cart_but")
        self.refresh_but = QtWidgets.QPushButton(parent=self.groupBox)
        self.refresh_but.setGeometry(QtCore.QRect(310, 440, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.refresh_but.setFont(font)
        self.refresh_but.setObjectName("refresh_but")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Product_catalogue"))
        self.label.setText(_translate("MainWindow", "Category"))
        self.label_2.setText(_translate("MainWindow", "Dress_Name"))
        self.label_3.setText(_translate("MainWindow", "size"))
        self.label_4.setText(_translate("MainWindow", "Color"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product_id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Item Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Color"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Size"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "brand"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Discount"))
        self.search_but.setText(_translate("MainWindow", "Search"))
        self.close_but.setText(_translate("MainWindow", "Close"))
        self.cart_but.setText(_translate("MainWindow", "Add To Cart"))
        self.refresh_but.setText(_translate("MainWindow", "Refresh"))
