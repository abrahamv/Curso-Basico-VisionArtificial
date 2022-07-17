from operator import itemgetter
import sys
from Ventana import *
class Principal(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.listaA=[]
        self.listaB=[]
        self.listaC=[]
        self.pushButton.clicked.connect(self.IngresarListas)
    def IngresarListas(self):
        cantidad=int(self.lineEdit.text())

        self.ingresarLista("Lista A",cantidad,self.listaA,self.listWidget)
        self.ingresarLista("Lista B",cantidad,self.listaB,self.listWidget_2)
               
        for i in range(cantidad):
            suma=self.listaA[i]+self.listaB[i]
            self.listaC.append(suma)
            self.listWidget_3.addItem(str(suma))  
    def  ingresarLista(self,titulo,cantidad,lista,listaW):  
        for i in range(cantidad):
            item,estado=QtWidgets.QInputDialog.getInt(self,titulo,"Numero entero")
            if estado:
                lista.append(item)
                listaW.addItem(str(item))
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    dialogo=Principal()
    dialogo.show()
    sys.exit(app.exec_())


