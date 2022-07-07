# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(514, 398)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 50, 291, 61))
        self.label.setStyleSheet("font: 75 21pt \"Ubuntu Mono\";")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(220, 220, 80, 25))
        self.pushButton.setObjectName("pushButton")
        self.BtnSalir = QtWidgets.QPushButton(Dialog)
        self.BtnSalir.setGeometry(QtCore.QRect(400, 350, 80, 25))
        self.BtnSalir.setObjectName("BtnSalir")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ventan Proyecto1"))
        self.pushButton.setText(_translate("Dialog", "Saludar"))
        self.BtnSalir.setText(_translate("Dialog", "Salir"))
