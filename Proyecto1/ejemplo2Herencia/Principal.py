
#from Persona import *
from Estudiante import *
from Docente import *

if __name__=="__main__":
    print("Objetos Persona")
    juan=Persona("Juan",23)
    #print(juan.__nombre)
    print(juan)
    roberto=Persona()
    print(roberto)

    print("Objeto Estudiante")
    estudianteJuan=Estudiante("Juan",23,"123ABC")
    print(estudianteJuan)

    print("Objeto Docente")
    abraham=Docente("abraham",40,"ID123")
    print(abraham)
