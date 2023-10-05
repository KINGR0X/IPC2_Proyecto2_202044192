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
from lista_contenido_m import lista_contenido_m
from contenido_m import contenido_m
from tiempo import tiempo
from lista_tiempo import lista_tiempo
from drones_salida import drones_salida
from lista_drones_salida import lista_drones_salida
# from lista_contenido_m import graficar_mensajeM


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

    # antes de agregar el sistema de drones a la lista se debe de verificar si no es repetido

    # === Guardar lista de drones ===
    for drones in raiz.findall('listaDrones'):

        for dronn in drones.findall('dron'):
            nuevo_dron = dronn.text

            nuevo = dron(str(nuevo_dron))

            # antes de agregar el sistema se verifica si ya anteriormente se agrego un sistema con el mismo nombre
            if lista_dron.primero != None:
                ultimoNodo = False
                sistemaEncontrado = False
                actual = lista_dron.primero
                while actual != None:

                    # Solo si luego de buscar en toda la lista NO encuentra el nuevo_dron, se agrega a la lista

                    if actual.siguiente == None:
                        ultimoNodo = True

                    if nuevo_dron == actual.dron.nombre:
                        sistemaEncontrado = True

                    if sistemaEncontrado == False and ultimoNodo == True:
                        # Se agregan las listas a la lista de sistema_drones
                        lista_dron.insertar_dato_ordenado(nuevo)

                    actual = actual.siguiente
            else:
                # Se agregan las listas a la lista de sistema_drones
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

            # antes de agregar el sistema se verifica si ya anteriormente se agrego un mensaje con el mismo nombre
            if lista_mensajes.primero != None:
                ultimoNodo = False
                sistemaEncontrado = False
                actual = lista_mensajes.primero
                while actual != None:

                    # Solo si luego de buscar en toda la lista NO encuentra el nombre_SistemaDron, se agrega a la lista

                    if actual.siguiente == None:
                        ultimoNodo = True

                    if nuevomensaje == actual.mensaje.nombre:
                        sistemaEncontrado = True

                    if sistemaEncontrado == False and ultimoNodo == True:
                        lista_mensajes.insertar_dato_ordenado(nuevo_mensaje)

                    actual = actual.siguiente
            else:
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

                # antes de agregar el sistema se verifica si ya anteriormente se agrego un sistema con el mismo nombre
                if lista_sistemas.primero != None:
                    ultimoNodo = False
                    sistemaEncontrado = False
                    actual = lista_sistemas.primero
                    while actual != None:

                        # Solo si luego de buscar en toda la lista NO encuentra el nombre_SistemaDron, se agrega a la lista

                        if actual.siguiente == None:
                            ultimoNodo = True

                        if nombre_SistemaDron == actual.sistema_drones.nombre:
                            sistemaEncontrado = True

                        if sistemaEncontrado == False and ultimoNodo == True:
                            lista_sistemas.insertar_dato(sistema_drones(
                                nombre_SistemaDron, altura_maxima, cantidad_drones, lista_contenido_temporal))

                        actual = actual.siguiente
                else:
                    # # Se agregan las listas a la lista de sistema_drones
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


def generar_grafica_instrucciones_dron(nombre_dronesM, lista_salidaM, direccion_grafica2):

    nombreOriginal = direccion_grafica2+"_original"
    nombre = nombreOriginal+".dot"
    f = open(nombre, 'w')
    # se guara todo el texto y se cierra el archivo
    f.write(str(lista_salidaM.graficar_salida(nombre_dronesM)))
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

# === con lista de instrucciones ===


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


# === Imprimir solo el mensaje ===
def imprimir_mensajes(lista_salidaM):
    # variable para guardar los nombres de los sistemas de drones
    listaDrones = "Escoja un mensaje para mostrar (ingrese el numero del mensaje) \n"
    contador = 1
    # === Imprimir las señales que hay en el archivo ===
    actual = lista_salidaM.primero
    while actual != None:
        listaDrones += "\n"
        listaDrones += str(contador)+". "+"Nombre: " + \
            actual.drones_salida.NombreMensaje
        listaDrones += "\n"
        listaDrones += "Sistema de drones: " + actual.drones_salida.SistemaDrones
        listaDrones += "\n"
        listaDrones += "Tiempo optimo: " + \
            str(actual.drones_salida.tiempoOptimo)
        listaDrones += "\n"
        listaDrones += "Mensaje que se enviara: " + \
            actual.drones_salida.mensaje_desencriptado

        contador += 1
        actual = actual.siguiente
        listaDrones += "\n"

    return listaDrones


