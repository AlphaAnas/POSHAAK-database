# Form implementation generated from reading ui file 'd:\Third Semester files\database\project POSHAAK final\POSHAAK-database\AdminView.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1710, 927)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OrdersGroupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.OrdersGroupBox.setGeometry(QtCore.QRect(10, 0, 1681, 271))
        self.OrdersGroupBox.setObjectName("OrdersGroupBox")
        self.OrdersDateEdit = QtWidgets.QDateEdit(parent=self.OrdersGroupBox)
        self.OrdersDateEdit.setGeometry(QtCore.QRect(1459, 220, 131, 22))
        self.OrdersDateEdit.setObjectName("OrdersDateEdit")
        self.OrderDateLabel = QtWidgets.QLabel(parent=self.OrdersGroupBox)
        self.OrderDateLabel.setGeometry(QtCore.QRect(1360, 220, 91, 21))
        self.OrderDateLabel.setObjectName("OrderDateLabel")
        self.OrdersTableWidget = QtWidgets.QTableWidget(parent=self.OrdersGroupBox)
        self.OrdersTableWidget.setGeometry(QtCore.QRect(10, 20, 1581, 191))
        self.OrdersTableWidget.setObjectName("OrdersTableWidget")
        self.OrdersTableWidget.setColumnCount(10)
        self.OrdersTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.OrdersTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.OrdersTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.OrdersTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.OrdersTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.OrdersTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.OrdersTableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.OrdersTableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.OrdersTableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.OrdersTableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.OrdersTableWidget.setHorizontalHeaderItem(9, item)
        self.OrdersDeleteButton = QtWidgets.QPushButton(parent=self.OrdersGroupBox)
        self.OrdersDeleteButton.setGeometry(QtCore.QRect(20, 230, 101, 31))
        self.OrdersDeleteButton.setObjectName("OrdersDeleteButton")
        self.CustomersGroupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.CustomersGroupBox.setGeometry(QtCore.QRect(10, 560, 911, 261))
        self.CustomersGroupBox.setObjectName("CustomersGroupBox")
        self.CustomersTableWidget = QtWidgets.QTableWidget(parent=self.CustomersGroupBox)
        self.CustomersTableWidget.setGeometry(QtCore.QRect(20, 20, 881, 181))
        self.CustomersTableWidget.setObjectName("CustomersTableWidget")
        self.CustomersTableWidget.setColumnCount(5)
        self.CustomersTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.CustomersTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.CustomersTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.CustomersTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.CustomersTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.CustomersTableWidget.setHorizontalHeaderItem(4, item)
        self.CustomerIDLineEdit = QtWidgets.QLineEdit(parent=self.CustomersGroupBox)
        self.CustomerIDLineEdit.setGeometry(QtCore.QRect(740, 210, 151, 20))
        self.CustomerIDLineEdit.setObjectName("CustomerIDLineEdit")
        self.CustomerIDLabel = QtWidgets.QLabel(parent=self.CustomersGroupBox)
        self.CustomerIDLabel.setGeometry(QtCore.QRect(630, 210, 101, 21))
        self.CustomerIDLabel.setObjectName("CustomerIDLabel")
        self.CustomersDeleteButton = QtWidgets.QPushButton(parent=self.CustomersGroupBox)
        self.CustomersDeleteButton.setGeometry(QtCore.QRect(20, 216, 101, 31))
        self.CustomersDeleteButton.setObjectName("CustomersDeleteButton")
        self.ShippersGroupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.ShippersGroupBox.setGeometry(QtCore.QRect(10, 290, 911, 261))
        self.ShippersGroupBox.setObjectName("ShippersGroupBox")
        self.ShippersTableWidget = QtWidgets.QTableWidget(parent=self.ShippersGroupBox)
        self.ShippersTableWidget.setGeometry(QtCore.QRect(10, 20, 681, 192))
        self.ShippersTableWidget.setObjectName("ShippersTableWidget")
        self.ShippersTableWidget.setColumnCount(4)
        self.ShippersTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ShippersTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ShippersTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ShippersTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ShippersTableWidget.setHorizontalHeaderItem(3, item)
        self.ShipperIDLineEdit = QtWidgets.QLineEdit(parent=self.ShippersGroupBox)
        self.ShipperIDLineEdit.setGeometry(QtCore.QRect(550, 220, 141, 20))
        self.ShipperIDLineEdit.setObjectName("ShipperIDLineEdit")
        self.ShipperIDLabel = QtWidgets.QLabel(parent=self.ShippersGroupBox)
        self.ShipperIDLabel.setGeometry(QtCore.QRect(470, 220, 71, 21))
        self.ShipperIDLabel.setObjectName("ShipperIDLabel")
        self.ShippersDeleteButton = QtWidgets.QPushButton(parent=self.ShippersGroupBox)
        self.ShippersDeleteButton.setGeometry(QtCore.QRect(700, 20, 81, 31))
        self.ShippersDeleteButton.setObjectName("ShippersDeleteButton")
        self.ShipperInsertButton = QtWidgets.QPushButton(parent=self.ShippersGroupBox)
        self.ShipperInsertButton.setGeometry(QtCore.QRect(700, 70, 81, 31))
        self.ShipperInsertButton.setObjectName("ShipperInsertButton")
        self.DeliveryGroupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.DeliveryGroupBox.setGeometry(QtCore.QRect(930, 560, 761, 261))
        self.DeliveryGroupBox.setObjectName("DeliveryGroupBox")
        self.DeliveryTableWidget = QtWidgets.QTableWidget(parent=self.DeliveryGroupBox)
        self.DeliveryTableWidget.setGeometry(QtCore.QRect(10, 20, 741, 181))
        self.DeliveryTableWidget.setObjectName("DeliveryTableWidget")
        self.DeliveryTableWidget.setColumnCount(6)
        self.DeliveryTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.DeliveryTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.DeliveryTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.DeliveryTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.DeliveryTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.DeliveryTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.DeliveryTableWidget.setHorizontalHeaderItem(5, item)
        self.CityLineEdit = QtWidgets.QLineEdit(parent=self.DeliveryGroupBox)
        self.CityLineEdit.setGeometry(QtCore.QRect(640, 210, 113, 20))
        self.CityLineEdit.setObjectName("CityLineEdit")
        self.CityLabel = QtWidgets.QLabel(parent=self.DeliveryGroupBox)
        self.CityLabel.setGeometry(QtCore.QRect(600, 210, 31, 20))
        self.CityLabel.setObjectName("CityLabel")
        self.DeliveryDeleteButton = QtWidgets.QPushButton(parent=self.DeliveryGroupBox)
        self.DeliveryDeleteButton.setGeometry(QtCore.QRect(10, 220, 91, 31))
        self.DeliveryDeleteButton.setObjectName("DeliveryDeleteButton")
        self.DeliveryInsertButton = QtWidgets.QPushButton(parent=self.DeliveryGroupBox)
        self.DeliveryInsertButton.setGeometry(QtCore.QRect(110, 220, 91, 31))
        self.DeliveryInsertButton.setObjectName("DeliveryInsertButton")
        self.ClearButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ClearButton.setGeometry(QtCore.QRect(1340, 830, 171, 41))
        self.ClearButton.setObjectName("ClearButton")
        self.ShowButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ShowButton.setGeometry(QtCore.QRect(1520, 830, 171, 41))
        self.ShowButton.setObjectName("ShowButton")
        self.ViewProductsButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ViewProductsButton.setGeometry(QtCore.QRect(190, 830, 171, 41))
        self.ViewProductsButton.setObjectName("ViewProductsButton")
        self.BackButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(10, 830, 171, 41))
        self.BackButton.setObjectName("BackButton")
        self.CategoriesGroupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.CategoriesGroupBox.setGeometry(QtCore.QRect(930, 290, 761, 261))
        self.CategoriesGroupBox.setObjectName("CategoriesGroupBox")
        self.CategoriesTableWidget = QtWidgets.QTableWidget(parent=self.CategoriesGroupBox)
        self.CategoriesTableWidget.setGeometry(QtCore.QRect(20, 20, 521, 181))
        self.CategoriesTableWidget.setObjectName("CategoriesTableWidget")
        self.CategoriesTableWidget.setColumnCount(3)
        self.CategoriesTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.CategoriesTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.CategoriesTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.CategoriesTableWidget.setHorizontalHeaderItem(2, item)
        self.CategoryComboBox = QtWidgets.QComboBox(parent=self.CategoriesGroupBox)
        self.CategoryComboBox.setGeometry(QtCore.QRect(400, 210, 141, 22))
        self.CategoryComboBox.setObjectName("CategoryComboBox")
        self.CategoryComboBox.addItem("")
        self.CategoryComboBox.addItem("")
        self.CategoryComboBox.addItem("")
        self.CategoryComboBox.addItem("")
        self.CategoryLabel = QtWidgets.QLabel(parent=self.CategoriesGroupBox)
        self.CategoryLabel.setGeometry(QtCore.QRect(270, 210, 121, 20))
        self.CategoryLabel.setObjectName("CategoryLabel")
        self.CategoryDeleteButton = QtWidgets.QPushButton(parent=self.CategoriesGroupBox)
        self.CategoryDeleteButton.setGeometry(QtCore.QRect(560, 20, 91, 31))
        self.CategoryDeleteButton.setObjectName("CategoryDeleteButton")
        self.CategoryInsertButton = QtWidgets.QPushButton(parent=self.CategoriesGroupBox)
        self.CategoryInsertButton.setGeometry(QtCore.QRect(560, 70, 91, 31))
        self.CategoryInsertButton.setObjectName("CategoryInsertButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OrdersGroupBox.setTitle(_translate("MainWindow", "Orders"))
        self.OrderDateLabel.setText(_translate("MainWindow", "Order Date"))
        item = self.OrdersTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "order_id"))
        item = self.OrdersTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "cart_id"))
        item = self.OrdersTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "customer_id"))
        item = self.OrdersTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "order_date"))
        item = self.OrdersTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "total_amount"))
        item = self.OrdersTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "payment_method"))
        item = self.OrdersTableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "status"))
        item = self.OrdersTableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "shipCity"))
        item = self.OrdersTableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "shipDate"))
        item = self.OrdersTableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "shipperID"))
        self.OrdersDeleteButton.setText(_translate("MainWindow", "Delete"))
        self.CustomersGroupBox.setTitle(_translate("MainWindow", "Customers"))
        item = self.CustomersTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.CustomersTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "last_name"))
        item = self.CustomersTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "email"))
        item = self.CustomersTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "password"))
        item = self.CustomersTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "account_type"))
        self.CustomerIDLabel.setText(_translate("MainWindow", "CustomerID"))
        self.CustomersDeleteButton.setText(_translate("MainWindow", "Delete"))
        self.ShippersGroupBox.setTitle(_translate("MainWindow", "Shippers"))
        item = self.ShippersTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.ShippersTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "name"))
        item = self.ShippersTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "contact_number"))
        item = self.ShippersTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "email"))
        self.ShipperIDLabel.setText(_translate("MainWindow", "ShipperID"))
        self.ShippersDeleteButton.setText(_translate("MainWindow", "Delete"))
        self.ShipperInsertButton.setText(_translate("MainWindow", "Insert"))
        self.DeliveryGroupBox.setTitle(_translate("MainWindow", "Delivery Areas"))
        item = self.DeliveryTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "city"))
        item = self.DeliveryTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "area"))
        item = self.DeliveryTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "country"))
        item = self.DeliveryTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "postal_code"))
        item = self.DeliveryTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "charges"))
        item = self.DeliveryTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "isPossible"))
        self.CityLabel.setText(_translate("MainWindow", "City"))
        self.DeliveryDeleteButton.setText(_translate("MainWindow", "Delete"))
        self.DeliveryInsertButton.setText(_translate("MainWindow", "Insert"))
        self.ClearButton.setText(_translate("MainWindow", "Clear"))
        self.ShowButton.setText(_translate("MainWindow", "Show"))
        self.ViewProductsButton.setText(_translate("MainWindow", "View Products"))
        self.BackButton.setText(_translate("MainWindow", "Back"))
        self.CategoriesGroupBox.setTitle(_translate("MainWindow", "Categories"))
        item = self.CategoriesTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.CategoriesTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "name"))
        item = self.CategoriesTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "description"))
        self.CategoryComboBox.setItemText(0, _translate("MainWindow", "All"))
        self.CategoryComboBox.setItemText(1, _translate("MainWindow", "1"))
        self.CategoryComboBox.setItemText(2, _translate("MainWindow", "2"))
        self.CategoryComboBox.setItemText(3, _translate("MainWindow", "3"))
        self.CategoryLabel.setText(_translate("MainWindow", "Category Type"))
        self.CategoryDeleteButton.setText(_translate("MainWindow", "Delete"))
        self.CategoryInsertButton.setText(_translate("MainWindow", "Insert"))
