from tkinter import dialog
import sys
from Ventana import *

class Principal(QtWidgets.QDialog,Ui_Dialog):
        def __init__(self):
            QtWidgets.QDialog.__init__(self)
            self.setupUi(self)
            
            self.pushButton.clicked.connect(self.verificar)
        
        def verificar(self):
            N=int(self.lineEdit.text())
            self.matriz=[[0 for i in range(N)] for j in range(N)]
            self.tableWidget.setColumnCount(N)
            self.tableWidget.setRowCount(N)
            for i in range(N):
                for j in range(N):
                    numero,estado=QtWidgets.QInputDialog.getInt(self,"Ingrese Items","Item")
                    if estado:
                        self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(numero)))
                        self.matriz[i][j]=numero
            bandera=0
            for i in range(N):
                for j in range(N):
                    if (i==j and self.matriz[i][j]==1) or (self.matriz[i][j]==0 and i!=j):
                        bandera=0
                    else:
                        bandera=1    
                        break
                   # if self.matriz[i][j]!=0 and i!=j:
                    #    bandera=1
                     #   break
                if bandera==1:
                    break
            if bandera==0:
                self.label_2.setText("Es Diagonal")
            else:
                self.label_2.setText("No es Diagonal")
                 
if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    dialogo=Principal()
    dialogo.show()
    sys.exit(app.exec_())