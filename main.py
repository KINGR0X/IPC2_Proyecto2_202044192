# Importaciones
import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from sistema_drones import sistema_drones
from contenido import contenido
from lista_sistema_drones import lista_sistema_drones
from lista_drones import lista_drones
from lista_altura import lista_altura
from lista_contenido import lista_contenido
from dron import dron
from altura import altura
from colorama import init, Fore, Back, Style
import os
from lista_mensaje import lista_mensaje
from mensaje import mensaje
from lista_instruccion import lista_instruccion
from instruccion import instruccion


def cargar_archivo(lista_dron, lista_sistemas, lista_mensajes):
    # Recuperar el xml
    ruta = askopenfilename()
    archivo = open(ruta, "r")
    archivo.close()

    # Parsear para que la aplicación entienda que manipulará xml
    tree = ET.parse(ruta)
    raiz = tree.getroot()

    # Lectura del xml
    # Lista que guarda los sistemas de drones
    lista_drones_temporal = lista_drones()
    lista_sistema_temporal = lista_sistema_drones()
    lista_mensajes_temporal = lista_mensaje()

    # === Guardar lista de drones ===
    for drones in raiz.findall('listaDrones'):

        for dronn in drones.findall('dron'):
            nuevo_dron = dronn.text

            nuevo = dron(str(nuevo_dron))

            lista_dron.insertar_dato_ordenado(nuevo)

    # === Guardar lista mensajes ===
    for lmensaje in raiz.findall('listaMensajes'):

        for mensajes in lmensaje.findall('Mensaje'):
            nuevomensaje = mensajes.get('nombre')

            for sistemaDrones in mensajes.findall('sistemaDrones'):

                mensaje_sistemaD = sistemaDrones.text

            for instrucciones in mensajes.findall('instrucciones'):
                # inicializacion de la lista de instrucciones
                lista_instrucciones_temporal = lista_instruccion()

                for instruccionM in instrucciones.findall('instruccion'):

                    nueva_instruccion = instruccionM.get("dron")
                    nueva_altura_instruccion = instruccionM.text

                    objeto_instrucciones = instruccion(
                        str(nueva_instruccion), str(nueva_altura_instruccion))

                    lista_instrucciones_temporal.insertar_dato(
                        objeto_instrucciones)

                    nuevo_mensaje = mensaje(
                        str(nuevomensaje), str(mensaje_sistemaD),  lista_instrucciones_temporal)

            lista_mensajes.insertar_dato_ordenado(nuevo_mensaje)

        # === Lectura del Xml en cascada desde listaSistemasDrones ===

        for listaSDrones in raiz.findall('listaSistemasDrones'):

            for sDrones in listaSDrones.findall('sistemaDrones'):
                lista_contenido_temporal = lista_contenido()
                nombre_SistemaDron = sDrones.get('nombre')

                for alturaMax in sDrones.findall('alturaMaxima'):
                    altura_maxima = alturaMax.text

                    for cantidadD in sDrones.findall('cantidadDrones'):
                        cantidad_drones = cantidadD.text

                        for contenido_sistema in sDrones.findall('contenido'):
                            # inicialización de listas
                            lista_altura_temporal = lista_altura()

                            for dron_contenido in contenido_sistema.findall('dron'):

                                nuevo_dron_contenido = dron_contenido.text
                                # Creación del objeto dron
                                # de momento se guarda para luego añadirlo al tener las alturas
                                nombre_dron = dron(str(nuevo_dron_contenido))
                                # print(nombre_dron.nombre)

                                for alturas in contenido_sistema.findall('alturas'):

                                    for altura_dron in alturas.findall('altura'):
                                        # cada altura debe de tener un valor y una letra
                                        valor_altura = altura_dron.get('valor')
                                        letra_altura = str(altura_dron.text)

                                        altura_temporal = altura(
                                            valor_altura, letra_altura)

                                        lista_altura_temporal.insertar_dato(
                                            altura_temporal)

                                # Se insertan los datos en la lista de contenido
                            lista_contenido_temporal.insertar_dato(
                                contenido(nombre_dron, lista_altura_temporal))

                        # Se agregan las listas a la lista de sistema_drones
                lista_sistemas.insertar_dato(sistema_drones(
                    nombre_SistemaDron, altura_maxima, cantidad_drones, lista_contenido_temporal))

    # lista_sistema_temporal.recorrer_e_imprimir_lista()
    # return lista_sistema_temporal, lista_drones_temporal


def imprimir_nombres_sistemas_drones(lista_sistema_temporal):
    # variable para guardar los nombres de los sistemas de drones
    listaD = "Ingrese el número del sistema de drones \n"

    # === Imprimir las señales que hay en el archivo ===
    actual = lista_sistema_temporal.primero
    contador = 0
    while actual != None:
        contador += 1
        listaD += str(contador)+". "+actual.sistema_drones.nombre
        listaD += "\n"
        # print(Fore.WHITE+str(contador)+". "+actual.sistema_drones.nombre)
        actual = actual.siguiente

    return listaD

# Funcion para graficar


def generar_grafica_original(nombreSignal, lista_sistema_temporal, direccion_grafica):

    nombreOriginal = direccion_grafica+"_original"
    nombre = nombreOriginal+".dot"
    f = open(nombre, 'w')
    # se guara todo el texto y se cierra el archivo
    f.write(str(lista_sistema_temporal.graficar_mi_lista_original(nombreSignal)))
    f.close()
    os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
    # se pasa el archivo a png
    os.system("""dot -Tpng """+nombre+""" -o """+nombreOriginal+""".png""")


def imprimir_nombres_lista_drones(lista_drones_temporal):
    # variable para guardar los nombres de los sistemas de drones
    listaDrones = "Listado de drones \n"

    # === Imprimir las señales que hay en el archivo ===
    actual = lista_drones_temporal.primero
    while actual != None:
        listaDrones += actual.dron.nombre
        listaDrones += "\n"

        actual = actual.siguiente

    return listaDrones


def imprimir_lista_mensajes(lista_mensajes):

    # variable para guardar los nombres de los sistemas de drones
    listaDrones = "Listado de mensajes \n"

    # === Imprimir las señales que hay en el archivo ===
    actual = lista_mensajes.primero
    while actual != None:
        listaDrones += "\n"
        listaDrones += "Nombre: " + actual.mensaje.nombre
        listaDrones += "\n"
        listaDrones += "Sistema de drones: " + actual.mensaje.sistemaDrones

        listaDrones += actual.mensaje.lista_instruccion.recorrer_e_imprimir_lista()

        actual = actual.siguiente
        listaDrones += "\n"

    return listaDrones


# Mostrar lista de drones
def imprimir_mensajes(lista_mensajes):

    # variable para guardar los nombres de los sistemas de drones
    listaDrones = "Escoja un mensaje para mostrar \n"
    contador = 1
    # === Imprimir las señales que hay en el archivo ===
    actual = lista_mensajes.primero
    while actual != None:
        listaDrones += "\n"
        listaDrones += str(contador)+". "+"Nombre: " + actual.mensaje.nombre
        listaDrones += "\n"
        listaDrones += "Sistema de drones: " + actual.mensaje.sistemaDrones

        contador += 1
        actual = actual.siguiente
        listaDrones += "\n"

    return listaDrones
