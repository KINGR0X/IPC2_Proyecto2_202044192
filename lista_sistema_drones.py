from nodo_sistema_drones import nodo_sistema_drones


class lista_sistema_drones:
    def __init__(self):
        self.primero = None
        self.contador_sistemas_drones = 0

    def insertar_dato(self, sistema_drones):
        if self.primero is None:
            self.primero = nodo_sistema_drones(sistema_drones=sistema_drones)
            self.contador_sistemas_drones += 1
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_sistema_drones(sistema_drones=sistema_drones)
        self.contador_sistemas_drones += 1

    def recorrer_e_imprimir_lista(self):
        print("")
        print("Total de sistema de drones almacenados:",
              self.contador_sistemas_drones)
        print("")
        print("============================================================")
        actual = self.primero
        while actual != None:
            print("Nombre:", actual.sistema_drones.nombre, "Altura maxima:",
                  actual.sistema_drones.alturaMaxima, "Cantidad drones:", actual.sistema_drones.cantidadDrones)

            # actual.sistema_drones.lista_drones.recorrer_e_imprimir_lista()
            actual.sistema_drones.lista_contenido.recorrer_e_imprimir_lista()
            actual = actual.siguiente
            print("")
        print("============================================================")
        print("")
        print("")
        print("")

    def graficar_mi_lista_original(self, nombre_signal):
        actual = self.primero
        while actual != None:
            if actual.sistema_drones.nombre == nombre_signal:
                dot = actual.sistema_drones.lista_contenido.graficar(actual.sistema_drones.nombre,
                                                                     str(
                                                                         actual.sistema_drones.alturaMaxima),
                                                                     str(actual.sistema_drones.cantidadDrones))
            # actual.sistema_drones.lista_patrones_celdas.recorrer_e_imprimir_lista()
                return dot
            actual = actual.siguiente
