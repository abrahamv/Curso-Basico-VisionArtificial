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
        Dialog.resize(838, 714)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(370, 450, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(40, 30, 781, 401))
        self.tableWidget.setRowCount(15)
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setObjectName("tableWidget")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(250, 510, 361, 110))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_6)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Calcular"))
        self.label.setText(_translate("Dialog", "Menor Elemento:"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">0</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "suma de las 5 primeras filas:"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">0</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "Numero de Negativos"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">0</span></p></body></html>"))
