# Form implementation generated from reading ui file 'd:\Third Semester files\database\project POSHAAK final\POSHAAK-database\admin_interface2.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(613, 475)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 80, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 140, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 170, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 200, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 230, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 260, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.name = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.name.setGeometry(QtCore.QRect(170, 80, 281, 20))
        self.name.setObjectName("name")
        self.category = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.category.setGeometry(QtCore.QRect(180, 110, 271, 20))
        self.category.setObjectName("category")
        self.b = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.b.setGeometry(QtCore.QRect(190, 200, 251, 20))
        self.b.setObjectName("b")
        self.quantity = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.quantity.setGeometry(QtCore.QRect(190, 230, 241, 20))
        self.quantity.setObjectName("quantity")
        self.price = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.price.setGeometry(QtCore.QRect(200, 260, 231, 20))
        self.price.setObjectName("price")
        self.add_but = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_but.setGeometry(QtCore.QRect(140, 370, 111, 41))
        self.add_but.setObjectName("add_but")
        self.color = QtWidgets.QComboBox(parent=self.centralwidget)
        self.color.setGeometry(QtCore.QRect(190, 170, 261, 22))
        self.color.setObjectName("color")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.size = QtWidgets.QComboBox(parent=self.centralwidget)
        self.size.setGeometry(QtCore.QRect(180, 140, 261, 22))
        self.size.setObjectName("size")
        self.size.addItem("")
        self.size.addItem("")
        self.size.addItem("")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 50, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.product_id = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.product_id.setGeometry(QtCore.QRect(180, 50, 271, 20))
        self.product_id.setObjectName("product_id")
        self.discription = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.discription.setGeometry(QtCore.QRect(210, 320, 251, 41))
        self.discription.setObjectName("discription")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 320, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(60, 283, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.discount = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.discount.setGeometry(QtCore.QRect(200, 290, 251, 20))
        self.discount.setObjectName("discount")
        self.close = QtWidgets.QPushButton(parent=self.centralwidget)
        self.close.setGeometry(QtCore.QRect(370, 370, 101, 31))
        self.close.setObjectName("close")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 613, 26))
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
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_2.setText(_translate("MainWindow", "Category"))
        self.label_3.setText(_translate("MainWindow", "Size"))
        self.label_4.setText(_translate("MainWindow", "Color"))
        self.label_5.setText(_translate("MainWindow", "Brand"))
        self.label_6.setText(_translate("MainWindow", "Quantity"))
        self.label_7.setText(_translate("MainWindow", "Price"))
        self.add_but.setText(_translate("MainWindow", "ADD Item"))
        self.color.setItemText(0, _translate("MainWindow", "Blue"))
        self.color.setItemText(1, _translate("MainWindow", "Red"))
        self.color.setItemText(2, _translate("MainWindow", "Black"))
        self.color.setItemText(3, _translate("MainWindow", "Green"))
        self.color.setItemText(4, _translate("MainWindow", "Purple"))
        self.size.setItemText(0, _translate("MainWindow", "L"))
        self.size.setItemText(1, _translate("MainWindow", "M"))
        self.size.setItemText(2, _translate("MainWindow", "S"))
        self.label_8.setText(_translate("MainWindow", "Pro_id"))
        self.label_9.setText(_translate("MainWindow", "Discription"))
        self.label_10.setText(_translate("MainWindow", "Discount"))
        self.close.setText(_translate("MainWindow", "Close"))
