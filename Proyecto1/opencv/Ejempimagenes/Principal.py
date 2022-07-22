import sys
import cv2
import imutils
from  PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QTimer

from Ventana import *

class Principal(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.timer=QTimer()
        self.timer.timeout.connect(self.mostrarVideo)
        self.pushButton.clicked.connect(self.cargarVideo)

    def cargarVideo(self):
        direccionVideo=QFileDialog.getOpenFileName(filter="Video (*.*)")[0]
        
        if not self.timer.isActive():
            self.video=cv2.VideoCapture(direccionVideo)
            self.timer.start(20)
        else:
            self.video.release()

    def mostrarVideo(self):
    
        ret,frame=self.video.read()
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        h,w,ch=frame.shape
        tamanio=ch*w
        image=QImage(frame.data,w,h,tamanio,QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(image))

        


if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    dialogo=Principal()
    dialogo.show()
    sys.exit(app.exec_())