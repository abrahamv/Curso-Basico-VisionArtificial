




class Guess:
    #atributo
    
    #comportamiento
    def __init__(self,nombreJuego="Juego sin nombre"):
        self.__nombreJuego=nombreJuego
        self.__numeroAdivinar=0
        self.__vidas=3
        
    def ponerNumero(self,numero):
        self.numeroAdivinar=numero
    def Jugar(self):
         print(self.__nombreJuego)
         while self.__vidas!=0:
             numeroUsuario=int(input("Adivina el numero entre 1-100: "))
             if self.__numeroAdivinar==numeroUsuario:
                 print("Uds. Gano!!! ")
                 break
             elif numeroUsuario<self.__numeroAdivinar:
                 print("El numero es mayor")
                 self.__vidas-=1  # vidas=vidas-1
             else:
                 print("El numero es menor")
                 self.__vidas-=1


