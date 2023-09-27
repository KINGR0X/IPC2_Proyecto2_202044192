from nodo_dron import nodo_dron
import sys
import os


class lista_drones:
    def __init__(self):
        self.primero = None
        self.contador_celdas = 0

    def insertar_dato(self, dron):
        # Si el primer nodo es nulo
        if self.primero is None:
            self.primero = nodo_dron(dron=dron)
            self.contador_celdas += 1
            return
        # Temporal para recorrer nuestra lista
        actual = self.primero
        # Ejecuta el ciclo, mientras actual.siguiente exista
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_dron(dron=dron)
        self.contador_celdas += 1

    def recorrer_e_imprimir_lista(self):
        print()
        print("======================= Lista drones =======================")
        actual = self.primero
        while actual != None:
            print("Dron:", actual.dron.nombre)
            actual = actual.siguiente
        print("============================================================")
