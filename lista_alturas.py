from nodo_alturas import nodo_alturas
import sys
import os


class lista_celdas:
    def __init__(self):
        self.primero = None
        self.contador_celdas = 0

    def insertar_dato(self, celda):
        # Si el primer nodo es nulo
        if self.primero is None:
            self.primero = nodo_alturas(celda=celda)
            self.contador_celdas += 1
            return
        # Temporal para recorrer nuestra lista
        actual = self.primero
        # Ejecuta el ciclo, mientras actual.siguiente exista
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_alturas(celda=celda)
        self.contador_celdas += 1

    def recorrer_e_imprimir_lista(self):
        print("============================================================")
        actual = self.primero
        while actual != None:
            print("Nivel:", actual.celda.nivel, "No. celda:", actual.celda.numero_celda,
                  "Prisionero:", actual.celda.prisionero)
            actual = actual.siguiente
        print("============================================================")
