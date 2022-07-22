
import cv2

class Principal:

    def __init__(self,titulo=""):

        self.titulo=titulo


    def VerCamara(self,nCamara):

        cap=cv2.VideoCapture(nCamara)
        self.mostrarVideo(cap)

    def VerVideo(self,nombreVideo):
        cap=cv2.VideoCapture(nombreVideo)
        self.mostrarVideo(cap)

    def mostrarVideo(self,cap):
        while(True):
            ret,frame=cap.read()
            cv2.imshow('video',frame) 
            #cv2.waitKey(0)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                cap.release()
                break
        cv2.destroyAllWindows()


if __name__=="__main__":
    app=Principal()
    #app.VerCamara(0)
    app.VerVideo("Rio.mp4")
