"""
Batallas de dados. Cada jugador tiene dos tiradas
"""
import random
#funcion tirada de dado
def tirada():
    puntos = random.randint(1,6)
    return puntos

#función mostrar puntos
def mostrar_puntos(puntos:int):
    print(f"Total de {puntos} puntos.")

#jugador 1 tira el dado dos veces
valor= [tirada(), tirada()]
print("Jugador 1")
mostrar_puntos(sum(valor))
#jugador 2 tira el dado dos veces
valor2= [tirada(), tirada()]
print("Jugador 2")
mostrar_puntos(sum(valor2))

if sum(valor)==sum(valor2):
    print("Empate.")
elif sum(valor) > sum(valor2):
    print("Ganador Jugador 1")
else:
    print("Ganador Jugador 2")