# === descifrar mensaje ===
def descifrar_mensaje_salida(lista_mensajes, drones_salidaM, lista_sistema_drones):

    # === Se recorre la lista mensaje para ejecutar las instrucciones que indica ===
    actual = lista_mensajes.primero
    while actual != None:

        # con el sistema drones que indica el mensaje, se busca en la lista_sistema_drones el sistema de drones que se seleccionó
        mensaje_seleccionado = actual.mensaje.sistemaDrones

        mensaje_descifrado = ""
        actual2 = lista_sistema_drones.primero
        while actual2 != None:

            if actual2.sistema_drones.nombre == mensaje_seleccionado:
                # Se guarda el sistema de drones que se seleccionó
                sistema_drones_seleccionado = actual2.sistema_drones
                lista_instrucciones_select = actual.mensaje.lista_instruccion

                # Se recorre la lista de instrucciones ej: dron="DronW" (1)

                actual3 = lista_instrucciones_select.primero
                while actual3 != None:
                    # print("Dron: ", actual3.instruccion.dron)
                    # print("Altura: ", actual3.instruccion.altura)

                    # Se recorre la lista de contenido del sistema de drones seleccionado
                    actual4 = sistema_drones_seleccionado.lista_contenido.primero
                    while actual4 != None:

                        # Se verifica si el dron de la lista de instrucciones es igual al dron de la lista de contenido
                        if actual3.instruccion.dron == actual4.contenido.dron.nombre:

                            # Se recorre la lista de alturas del dron seleccionado
                            actuald = actual4.contenido.lista_altura.primero
                            while actuald != None:
                                # Se verifica si el valor de la instrucción es igual al valor de la altura
                                if actual3.instruccion.altura == actuald.altura.valor:
                                    # Se guarda la letra de la altura
                                    mensaje_descifrado += actuald.altura.letra
                                    # print("Letra descifrada:",
                                    #       actuald.altura.letra)
                                    break
                                actuald = actuald.siguiente
                            break
                        actual4 = actual4.siguiente

                    actual3 = actual3.siguiente
            actual2 = actual2.siguiente

        # se le pasa la lista_contenidoM de la lista de drones_salidaM para que se pueda llenar
        lista_contenidoM = lista_contenido_m()
        Crear_instrucciones_mensaje(
            mensaje_seleccionado, lista_sistema_drones, lista_instrucciones_select, lista_contenidoM)

        # Se encuentra el tiempo optimo
        tiempoOp = encontrar_tiempo_optimo(lista_contenidoM)

        # Se rellenan los nodos con ESPERAR
        rellenar_nodos_tiempo_optimo(lista_contenidoM, tiempoOp)

        # print(mensaje_descifrado)
        datosMensaje = drones_salida(actual.mensaje.nombre, actual.mensaje.sistemaDrones,
                                     tiempoOp, mensaje_descifrado, lista_contenidoM)

        drones_salidaM.insertar_dato(datosMensaje)

        actual = actual.siguiente


