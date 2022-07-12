
from Persona import *

class Estudiante(Persona):
    def __init__(self,nombre,edad,matricula):
        super().__init__(nombre,edad)
        self.matricula=matricula
    def __str__(self):
        return super().__str__()+"\n matricula: "+self.matricula+"    nombre:"+self._nombre

