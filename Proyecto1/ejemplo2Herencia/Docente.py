from Persona import *
class Docente(Persona):
    def __init__(self,nombre,edad,idDocente):
        super().__init__(nombre,edad)
        self.idDocente=idDocente
    def __str__(self):
        return super().__str__()+"\n id Docente: "+self.idDocente
