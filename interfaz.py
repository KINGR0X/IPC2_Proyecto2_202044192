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
from main import cargar_archivo, imprimir_nombres_sistemas_drones, generar_grafica_original, imprimir_nombres_lista_drones
from sistema_drones import sistema_drones
from lista_drones import lista_drones


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
        self.lista = sistema_drones
        self.lista_drones = lista_drones

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
            label="Generar XML", command=self.ver_listado_de_drones, font=("Roboto Mono", 13))

        self.menubar.add_cascade(
            label="Generar XML", menu=analizarMenu, font=("Roboto Mono", 13))

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
            label="Grafica listado sitema de drones", command=self.graficar, font=("Roboto Mono", 13))

        self.menubar.add_cascade(
            label="Gestión sistema de drones", menu=analizarMenu, font=("Roboto Mono", 13))

        # === Gestión de mensajes ===
        archivoMenu = Menu(self.menubar, tearoff=0)

        archivoMenu .add_command(
            label="Listado de mensajes", command=self.ver_listado_de_drones, font=("Roboto Mono", 13))
        archivoMenu .add_command(
            label="Instrucciones para enviar un mensaje", command=self.cargarArchivo, font=("Roboto Mono", 13))

        self.menubar.add_cascade(
            label="Gestión de mensajes", menu=archivoMenu, font=("Roboto Mono", 13))

        # === Menu inicializacion ===
        analizarMenu = Menu(self.menubar, tearoff=0)

        analizarMenu .add_command(
            label="Ayuda", command=self.ver_listado_de_drones, font=("Roboto Mono", 13))

        self.menubar.add_cascade(
            label="Ayuda", menu=analizarMenu, font=("Roboto Mono", 13))

        # confiuracion del menubar

        self.pp.config(menu=self.menubar)

        # cuadro entrada de datos

        self.ingresoDato = StringVar()

        self.ingresoDato_entry = Entry(
            textvariable=self.ingresoDato, width=39, font=("Times New Roman", 14))

        # posicionamiento del cuadro de entrada
        self.ingresoDato_entry.place(x=30, y=192)

        # Botón para guardar el texto que ingreso el usuario
        self.botonGuardar = Button(
            self.pp, text="Guardar", command=self.guardar_dato, width="10", height="3", bg="white")

        self.botonGuardar.place(x=170, y=228)

        # cuadro de texto
        self.textContainer = Frame(self.pp, borderwidth=1, relief="sunken")

        self.text = Text(self.textContainer, font=(
            "Times New Roman", 15), fg='white', bg="#444654", width=33, height=5, wrap="none")

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

        self.textContainer.place(x=30, y=52)

        # Actualizacion del Frame
        self.Frame.mainloop()

    def inicializar(self):

        try:
            self.analizado = False
            self.botonGraficaContenido = False

            messagebox.showinfo(
                "Inicialización", "Sistema inicializado con exito")

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

                messagebox.showinfo(
                    "Grafica", "Grafica generada con exito")

            except:
                messagebox.showerror(
                    "Error", "No se ha seleccionado ningún archivo")
                return

        else:
            messagebox.showerror(
                "Error", "No se ha presionado el boton de graficar sistema de datos")
            return

    def cargarArchivo(self):

        try:
            self.lista, self.lista_drones = cargar_archivo()
            self.analizado = True

        except:
            messagebox.showerror(
                "Error", "Archivo no soportado")
            return

    def graficar(self):

        if self.analizado == True:

            try:
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
        pass


# mostrar pantalla
r = Pantalla_principal()
