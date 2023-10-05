from nodo_drones_salida import nodo_drones_salida
import xml.etree.ElementTree as ET


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

    def graficar_salida(self, nombre_dronesM):

        # Grafica del contenido
        actual = self.primero
        while actual != None:
            if actual.drones_salida.NombreMensaje == nombre_dronesM:
                dot = actual.drones_salida.lista_contenido_m.graficar_mensajeM(
                    actual.drones_salida.NombreMensaje, actual.drones_salida.SistemaDrones, str(actual.drones_salida.tiempoOptimo), actual.drones_salida.mensaje_desencriptado)
            # actual.drones_salida.lista_patrones_celdas.recorrer_e_imprimir_lista()
                return dot
            actual = actual.siguiente

    # Generar XML de salida
    def generar_xml_salida(self, direccion):
        actual = self.primero
        # creación del xml de salida
        mis_carceles = ET.Element("respuesta")

        # Tercero etiqueta <ListaMensajes>
        lista_mensajes = ET.SubElement(mis_carceles, "listaMensajes")

        # El while es para graficar cada carcel
        actual = self.primero
        while actual != None:

            nombreM = ET.SubElement(
                lista_mensajes, "mensaje nombre="+"\""+actual.drones_salida.NombreMensaje+"\"")

            sistemaDrones = ET.SubElement(nombreM, "sistemaDrones")
            sistemaDrones.text = actual.drones_salida.SistemaDrones

            tiempo_optimo = ET.SubElement(nombreM, "tiempoOptimo")
            tiempo_optimo.text = str(actual.drones_salida.tiempoOptimo)

            mensaje_desencriptado = ET.SubElement(
                nombreM, "mensajeRecibido")
            mensaje_desencriptado.text = actual.drones_salida.mensaje_desencriptado

            instrucciones = ET.SubElement(nombreM, "instrucciones")

            # ciclo de los tiempos, donde dentro de cada tiempo va el dron, por ejemplo tiempo 1, dron 1, dron 2, dron 3
            contador = 0

            # for para que el contador llegue a ser el tiempo optimo
            for i in range(actual.drones_salida.tiempoOptimo):
                tiempo = ET.SubElement(
                    instrucciones, "tiempo valor="+"\""+str(i+1)+"\"")

                acciones = ET.SubElement(tiempo, "acciones")

                # dentro del ciclo de los tiempos se hace otro ciclo para recorrer los drones
                actual2 = actual.drones_salida.lista_contenido_m.primero
                while actual2 != None:
                    dron = ET.SubElement(
                        acciones, "dron nombre="+"\""+actual2.contenido_m.dron+"\"")

                    # se crea otro ciclo para recorrer las acciones de cada dron
                    actual3 = actual2.contenido_m.lista_tiempo.primero
                    while actual3 != None:
                        # si se encuentra el tiempo en el coontado+1 se agrega la accion
                        if actual3.tiempo.valor == contador+1:
                            dron.text = actual3.tiempo.accion
                            break

                        actual3 = actual3.siguiente

                    actual2 = actual2.siguiente

                contador += 1

            actual = actual.siguiente

        # Generar xml
        my_data = ET.tostring(mis_carceles)
        my_data = str(my_data)
        self.xml_arreglado(mis_carceles)

        arbol_xml = ET.ElementTree(mis_carceles)
        arbol_xml.write(direccion, encoding="UTF-8", xml_declaration=True)

    def xml_arreglado(self, element, indent='  '):
        # Inicializar una cola con el elemento raíz y nivel de anidación 0
        queue = [(0, element)]  # (level, element)
        # Bucle principal: continúa mientras haya elementos en la cola
        while queue:
            # Extraer nivel y elemento actual de la cola
            level, element = queue.pop(0)
            # Crear tuplas para cada hijo con nivel incrementado
            children = [(level + 1, child) for child in list(element)]
            # Agregar saltos de línea e indentación al inicio del elemento actual
            if children:
                element.text = '\n' + indent * (level + 1)
                # Agregar saltos de línea e indentación al final del elemento actual
            if queue:
                element.tail = '\n' + indent * queue[0][0]
            else:
                # Si este es el último elemento del nivel actual, reducir la indentación
                element.tail = '\n' + indent * (level - 1)
            # Insertar las tuplas de hijos al principio de la cola
            queue[0:0] = children
