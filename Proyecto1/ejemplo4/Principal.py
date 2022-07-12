
import sys
from Ventana import *

class Principal(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.BtnSalir.clicked.connect(self.Salir)
        self.BtnCalcular.clicked.connect(self.Calcular)
        self.BtnLimpiar.clicked.connect(self.Limpiar)
    def Limpiar(self):
        self.lblResultado.clear()
        self.ledit.clear()
    def Calcular(self):
        radio=float(self.ledit.text())
        pi=3.1416
        area=pi*radio*radio
        print("El area es : ",area)
        self.lblResultado.setText("El area es "+str(area))
    def Salir(self):
        sys.exit(0)

app=QtWidgets.QApplication(sys.argv)
dialogo=Principal()
dialogo.show()
sys.exit(app.exec_())
