# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(703, 329)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 70, 141, 192))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(Dialog)
        self.listWidget_2.setGeometry(QtCore.QRect(250, 70, 151, 192))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_3 = QtWidgets.QListWidget(Dialog)
        self.listWidget_3.setGeometry(QtCore.QRect(510, 70, 131, 192))
        self.listWidget_3.setObjectName("listWidget_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 150, 67, 61))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(430, 150, 67, 61))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 270, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(290, 270, 67, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(550, 270, 67, 17))
        self.label_6.setObjectName("label_6")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(40, 20, 601, 27))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">+</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">=</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "lista A"))
        self.label_5.setText(_translate("Dialog", "lista B"))
        self.label_6.setText(_translate("Dialog", "lista C"))
        self.label.setText(_translate("Dialog", "Ingrese N:"))
        self.pushButton.setText(_translate("Dialog", "Ingresar Items"))
