from nodo_altura import nodo_altura
import sys
import os


class lista_altura:
    def __init__(self):
        self.primero = None
        self.contador_celdas = 0

    def insertar_dato(self, altura):
        # Si el primer nodo es nulo
        if self.primero is None:
            self.primero = nodo_altura(altura=altura)
            self.contador_celdas += 1
            return
        # Temporal para recorrer nuestra lista
        actual = self.primero
        # Ejecuta el ciclo, mientras actual.siguiente exista
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_altura(altura=altura)
        self.contador_celdas += 1

    def recorrer_e_imprimir_lista(self):
        print("============================================================")
        actual = self.primero
        while actual != None:
            print("Altura:", actual.altura.valor,
                  "Letra:", actual.altura.letra)
            actual = actual.siguiente
        print("============================================================")
