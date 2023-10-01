from nodo_tiempo import nodo_tiempo
import sys
import os


class lista_tiempo:
    def __init__(self):
        self.primero = None
        self.contador_celdas = 0

    def insertar_dato(self, tiempo):
        # Si el primer nodo es nulo
        if self.primero is None:
            self.primero = nodo_tiempo(tiempo=tiempo)
            self.contador_celdas += 1
            return
        # Temporal para recorrer nuestra lista
        actual = self.primero
        # Ejecuta el ciclo, mientras actual.siguiente exista
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_tiempo(tiempo=tiempo)
        self.contador_celdas += 1

    def recorrer_e_imprimir_lista(self):
        print("============================================================")
        actual = self.primero
        while actual != None:
            print("Altura:", actual.tiempo.valor,
                  "Letra:", actual.tiempo.letra)
            actual = actual.siguiente
        print("============================================================")
