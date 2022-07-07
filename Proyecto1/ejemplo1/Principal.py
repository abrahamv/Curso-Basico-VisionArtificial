
from Guess import Guess

if __name__=="__main__":
    juego1=Guess()
    print(juego1.vidas)
    juego1.ponerNumero(40)
    juego1.Jugar()

    juego2=Guess("Juego2")
    juego2.ponerNumero(30)
    juego2.Jugar()

    juego3=Guess("Juego3")
    juego3.ponerNumero(20)
    juego3.Jugar()
