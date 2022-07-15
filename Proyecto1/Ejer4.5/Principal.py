import sys
from Ventana import *

class Principal(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.contadorNegativos=0
        self.contadorPositivos=0
        self.pushButton.clicked.connect(self.contador)
    def contador(self):
        cantidadNumeros=int(self.lineEdit.text())
        while cantidadNumeros!=0:
            numero,estado=QtWidgets.QInputDialog.getInt(self,"Numeros","Ingrese un numero: ")
            if estado:
                if numero>0:
                    self.contadorPositivos+=1
                    self.label_5.setText(str(self.contadorPositivos))
                    self.label_5.setAlignment(QtCore.Qt.AlignCenter)
                else:
                    self.contadorNegativos+=1
                    self.label_3.setText(str(self.contadorNegativos))
                    self.label_3.setAlignment(QtCore.Qt.AlignCenter)

            cantidadNumeros-=1  # cantidadNumeros=cantidadNumeros-1

if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    dialog=Principal()
    dialog.show()
    sys.exit(app.exec_())