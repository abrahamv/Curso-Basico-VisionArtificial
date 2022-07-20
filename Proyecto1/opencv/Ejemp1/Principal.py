import sys
import cv2
import imutils
from  PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtWidgets import QFileDialog

from Ventana import *

class Principal(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.cargarImagen)
        self.pushButton_2.clicked.connect(self.cambiarBGR)
        self.pushButton_3.clicked.connect(self.guardar)


    def cambiarBGR(self):
        self.image=cv2.cvtColor(self.image,cv2.COLOR_RGB2BGR)
        self.mostrarImagen()

    def guardar(self):
        nombreArchivo=QFileDialog.getSaveFileName(filter=("jpg(*.jpg);png"))[0]
        cv2.imwrite(nombreArchivo,self.image)
        print("se guardo la imagen")
    def cargarImagen(self):
        direccionImagen=QFileDialog.getOpenFileName(filter="Imagen (*.*)")[0]
        self.image=cv2.imread(direccionImagen)
        self.mostrarImagen()

    def mostrarImagen(self):
        frame=imutils.resize(self.image,width=640)
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        image=QImage(frame,frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(image))

if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    dialogo=Principal()
    dialogo.show()
    sys.exit(app.exec_())