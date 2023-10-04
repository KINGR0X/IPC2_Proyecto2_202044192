from nodo_drones_salida import nodo_drones_salida


class lista_drones_salida:
    def __init__(self):
        self.primero = None
        self.contador_sistemas_drones = 0

    def insertar_dato(self, drones_salida):
        if self.primero is None:
            self.primero = nodo_drones_salida(drones_salida=drones_salida)
            self.contador_sistemas_drones += 1
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_drones_salida(drones_salida=drones_salida)
        self.contador_sistemas_drones += 1

    def recorrer_e_imprimir_lista(self):
        print("")
        print("Total de sistema de salida:",
              self.contador_sistemas_drones)
        print("")
        print("============================================================")
        actual = self.primero
        while actual != None:
            print("Nombre del mensaje: ", actual.drones_salida.NombreMensaje)
            print("Sistema de drones: ", actual.drones_salida.SistemaDrones)
            print("Tiempo optimo: ", actual.drones_salida.tiempoOptimo)
            print("Mensaje desencriptado: ",
                  actual.drones_salida.mensaje_desencriptado)

            # actual.drones_salida.lista_drones.recorrer_e_imprimir_lista()
            actual.drones_salida.lista_contenido_m.recorrer_e_imprimir_lista()
            actual = actual.siguiente
            print("")
        print("============================================================")
        print("")
        print("")
        print("")

    # def graficar_mi_lista_original(self, nombre_signal):

    #     # Grafica del contenido
    #     actual = self.primero
    #     while actual != None:
    #         if actual.drones_salida.nombre == nombre_signal:
    #             dot = actual.drones_salida.lista_contenido.graficar(actual.drones_salida.nombre,
    #                                                                 str(
    #                                                                     actual.drones_salida.alturaMaxima),
    #                                                                 str(actual.drones_salida.cantidadDrones))
    #         # actual.drones_salida.lista_patrones_celdas.recorrer_e_imprimir_lista()
    #             return dot
    #         actual = actual.siguiente
