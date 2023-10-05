from fileinput import filename
from tkinter.filedialog import askopenfilename
from tkinter.tix import Tree
from tkinter import filedialog
from tkinter import Tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.filedialog import asksaveasfilename
import os
from main import cargar_archivo, imprimir_nombres_sistemas_drones, generar_grafica_original, imprimir_nombres_lista_drones, imprimir_lista_mensajes, imprimir_mensajes,  Crear_instrucciones_mensaje, generar_grafica_instrucciones_dron, encontrar_tiempo_optimo, rellenar_nodos_tiempo_optimo, descifrar_mensaje_salida
from lista_sistema_drones import lista_sistema_drones
from lista_drones import lista_drones
from dron import dron
from lista_mensaje import lista_mensaje
from lista_contenido_m import lista_contenido_m
from lista_drones_salida import lista_drones_salida


class Pantalla_principal():

    def __init__(self):
        self.pp = Tk()
        self.pp.title("Pantalla Principal | Proyecto 2")
        self.centrar(self.pp, 1000, 700)
        self.pp.configure(bg="#343541")
        self.pantalla_1()

    def centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        anchura_pantalla = r.winfo_screenwidth()
        x = (anchura_pantalla//2)-(ancho//2)
        y = (altura_pantalla//2)-(alto//2)
        r.geometry(f"+{x}+{y}")

    def pantalla_1(self):
        self.Frame = Frame(height=630, width=1000)
        self.Frame.config(bg="#343541")
        self.Frame.pack(padx=25, pady=25)
        self.text = ''
        posicionx1 = 480
        self.analizado = False
        self.botonGraficaContenido = False
        self.botonNuevoDron = False
        self.botonMensaje = False
        self.lista = lista_sistema_drones()
        self.lista_drones = lista_drones()
        self.lista_mensajes = lista_mensaje()
        self.lista_contenido_m = lista_contenido_m()
        self.drones_salidaM = lista_drones_salida()

        # encabezado de cuadro de texto de entrada
        Label(self.Frame, text="Sistema de drones", font=(
            "Roboto Mono", 18), fg="white",
            bg="#343541", width=30, justify="left", anchor="w").place(x=0, y=0)

        # menu archivo
        self.menubar = Menu(self.pp)

        # === Menu inicializacion ===
        analizarMenu = Menu(self.menubar, tearoff=0)

        analizarMenu .add_command(
            label="Inicilización", command=self.inicializar, font=("Roboto Mono", 13))

        self.menubar.add_cascade(
            label="Inicilización", menu=analizarMenu, font=("Roboto Mono", 13))

        # === Menu inicializacion ===
        analizarMenu = Menu(self.menubar, tearoff=0)

        analizarMenu .add_command(
            label="Cargar XML", command=self.cargarArchivo, font=("Roboto Mono", 13))

        self.menubar.add_cascade(
            label="Cargar XML", menu=analizarMenu, font=("Roboto Mono", 13))

        # === Menu inicializacion ===
        analizarMenu = Menu(self.menubar, tearoff=0)

        analizarMenu .add_command(
            label="Generar XML de salida", command=self.generar_archivo_salida, font=("Roboto Mono", 13))

        self.menubar.add_cascade(
            label="Generar XML salida", menu=analizarMenu, font=("Roboto Mono", 13))

        # === Opciones de gestion de drones ===
        archivoMenu = Menu(self.menubar, tearoff=0)

        archivoMenu .add_command(
            label="Ver listado de drones", command=self.ver_listado_de_drones, font=("Roboto Mono", 13))
        archivoMenu .add_command(
            label="Agregar nuevo dron", command=self.agregar_nuevo_dron, font=("Roboto Mono", 13))

        self.menubar.add_cascade(
            label="Gestión de drones", menu=archivoMenu, font=("Roboto Mono", 13))

        # === Gestión sistema de drones ===

        analizarMenu = Menu(self.menubar, tearoff=0)

        analizarMenu .add_command(
            label="Graficar listado sitema de drones", command=self.graficar, font=("Roboto Mono", 13))

        self.menubar.add_cascade(
            label="Gestión sistemas de drones", menu=analizarMenu, font=("Roboto Mono", 13))

        # === Gestión de mensajes ===
        archivoMenu = Menu(self.menubar, tearoff=0)

        archivoMenu .add_command(
            label="Listado de mensajes", command=self.listado_mensajes, font=("Roboto Mono", 13))
        archivoMenu .add_command(
            label="Instrucciones para enviar un mensaje", command=self.instrucciones_para_enviar_un_mensaje, font=("Roboto Mono", 13))

        self.menubar.add_cascade(
            label="Gestión de mensajes", menu=archivoMenu, font=("Roboto Mono", 13))

        # === Menu inicializacion ===
        analizarMenu = Menu(self.menubar, tearoff=0)

        analizarMenu .add_command(
            label="Ayuda", command=self.ayuda, font=("Roboto Mono", 13))

        self.menubar.add_cascade(
            label="Ayuda", menu=analizarMenu, font=("Roboto Mono", 13))

        # confiuracion del menubar

        self.pp.config(menu=self.menubar)

        # cuadro entrada de datos

        self.ingresoDato = StringVar()

        self.ingresoDato_entry = Entry(
            textvariable=self.ingresoDato, width=39, font=("Times New Roman", 14))

        # posicionamiento del cuadro de entrada
        self.ingresoDato_entry.place(x=140, y=390)

        # Botón para guardar el texto que ingreso el usuario
        self.botonGuardar = Button(
            self.pp, text="Aceptar", command=self.guardar_dato, width="10", height="3", bg="white")

        self.botonGuardar.place(x=275, y=420)

        # cuadro de texto
        self.textContainer = Frame(self.pp, borderwidth=1, relief="sunken")

        self.text = Text(self.textContainer, font=(
            "Times New Roman", 15), fg='white', bg="#444654", width=57, height=14, wrap="none")

        textVsb = Scrollbar(
            self.textContainer, orient="vertical", command=self.text.yview)
        textHsb = Scrollbar(
            self.textContainer, orient="horizontal", command=self.text.xview)
        self.text.configure(yscrollcommand=textVsb.set,
                            xscrollcommand=textHsb.set)

        self.text.grid(row=0, column=0, sticky="nsew")
        textVsb.grid(row=0, column=1, sticky="ns")
        textHsb.grid(row=1, column=0, sticky="ew")

        self.textContainer.grid_rowconfigure(0, weight=1)
        self.textContainer.grid_columnconfigure(0, weight=1)

        self.textContainer.place(x=30, y=55)

        # Actualizacion del Frame
        self.Frame.mainloop()

    def inicializar(self):

        try:
            self.analizado = False
            self.botonGraficaContenido = False
            self.botonNuevoDron = False
            self.botonMensaje = False

            # Limpieza de listas
            self.lista = lista_sistema_drones()
            self.lista_drones = lista_drones()
            self.lista_mensajes = lista_mensaje()
            self.drones_salidaM = lista_drones_salida()

            messagebox.showinfo(
                "Inicialización", "Sistema inicializado con exito")

            # Elimina contenido del cuadro
            self.text.delete(1.0, "end")

        except:
            messagebox.showerror(
                "Error", "No se ha podido inicializar el sistema de drones")
            return

    def guardar_dato(self):

        if self.botonGraficaContenido == True:

            try:
                numero_signal = self.ingresoDato.get().strip()

                # Luego de guardar el dato se grafica

                # === convertir el numero seleccionado a el nombre de la señal ===
                actual = self.lista.primero
                contadorAux = 0
                signal_a_graficar = ""
                while actual != None:
                    contadorAux += 1
                    if numero_signal == str(contadorAux):
                        signal_a_graficar = actual.sistema_drones.nombre
                        # lista_sistema_temporal.calcular_los_patrones(str(actual.sistema_drones.nombre))
                    actual = actual.siguiente

                # El usuario selecciona donde guardar la grafica
                direccion_grafica = filedialog.asksaveasfilename(
                    filetypes=[("Archivos de texto", "*.dot"),
                               ("Todos los archivos", "*.*")],
                    title="Guardar archivo como", initialfile="Matriz")

                generar_grafica_original(
                    signal_a_graficar, self.lista, direccion_grafica)

                self.botonGraficaContenido = False

                messagebox.showinfo(
                    "Grafica", "Grafica generada con exito")

            except:
                messagebox.showerror(
                    "Error", "No se ha seleccionado ningún archivo")
                return

        elif self.botonNuevoDron == True:

            try:
                nombre_dron = self.ingresoDato.get().strip()

                # Se comprueba que el nombre del dron no exista
                dronYaExiste = False
                actual = self.lista_drones.primero
                while actual != None:
                    if actual.dron.nombre == nombre_dron:
                        messagebox.showerror(
                            "Error", "El nombre del dron ya existe")
                        dronYaExiste = True
                    actual = actual.siguiente

                if dronYaExiste == False:
                    # Se crea el objeto dron
                    nuevo_dron = dron(nombre_dron)
                    # Se inserta el dron en la lista de drones
                    self.lista_drones.insertar_dato_ordenado(nuevo_dron)
                    messagebox.showinfo(
                        "Nuevo dron", "Nuevo Dron agregado con exito")

                # self.lista_drones.recorrer_e_imprimir_lista()
                self.botonNuevoDron = False

            except:
                messagebox.showerror(
                    "Error", "No se ha podido agregar el nuevo dron")
                return

        elif self.botonMensaje == True:

            try:
                nombre_mensaje = self.ingresoDato.get().strip()

                # === convertir el numero seleccionado a el nombre del mensaje ===
                actual = self.lista_mensajes.primero
                contadorAux = 0
                mensaje_select = ""
                while actual != None:
                    contadorAux += 1
                    if nombre_mensaje == str(contadorAux):
                        mensaje_select = actual.mensaje.sistemaDrones
                        nombreM_select = actual.mensaje.nombre

                        lista_instrucciones_select = actual.mensaje.lista_instruccion
                        # lista_sistema_temporal.calcular_los_patrones(str(actual.sistema_drones.nombre))
                    actual = actual.siguiente

                # El usuario selecciona donde guardar la grafica
                direccion_grafica2 = filedialog.asksaveasfilename(
                    filetypes=[("Archivos de texto", "*.dot"),
                               ("Todos los archivos", "*.*")],
                    title="Guardar archivo como", initialfile="Mensaje")

                # Se genera la grafica
                generar_grafica_instrucciones_dron(
                    nombreM_select, self.drones_salidaM, direccion_grafica2)

                self.botonMensaje = False

                messagebox.showinfo(
                    "Grafica", "Grafica de instrucciones generada con exito")

            except:
                messagebox.showerror(
                    "Error", "No se ha seleccionado ningún archivo")
                return

        else:
            messagebox.showerror(
                "Error", "No se ha podio realizar la acción")
            return

    def cargarArchivo(self):

        try:
            cargar_archivo(self.lista_drones, self.lista, self.lista_mensajes)

            self.analizado = True

            # Solo despues de caragar un archivo se desigran los mensajes, y se crean la lista de instrucciones
            self.drones_salidaM = lista_drones_salida()

            descifrar_mensaje_salida(
                self.lista_mensajes, self.drones_salidaM, self.lista)

            messagebox.showinfo(
                "Carga de archivo", "Archivo cargado con exito")
            # Elimina contenido del cuadro
            self.text.delete(1.0, "end")

        except:
            messagebox.showerror(
                "Error", "Archivo no soportado")
            return

    def graficar(self):

        if self.analizado == True:

            try:
                # si se presiono antes el boton de nuevo dron se desactiva
                self.botonNuevoDron = False
                self.botonMensaje = False

                # Elimina contenido del cuadro
                self.text.delete(1.0, "end")

                n = imprimir_nombres_sistemas_drones(self.lista)

                # set contenido
                self.text.insert(1.0, n)
                self.botonGraficaContenido = True

            except:
                messagebox.showerror(
                    "Error", "No se ha podido generar la grafica")
                return

        else:

            messagebox.showerror(
                "Error", "No se ha cargado ningun archivo")
            return

    def ver_listado_de_drones(self):

        if self.analizado == True:

            try:
                # Elimina contenido del cuadro
                self.text.delete(1.0, "end")

                n = imprimir_nombres_lista_drones(self.lista_drones)

                # set contenido
                self.text.insert(1.0, n)

            except:
                messagebox.showerror(
                    "Error", "No se ha podido mostrar la lista de drones")
                return

        else:

            messagebox.showerror(
                "Error", "No se ha cargado ningun archivo")
            return

    def agregar_nuevo_dron(self):

        if self.analizado == True:

            try:
                # si se presiono antes el boton de graficar contenido se desactiva
                self.botonGraficaContenido = False
                self.botonMensaje = False

                self.botonNuevoDron = True
                # Elimina contenido del cuadro
                self.text.delete(1.0, "end")

                # set contenido
                self.text.insert(1.0, "Ingrese el nombre del nuevo dron \n")

            except:
                messagebox.showerror(
                    "Error", "No se ha podido agregar el nuevo dron")
                return

        else:

            messagebox.showerror(
                "Error", "No se ha cargado ningun archivo")
            return

    def listado_mensajes(self):

        if self.analizado == True:

            try:
                # Elimina contenido del cuadro
                self.text.delete(1.0, "end")

                m = imprimir_lista_mensajes(self.lista_mensajes)

                # set contenido
                self.text.insert(1.0, m)

            except:
                messagebox.showerror(
                    "Error", "No se ha podido mostrar el listado de mensajes")
                return

        else:

            messagebox.showerror(
                "Error", "No se ha cargado ningun archivo")
            return

    def instrucciones_para_enviar_un_mensaje(self):

        if self.analizado == True:

            try:
                # si se presiono antes el boton de graficar contenido se desactiva
                self.botonGraficaContenido = False
                self.botonNuevoDron = False

                self.botonMensaje = True

                # Elimina contenido del cuadro
                self.text.delete(1.0, "end")

                l = imprimir_mensajes(
                    self.drones_salidaM)

                # set contenido
                self.text.insert(1.0, l)

            except:
                messagebox.showerror(
                    "Error", "No se ha podido mostrar el listado de mensajes")
                return

        else:

            messagebox.showerror(
                "Error", "No se ha cargado ningun archivo")
            return

    def generar_archivo_salida(self):

        if self.analizado == True:

            try:

                # El usuario selecciona donde guardar la grafica
                direccion_salida = filedialog.asksaveasfilename(defaultextension=".xml",
                                                                filetypes=[
                                                                    ("Archivos de texto", "*.xml"), ("Todos los archivos", "*.*")],
                                                                title="Guardar archivo como", initialfile="Salida")

                self.drones_salidaM.generar_xml_salida(direccion_salida)

                messagebox.showinfo(
                    "Archvio de salida", "Archivo xml de salida generado con exito")

            except:
                messagebox.showerror(
                    "Error", "No se ha podido generar el archivo de salida")
                return

        else:

            messagebox.showerror(
                "Error", "No se ha cargado ningun archivo")
            return

    def ayuda(self):

        # Elimina contenido del cuadro
        self.text.delete(1.0, "end")

        # Datos del estudiante
        datosDelEstudiante = """
Datos del estudiante:
Nombre: Elian Angel Fernando Reyes Yac
Carnet: 202044192

Documentación:
https://github.com/KINGR0X/IPC2_Proyecto2_202044192/tree/main/Documentacion
"""
        # set contenido
        self.text.insert(1.0, datosDelEstudiante)


# mostrar pantalla
r = Pantalla_principal()
