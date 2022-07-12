import sys
from Ventana import *

class Principal(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self,datos=None):
        #QtGui.QWidget.__init__(self,datos)
        QtWidgets.QDialog.__init__(self)
        #self.Ui_Dialog,__init__()
        #super().__init__()
        
        self.setupUi(self)
       
       # self.label.setText("hola")
        self.pushButton_2.clicked.connect(self.salir)
        self.pushButton.clicked.connect(self.saludar)
    def salir(self):
        sys.exit(0)
        #self.pushButton_2.clicked.connect(self.salir())
    def saludar(self):
        self.label.setText("Bienvenidos al curso de programacion \n  Python con Vision Artificial")
        
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog=Principal()
    Dialog.show()
    sys.exit(app.exec_())
