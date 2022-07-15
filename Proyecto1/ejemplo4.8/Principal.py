import sys
from Ventana import *
class Principal(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.generar)
    def generar(self):
        for i in range(1,100,1):
            if i%2!=0:
                self.listWidget.addItem(str(i))

if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    dialogo=Principal()
    dialogo.show()
    sys.exit(app.exec_())