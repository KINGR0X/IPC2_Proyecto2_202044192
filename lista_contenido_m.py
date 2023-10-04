from nodo_contenido_m import nodo_contenido_m
from sistema_drones import sistema_drones
import sys
import os


class lista_contenido_m:
    def __init__(self):
        self.primero = None
        self.contador_celdas = 0

    def insertar_dato(self, contenido_m):
        # Si el primer nodo es nulo
        if self.primero is None:
            self.primero = nodo_contenido_m(contenido_m=contenido_m)
            self.contador_celdas += 1
            return
        # Temporal para recorrer nuestra lista
        actual = self.primero
        # Ejecuta el ciclo, mientras actual.siguiente exista
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_contenido_m(contenido_m=contenido_m)
        self.contador_celdas += 1

    def recorrer_e_imprimir_lista(self):
        print("============================================================")
        actual = self.primero
        while actual != None:
            print("Dron:", actual.contenido_m.dron)

            actual.contenido_m.lista_tiempo.recorrer_e_imprimir_lista()
            actual = actual.siguiente
        print("============================================================")

    def graficar_mensajeM(self, nombre_mensaje, sistema_drones, TiempoOptimo, mensaje_desencriptado):
        # f = open('bb.dot', 'w')
        # variable que conmtiene la configuración del grafo
        # se crea el subgrafo primero
        text = """
digraph G {
subgraph {
nodo_00[label=" """+nombre_mensaje+""" ",fontcolor="#000000",fillcolor=gold, style=filled,shape=box];
nodo_01_left[label="Sistema drones\\n"""+sistema_drones+"""",fontcolor="#000000",fillcolor=gold, style=filled,shape=box];
nodo_00 -> nodo_01_left;
nodo_01_right[label="Tiempo optimo\n"""+TiempoOptimo+"""",fontcolor="#000000",fillcolor=gold, style=filled,shape=box];
nodo_00 -> nodo_01_right;
nodo_02_right[label="Mensaje que se enviara\n"""+mensaje_desencriptado+"""",fontcolor="#000000",fillcolor=gold, style=filled,shape=box];
nodo_00 -> nodo_02_right;
}

fontname="Helvetica,Arial,sans-serif"
node [fontname="Helvetica,Arial,sans-serif"]
edge [fontname="Helvetica,Arial,sans-serif"]
a0 [shape=none label=<
<TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="#088395" gradientangle="315">
            """

        # Primero se deben de graficar las alturas tomando en cuenta la tiempo maxima
        contador = int(TiempoOptimo)+1
        actual = self.primero
        # for que use el contador
        for i in range(contador):
            if i == 0:
                text += """<TR>"""
                text += """<TD border="3"  bgcolor="gold" gradientangle="315">""" + \
                    str("Alturas")+"""</TD>\n"""
            else:
                text += """<TD border="3"  bgcolor="gold" gradientangle="315">""" + \
                    str(i)+"""</TD>\n"""

        text += """</TR>"""

        actual = self.primero
        # iniciaria en 1, verifica si se cambio de linea
        sentinela_de_filas = actual.contenido_m.dron
        fila_iniciada = False  # para saber si se inicio una nueva fila

        while actual != None:
            # Si el dron actual es diferente al que viene, ej: DronX y el siguiente es DronY
            if sentinela_de_filas != actual.contenido_m.dron:
                sentinela_de_filas = actual.contenido_m.dron
                # aun no se inicia una nueva fila por lo que es False
                fila_iniciada = False
                # Cerramos la fila
                text += """</TR>\n"""

            # si la fila iniciada es False es porque se acaba de cerrar una fila, entonces inicializamos la nueva fila
            if fila_iniciada == False:
                fila_iniciada = True
                # Abrimos la fila
                text += """<TR>"""
                text += """<TD border="3"  bgcolor="orangered" gradientangle="315">""" + \
                    str(actual.contenido_m.dron)+"""</TD>\n"""

                # Lista de tiempos
                actualL = actual.contenido_m.lista_tiempo.primero
                while actualL != None:

                    if actualL.tiempo.accion == "Emitir luz":

                        text += """<TD border="3"  bgcolor="gold" gradientangle="315">""" + \
                            str(actualL.tiempo.accion) + \
                            """</TD>\n"""

                    elif actualL.tiempo.accion == "Esperar":

                        text += """<TD border="3"  bgcolor="cornflowerblue" gradientangle="315">""" + \
                            str(actualL.tiempo.accion) + \
                            """</TD>\n"""
                    else:

                        text += """<TD border="3"  bgcolor="orangered" gradientangle="315">""" + \
                            str(actualL.tiempo.accion) + \
                            """</TD>\n"""

                    actualL = actualL.siguiente

            # Si no se da ninguno de los csos anteriores entonces secagrega una contenido_m con el TD
            else:
                text += """<TD border="3"  bgcolor="orangered" gradientangle="315">""" + \
                    str(actual.contenido_m.dron)+"""</TD>\n"""

            actual = actual.siguiente

        # al fiunalizar el while se cierra la tablas
        text += """
</TR></TABLE>>];
}
"""
        return text
