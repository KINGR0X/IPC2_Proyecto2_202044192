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

    def insertar_dato_ordenado(self, dron):
        nuevo_dato = nodo_dron(dron=dron)
        self.contador_celdas += 1
        # Si la lista está vacía solo añade el nuevo nodo
        if self.primero is None:
            self.primero = nuevo_dato
            return
        # Caso especial: la nueva dron debe ser el nuevo primer nodo, debe reemplazar al primero
        if dron.nombre < self.primero.dron.nombre:
            nuevo_dato.siguiente = self.primero
            self.primero = nuevo_dato
            return
        # Si no cumple con ninguno de los casos, recorrer hasta encontrar su posición
        actual = self.primero
        while actual.siguiente is not None and (
                dron.nombre > actual.siguiente.dron.nombre or (
                    dron.nombre == actual.siguiente.dron.nombre > actual.siguiente.dron.nombre)):
            actual = actual.siguiente
        nuevo_dato.siguiente = actual.siguiente
        actual.siguiente = nuevo_dato

    def recorrer_e_imprimir_lista(self):
        print()
        print("======================= Lista drones =======================")
        actual = self.primero
        while actual != None:
            print("Dron:", actual.dron.nombre)
            actual = actual.siguiente
        print("============================================================")
