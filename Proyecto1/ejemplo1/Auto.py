


class Auto:
    # atributos
    marca=""
    modelo=""
    color=""
    # metodos/comportamiento
    def acelerar(self):
        print("el auto esta  Acelerando")
    def colocarMarca(self,marca):
        self.marca=marca
    def mostrarMarca(self):
        print("La marca del auto es: ",self.marca)


mitsubishi=Auto()
mitsubishi.acelerar()
mitsubishi.colocarMarca("mitsubishi")
mitsubishi.mostrarMarca()


toyota=Auto()
toyota.acelerar()
toyota.colocarMarca("toyota")
toyota.mostrarMarca()

volvo=Auto()
volvo.acelerar()
volvo.colocarMarca("volvo")
volvo.mostrarMarca()
