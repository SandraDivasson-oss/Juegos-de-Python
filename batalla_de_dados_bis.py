"""
Batallas de dados. Cada jugador tiene dos tiradas. 
Pedir los nombres de los jugadores.
"""
import random
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
