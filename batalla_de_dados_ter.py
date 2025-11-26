"""
Batallas de dados. Cada jugador tiene dos tiradas. 
Pedir los nombres de los jugadores.
Agregar el Menu: 
1. Jugar.
2. Instrucciones de Juego.
3. Salir.

"""
import random
#funcion imprime menu
def menu():
    print("----------MENÚ--------")
    print("ELIGE UNA OPCIÓN: ")
    print("1. Jugar.")
    print("2. Instrucciones de Juego.")
    print("3. Salir")
    #elige la opción por primera vez
    opcion= int(input(""))       
    return opcion

#funcion tirada de dado
def tirada():
    puntos = random.randint(1,6)
    return puntos

#función mostrar puntos
def mostrar_puntos(puntos:int):
    print(f"Total de {puntos} puntos.")

#función pedir los nombres de los jugadores
def nombres(lista:list):
    lista +=[input("Ingrese Nombre de Jugador: ")]
    return lista

#imprime el menu por primera vez
eleccion = menu()

while True:
    if eleccion ==1:
        name = []
        #jugador 1 ingresa su nombre
        name = nombres(name)
        #jugador 1 tira el dado dos veces
        valor= [tirada(), tirada()]
        print(f"Jugador {name[0]}")
        mostrar_puntos(sum(valor))

        #jugador 1 ingresa su nombre
        name = nombres(name)
        #jugador 2 tira el dado dos veces
        valor2= [tirada(), tirada()]
        print(f"Jugador {name[1]}")
        mostrar_puntos(sum(valor2))

        if sum(valor)==sum(valor2):
            print("Empate.")
        elif sum(valor) > sum(valor2):
            print(f"Ganador Jugador {name[0]}")
        else:
            print(f"Ganador Jugador {name[1]}")
        #imprime el menu 
        eleccion = menu()
    elif eleccion ==2:
        print("INSTRUCCIONES DEL JUEGO.")
        print("Cada jugador tira dos veces el dado.")
        print("El que sume más puntos gana.")
        #imprime el menu
        eleccion = menu()
    elif eleccion == 3:
        print("GRACIAS POR JUGAR.")
        break
    else: 
        print("OPCION INCORRECTA")
        eleccion = menu()
