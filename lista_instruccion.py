from nodo_instruccion import nodo_instruccion
import sys
import os


class lista_instruccion:
    def __init__(self):
        self.primero = None
        self.contador_celdas = 0

    def insertar_dato(self, instruccion):
        # Si el primer nodo es nulo
        if self.primero is None:
            self.primero = nodo_instruccion(instruccion=instruccion)
            self.contador_celdas += 1
            return
        # Temporal para recorrer nuestra lista
        actual = self.primero
        # Ejecuta el ciclo, mientras actual.siguiente exista
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_instruccion(instruccion=instruccion)
        self.contador_celdas += 1

    def recorrer_e_imprimir_lista(self):
        # variable para guardar los nombres de los sistemas de drones
        listaDrones = ""
        # === Imprimir las señales que hay en el archivo ===
        actual = self.primero
        while actual != None:
            listaDrones += "\n"
            listaDrones += "Dron: " + actual.instruccion.dron + \
                "; "+"Altura: " + actual.instruccion.altura

            # print(actual.instruccion.dron)
            # print(actual.instruccion.altura)
            actual = actual.siguiente

        return listaDrones
