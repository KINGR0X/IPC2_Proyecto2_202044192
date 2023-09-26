# Importaciones
import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename
from sistema_drones import sistema_drones
from contenido import contenido
from lista_sistema_drones import lista_sistema_drones
from lista_drones import lista_drones
from lista_altura import lista_altura
from lista_contenido import lista_contenido
from dron import dron
from altura import altura

# Recuperar el xml
ruta = askopenfilename()
archivo = open(ruta, "r")
archivo.close()

# Parsear para que la aplicación entienda que manipulará xml
tree = ET.parse(ruta)
raiz = tree.getroot()

# Lectura del xml
# Lista que guarda los sistemas de drones
lista_sistema_temporal = lista_sistema_drones()

lista_drones_temporal = lista_drones()

lista_contenido_temporal = lista_contenido()

lista_altura_temporal = lista_altura()

# === Guardar lista de drones ===
for drones in raiz.findall('listaDrones'):

    for dronn in drones.findall('dron'):
        nuevo_dron = dronn.text

        nuevo = dron(str(nuevo_dron))
        lista_drones_temporal.insertar_dato(nuevo)

    # === Lectura del Xml en cascada desde listaSistemasDrones ===

    for listaSDrones in raiz.findall('listaSistemasDrones'):

        for sDrones in listaSDrones.findall('sistemaDrones'):
            nombre_SistemaDron = sDrones.get('nombre')

            for alturaMax in sDrones.findall('alturaMaxima'):
                altura_maxima = alturaMax.text

                for cantidadD in sDrones.findall('cantidadDrones'):
                    cantidad_drones = cantidadD.text

                    for contenido_sistema in sDrones.findall('contenido'):
                        for dron_contenido in contenido_sistema.findall('dron'):

                            nuevo_dron_contenido = dron_contenido.text
                            # Creación del objeto dron
                            # de momento se guarda para luego añadirlo al tener las alturas
                            nombre_dron = dron(str(nuevo_dron_contenido))

                            for alturas in contenido_sistema.findall('alturas'):

                                for altura_dron in alturas.findall('altura'):
                                    # cada altura debe de tener un valor y una letra
                                    valor_altura = altura_dron.get('valor')
                                    letra_altura = str(altura_dron.text)

                                    lista_altura_temporal.insertar_dato(
                                        altura(valor_altura, letra_altura))

                                    # Se insertan los datos en la lista de contenido
                                    lista_contenido_temporal.insertar_dato(
                                        contenido(nombre_dron, lista_altura_temporal))

                                    # Se agregan las listas a la lista de sistema_drones
            lista_sistema_temporal.insertar_dato(sistema_drones(
                nombre_SistemaDron, altura_maxima, cantidad_drones, lista_drones_temporal, lista_contenido_temporal))


lista_sistema_temporal.recorrer_e_imprimir_lista()
