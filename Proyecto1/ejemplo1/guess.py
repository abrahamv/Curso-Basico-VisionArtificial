
'''
Programacion topdown estructurado
juego Adivina el numero

     F(x)=x+1
     F(10)=11
'''

def mostrarGanador(mensaje):
    print(mensaje)
    

numeroAdivinar=90
vidas=3
while vidas!=0:
    numeroUsuario=int(input("Adivina el numero entre 1-100: "))
    if numeroAdivinar==numeroUsuario:
        mostrarGanador("Uds. Gano!!! ")
        break
    elif numeroUsuario<numeroAdivinar:
        print("El numero es mayor")
        vidas-=1  # vidas=vidas-1
    else:
        print("El numero es menor")
        vidas-=1

        
