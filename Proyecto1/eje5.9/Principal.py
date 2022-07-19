
import sys
from Ventana import *

class Principal(QtWidgets.QDialog,Ui_Dialog):
        def __init__(self):
            QtWidgets.QDialog.__init__(self)
            self.setupUi(self)
            self.filas=15
            self.columnas=12
            self.matriz=[[0 for i in range(self.columnas)]for j in range(self.filas)]
            self.pushButton.clicked.connect(self.Calcular)

        def Calcular(self):
            self.llenarMatriz()
            self.label_4.setText(str(self.menor))
            suma=self.sumarFilas()
            self.label_5.setText(str(suma))
            cantidadNegativos=self.ContarNegativos()
            self.label_6.setText(str(cantidadNegativos))

        def ContarNegativos(self):
            negativos=0
            for i in range(self.filas):
                for j in range(5,10,1):
                    if self.matriz[i][j]<0:
                        negativos+=1

            return negativos
        def sumarFilas(self):
            suma=0
            for i in range(5):
                for j in range(self.columnas):
                    suma=suma+self.matriz[i][j]
            return suma
        def llenarMatriz(self):
            self.menor=0
            for i in range(self.filas):
                for j in range(self.columnas):
                    numero,estado=QtWidgets.QInputDialog.getInt(self,"item","item")
                    
                    if estado:
                        self.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(numero)))
                        self.matriz[i][j]=numero
                    if self.menor>numero:
                        self.menor=numero
                 
if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    dialogo=Principal()
    dialogo.show()
    sys.exit(app.exec_())