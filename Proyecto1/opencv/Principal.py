

import cv2 


class Principal():
    def __init__(self):
        imagen=cv2.imread("most.jpg",0)
        cv2.imshow('Amigo',imagen)
        cv2.imwrite("AMigo.png",imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    app=Principal()