

class Persona:
    #atributos
    def __init__(self,nombre="Sin nombre",edad=0):
        self._nombre=nombre
        self.__edad=edad
    #comportamiento
    def __str__(self):
        return "Nombre: "+self._nombre+"\nedad:"+str(self.__edad)
    

