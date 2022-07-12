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
        Dialog.resize(608, 400)
        self.BtnSalir = QtWidgets.QPushButton(Dialog)
        self.BtnSalir.setGeometry(QtCore.QRect(480, 340, 89, 25))
        self.BtnSalir.setObjectName("BtnSalir")
        self.BtnCalcular = QtWidgets.QPushButton(Dialog)
        self.BtnCalcular.setGeometry(QtCore.QRect(310, 130, 89, 25))
        self.BtnCalcular.setObjectName("BtnCalcular")
        self.ledit = QtWidgets.QLineEdit(Dialog)
        self.ledit.setGeometry(QtCore.QRect(310, 50, 81, 25))
        self.ledit.setObjectName("ledit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 50, 121, 17))
        self.label.setObjectName("label")
        self.lblResultado = QtWidgets.QLabel(Dialog)
        self.lblResultado.setGeometry(QtCore.QRect(310, 180, 191, 61))
        self.lblResultado.setText("")
        self.lblResultado.setObjectName("lblResultado")
        self.BtnLimpiar = QtWidgets.QPushButton(Dialog)
        self.BtnLimpiar.setGeometry(QtCore.QRect(130, 330, 89, 25))
        self.BtnLimpiar.setObjectName("BtnLimpiar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Area de una circunferencia"))
        self.BtnSalir.setText(_translate("Dialog", "salir"))
        self.BtnCalcular.setText(_translate("Dialog", "Calcular"))
        self.label.setText(_translate("Dialog", "Ingrese el Radio"))
        self.BtnLimpiar.setText(_translate("Dialog", "limpiar"))