# === Sirve para  llenar la lista de lista_contenido_m===
def Crear_instrucciones_mensaje(mensaje_seleccionado, lista_sistema_drones, lista_instrucciones_select, lista_contenidoM):

    lista_contenido_m_temporal = lista_contenido_m()
    tiempo_anterior = 0

    # === Se busca en la lista_sistema_drones el sistema de drones que se seleccionó ===
    # print("Sistema de drones del mensaje seleccionado:", mensaje_seleccionado)

    # === Se busca en la lista_sistema_drones el sistema de drones que se seleccionó ===
    actual = lista_sistema_drones.primero
    while actual != None:
        if actual.sistema_drones.nombre == mensaje_seleccionado:
            # Se guarda el sistema de drones que se seleccionó
            sistema_drones_seleccionado = actual.sistema_drones
            # print
            break
        actual = actual.siguiente

    # Contador para los tiempos
    contador_tiempo = 0

    # === Se recorre la lista de instrucciones del mensaje seleccionado ===
    lista_tiempo_temporal_anterior = lista_tiempo()
    actual = lista_instrucciones_select.primero
    while actual != None:
        # print("Dron: ", actual.instruccion.dron)
        # print("Altura: ", actual.instruccion.altura)

        # === Se recorre la lista de contenido del sistema de drones seleccionado ===

        lista_tiempo_temporal = lista_tiempo()
        nuevaInstruccionParaDron = False
        actual2 = sistema_drones_seleccionado.lista_contenido.primero
        while actual != None:

            # Se verifica si el dron de la lista de instrucciones es igual al dron de la lista de contenido
            if actual.instruccion.dron == actual2.contenido.dron.nombre:

                # === Se verifica si es una nueva instruccion ara un dron que ya recibio una instruccion ===
                actualComprobar = lista_contenidoM.primero
                while actualComprobar != None:

                    if actual.instruccion.dron == actualComprobar.contenido_m.dron:
                        nuevaInstruccionParaDron = True
                        break

                    actualComprobar = actualComprobar.siguiente

                if nuevaInstruccionParaDron == True:

                    # === Se verifica si ya anteriormente se recorrio un dron con el mismo nombre, para ver si debe de subir o bajar. Para ello se vuelve a reccorrer la lista de drones ===

                    # === actual 4 va una instruccion antes que actual ===
                    actual4 = lista_instrucciones_select.primero
                    while actual != None:

                        if (actual.instruccion.dron == actual4.instruccion.dron) and (actual.instruccion.altura != actual4.instruccion.altura):
                            # print("Dron: ", actual.instruccion.dron)
                            # print("Altura: ", actual.instruccion.altura)

                            # === Se agregan los nuevos nodos ===
                            actual5 = lista_contenidoM.primero
                            while actual5 != None:

                                # se agrega al dron que recibe los nuevos nodos
                                if actual5.contenido_m.dron == actual.instruccion.dron:

                                    contador_celdas = actual5.contenido_m.lista_tiempo.contador_celdas

                                    print(
                                        "actual", actual.instruccion.altura)
                                    print(
                                        "actual4", actual4.instruccion.altura)

                                    # === Se verifica si debe de subir o bajar el dron ===
                                    if actual.instruccion.altura > actual4.instruccion.altura:
                                        # se recupera la lista y se le debe de agregar los nuevos movimientos
                                        lista_contenidoM

                                        cantidadSubir = abs(int(
                                            actual4.instruccion.altura) - int(actual.instruccion.altura))
                                        print("Cantidad subir", cantidadSubir)
                                        # se crea un ciclo para ver cuantos nodos de bajar se deben de crear
                                        for i in range(cantidadSubir):
                                            i += 1
                                            contador_tiempo += 1
                                            # se crea el valor del tiempo
                                            tiempo_temporal = tiempo(
                                                contador_tiempo+contador_celdas, "Subir")

                                            actual5.contenido_m.lista_tiempo.insertar_dato(
                                                tiempo_temporal)

                                        contador_tiempo += 1
                                        # se crea el valor del tiempo
                                        tiempo_temporal = tiempo(
                                            contador_tiempo+contador_celdas, "Emitir luz")

                                        actual5.contenido_m.lista_tiempo.insertar_dato(
                                            tiempo_temporal)

                                        actual = actual.siguiente

                                    else:

                                        # se recupera la lista y se le debe de agregar los nuevos movimientos
                                        lista_contenidoM

                                        cantidadBajar = abs(int(
                                            actual4.instruccion.altura) - int(actual.instruccion.altura))

                                        # se crea un ciclo para ver cuantos nodos de bajar se deben de crear
                                        for i in range(cantidadBajar):
                                            i += 1
                                            contador_tiempo += 1
                                            # se crea el valor del tiempo
                                            tiempo_temporal = tiempo(
                                                contador_tiempo+contador_celdas, "Bajar")

                                            actual5.contenido_m.lista_tiempo.insertar_dato(
                                                tiempo_temporal)

                                        contador_tiempo += 1
                                        # se crea el valor del tiempo
                                        tiempo_temporal = tiempo(
                                            contador_tiempo+contador_celdas, "Emitir luz")

                                        actual5.contenido_m.lista_tiempo.insertar_dato(
                                            tiempo_temporal)

                                        actual = actual.siguiente
                                    break
                                actual5 = actual5.siguiente

                        actual4 = actual4.siguiente
                        # nuevaInstruccionParaDron = False
                else:
                    # === Se recorre cada dron y su lista de alturas  hasta encontrar la letra, al encontrar la letra se emite la luz===
                    actual3 = actual2.contenido.lista_altura.primero
                    while actual3 != None:

                        # === PRIMERO SE DEBE DE SUBIR TODOS LOS DRONES SIEMPRE ===
                        contador_tiempo += 1
                        # se crea el valor del tiempo
                        tiempo_temporal = tiempo(
                            contador_tiempo, "Subir")
                        lista_tiempo_temporal.insertar_dato(
                            tiempo_temporal)

                        lista_tiempo_temporal_anterior.insertar_dato(
                            tiempo_temporal)

                        # Si se encuentra la letra de la altura se emite la luz
                        if actual.instruccion.altura == actual3.altura.valor:
                            # print("tiempo anterior: ", tiempo_anterior)
                            # print("contador tiempo: ", contador_tiempo)

                            # Usando tiempo_anterior, se crea un ciclo para que se espere hasta que se pueda emitir la luz
                            if contador_tiempo < tiempo_anterior:
                                while contador_tiempo < tiempo_anterior:
                                    contador_tiempo += 1
                                    # se crea el valor del tiempo
                                    tiempo_temporal = tiempo(
                                        contador_tiempo, "Esperar")
                                    lista_tiempo_temporal.insertar_dato(
                                        tiempo_temporal)

                                    lista_tiempo_temporal_anterior.insertar_dato(
                                        tiempo_temporal)

                            # al terminar la espera se le suma uno al contador y se emite la luz
                            contador_tiempo += 1
                            # se crea el valor del tiempo
                            tiempo_temporal = tiempo(
                                contador_tiempo, "Emitir luz")
                            lista_tiempo_temporal.insertar_dato(
                                tiempo_temporal)

                            lista_tiempo_temporal_anterior.insertar_dato(
                                tiempo_temporal)

                            tiempo_anterior = contador_tiempo

                            break
                        actual3 = actual3.siguiente
                    break
            actual2 = actual2.siguiente

        # === If para evitar que cuando se le pasa una nueva instruccion a un dron no cree un nodo solo con el nombre del dron ===
        if nuevaInstruccionParaDron == False:
            lista_contenidoM.insertar_dato(contenido_m(
                actual.instruccion.dron, lista_tiempo_temporal))
            nuevaInstruccionParaDron = False

        contador_tiempo = 0

        if actual!= None:
            actual = actual.siguiente
        else:
            break
        # print(actual.instruccion.altura)


