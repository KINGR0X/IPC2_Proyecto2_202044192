from nodo_contenido import nodo_contenido
import sys
import os


class lista_contenido:
    def __init__(self):
        self.primero = None
        self.contador_celdas = 0

    def insertar_dato(self, contenido):
        # Si el primer nodo es nulo
        if self.primero is None:
            self.primero = nodo_contenido(contenido=contenido)
            self.contador_celdas += 1
            return
        # Temporal para recorrer nuestra lista
        actual = self.primero
        # Ejecuta el ciclo, mientras actual.siguiente exista
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_contenido(contenido=contenido)
        self.contador_celdas += 1

    def recorrer_e_imprimir_lista(self):
        print("============================================================")
        actual = self.primero
        while actual != None:
            print("Dron:", actual.contenido.dron.nombre)

            actual.contenido.lista_alturas.recorrer_e_imprimir_lista()
            actual = actual.siguiente
        print("============================================================")
