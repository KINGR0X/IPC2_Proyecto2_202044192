from nodo_mensaje import nodo_mensaje
import sys
import os


class lista_mensaje:
    def __init__(self):
        self.primero = None
        self.contador_celdas = 0

    def insertar_dato(self, mensaje):
        # Si el primer nodo es nulo
        if self.primero is None:
            self.primero = nodo_mensaje(mensaje=mensaje)
            self.contador_celdas += 1
            return
        # Temporal para recorrer nuestra lista
        actual = self.primero
        # Ejecuta el ciclo, mientras actual.siguiente exista
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_mensaje(mensaje=mensaje)
        self.contador_celdas += 1

    def insertar_dato_ordenado(self, mensaje):
        nuevo_dato = nodo_mensaje(mensaje=mensaje)
        self.contador_celdas += 1
        # Si la lista está vacía solo añade el nuevo nodo
        if self.primero is None:
            self.primero = nuevo_dato
            return
        # Caso especial: la nueva mensaje debe ser el nuevo primer nodo, debe reemplazar al primero
        if mensaje.nombre < self.primero.mensaje.nombre:
            nuevo_dato.siguiente = self.primero
            self.primero = nuevo_dato
            return
        # Si no cumple con ninguno de los casos, recorrer hasta encontrar su posición
        actual = self.primero
        while actual.siguiente is not None and (
                mensaje.nombre > actual.siguiente.mensaje.nombre or (
                    mensaje.nombre == actual.siguiente.mensaje.nombre > actual.siguiente.mensaje.nombre)):
            actual = actual.siguiente
        nuevo_dato.siguiente = actual.siguiente
        actual.siguiente = nuevo_dato

    # def recorrer_e_imprimir_lista(self):
    #     print()
    #     print("======================= Lista Mensajes =======================")
    #     actual = self.primero
    #     while actual != None:
    #         print("Mensaje:", actual.mensaje.nombre)
    #         print("Sistema de drones:", actual.mensaje.sistemaDrones)
    #         # recorrer lista de instrucciones
    #         actual.mensaje.lista_instruccion.recorrer_e_imprimir_lista()
    #         actual = actual.siguiente
    #     print("============================================================")