# === Encontrar tiempo optimo de la lista de lista_contenido_m y rellenar espacios con ESPERAR===

def encontrar_tiempo_optimo(lista_contenidoM):

    # === Se recorre la lista de lista_contenido_m ===
    actual = lista_contenidoM.primero
    tiempo_optimo = 0
    while actual != None:

        # === Se recorre la lista de tiempos de cada dron ===
        # y se busca el que tenga mayor cantidad de nodos

        contador_actual = actual.contenido_m.lista_tiempo.contador_celdas

        if contador_actual > tiempo_optimo:
            tiempo_optimo = contador_actual

        contador_anterior = actual.contenido_m.lista_tiempo.contador_celdas

        actual = actual.siguiente

    # print(tiempo_optimo)
    return tiempo_optimo


# Se rellenan los espacios con ESPERAR
def rellenar_nodos_tiempo_optimo(lista_contenidoM, tiempo_optimo):

    # === Se recorre la lista de lista_contenido_m ===
    actual = lista_contenidoM.primero
    while actual != None:

        # === Se recorre la lista de tiempos de cada dron ===
        # y se busca el que tenga mayor cantidad de nodos

        contador_actual = actual.contenido_m.lista_tiempo.contador_celdas

        if contador_actual < tiempo_optimo:

            # Se crea un ciclo para rellenar los nodos faltantes con ESPERAR
            for i in range(tiempo_optimo - contador_actual):
                i += 1
                # se crea el valor del tiempo
                tiempo_temporal = tiempo(i+contador_actual, "Esperar")
                actual.contenido_m.lista_tiempo.insertar_dato(
                    tiempo_temporal)

        actual = actual.siguiente
