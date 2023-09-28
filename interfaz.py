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
from main import cargar_archivo, imprimir_nombres_sistemas_drones, generar_grafica_original
from sistema_drones import sistema_drones


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
        self.lista = sistema_drones

        # encabezado de cuadro de texto de entrada
        Label(self.Frame, text="Sistema de drones", font=(
            "Roboto Mono", 18), fg="white",
            bg="#343541", width=30, justify="left", anchor="w").place(x=0, y=0)

        # menu archivo
        self.menubar = Menu(self.pp)

        # === Menu inicializacion ===
        analizarMenu = Menu(self.menubar, tearoff=0)

        analizarMenu .add_command(
            label="Inicilización", command=self.analizar, font=("Roboto Mono", 13))

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
            label="Generar XML", command=self.analizar, font=("Roboto Mono", 13))

        self.menubar.add_cascade(
            label="Generar XML", menu=analizarMenu, font=("Roboto Mono", 13))

        # === Opciones de gestion de drones ===
        archivoMenu = Menu(self.menubar, tearoff=0)

        archivoMenu .add_command(
            label="Ver listado de drones", command=self.analizar, font=("Roboto Mono", 13))
        archivoMenu .add_command(
            label="Agregar nuevo dron", command=self.cargarArchivo, font=("Roboto Mono", 13))

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
            label="Listado de mensajes", command=self.analizar, font=("Roboto Mono", 13))
        archivoMenu .add_command(
            label="Instrucciones para enviar un mensaje", command=self.cargarArchivo, font=("Roboto Mono", 13))

        self.menubar.add_cascade(
            label="Gestión de mensajes", menu=archivoMenu, font=("Roboto Mono", 13))

        # === Menu inicializacion ===
        analizarMenu = Menu(self.menubar, tearoff=0)

        analizarMenu .add_command(
            label="Ayuda", command=self.analizar, font=("Roboto Mono", 13))

        self.menubar.add_cascade(
            label="Ayuda", menu=analizarMenu, font=("Roboto Mono", 13))

        # confiuracion del menubar

        self.pp.config(menu=self.menubar)

        # cuadro entrada de datos

        self.ingresoDato = StringVar()

        self.ingresoDato_entry = Entry(
            textvariable=self.ingresoDato, width=24, font=("Times New Roman", 14))

        # posicionamiento del cuadro de entrada
        self.ingresoDato_entry.place(x=30, y=200)

        # Botón para guardar el texto que ingreso el usuario
        self.botonGuardar = Button(
            self.pp, text="Guardar", command=self.guardar_dato, width="10", height="3", bg="white")

        self.botonGuardar.place(x=105, y=230)

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

    def guardar_dato(self):
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

            print(signal_a_graficar)

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

    def cargarArchivo(self):

        try:
            self.lista = cargar_archivo()
            self.analizado = False

        except:
            messagebox.showerror(
                "Error", "Archivo no soportado")
            return

    def graficar(self):

        try:
            # Elimina contenido del cuadro
            self.text.delete(1.0, "end")

            n = imprimir_nombres_sistemas_drones(self.lista)

            # set contenido
            self.text.insert(1.0, n)

        except:
            messagebox.showerror(
                "Error", "No se ha podido generar la grafica")
            return

    def guardar(self):
        try:
            # Tomar datos que esta en el cuadro de texto
            self.texto = self.text.get(1.0, "end")

            archivo = open(self.archivo_seleccionado, 'w', encoding="utf-8")
            archivo.write(self.texto)

            # mensaje de guardado
            messagebox.showinfo("Guardado", "Archivo guardado con exito")

        except:
            messagebox.showerror(
                "Error", "No se ha seleccionado ningún archivo")
            return

    def guardarComo(self):
        try:
            # Tomar datos que esta en el cuadro de texto
            self.texto = self.text.get(1.0, "end")

            self.extensions = [("Archivos txt", f".txt"),
                               ("Archivos lfp", f".lfp"), ("All files", "*")]

            self.archivo_seleccionado = filename = asksaveasfilename(
                title="Seleccione un archivo", filetypes=[("Archivos txt", f".txt"), ("Archivos lfp", f".lfp"), ("All files", "*")], defaultextension=self.extensions, initialfile="Documento")

            archivo = open(self.archivo_seleccionado, 'w', encoding="utf-8")
            archivo.write(self.texto)

            # mensaje de guardado
            messagebox.showinfo("Guardado", "Archivo guardado con exito")

        except:
            messagebox.showerror(
                "Error", "No se ha seleccionado ningún archivo")
            return

    def getErrores(self):
        # Solo generamos los errores si ya se ha presionado el boton de analizar, porque si se presiona guardar sin analizar no se generan errores
        if (self.analizado == False):
            messagebox.showerror(
                "Error", "Para generar el archivo de errores primero debe de analizar el archivo")
            return
        # try:
        #     CrearArchivoErrores()
        #     # mensaje de guardado
        #     messagebox.showinfo(
        #         "Guardado", "Archivo de errores generado con exito")
        # except:
        #     messagebox.showerror(
        #         "Error", "No se ha podido generar el archivo de errores")
        #     return

    def analizar(self):
        # variable para saber si ya se presiono el boton de analizar
        self.analizado = True
        # En caso de que despues de analizar un arhivo se analice otro se limpian las listas
        # limpiarListaErrores()
        # limpiarLista()

        try:
            messagebox.showerror("Analisis completado", "Analisis completado")
            # limpiarListas()

            # instruccion(self.texto)
            # asignarToken()
            # analizador_sintactico(lista_lexemas)

            # # print(len(lista_errores))

            # if len(lista_errores) == 0:

            #     necesarioparaMongo(lista_lexemas)
            #     transformarMongo()
            #     # set contenido
            #     messagebox.showinfo("Analisis completado",
            #                         "Analisis completado, No se encontraron errores")

            #     # Elimina contenido del cuadro
            #     self.text2.delete(1.0, "end")

            #     # set contenido
            #     self.text2.insert(1.0, armarInstrucciones())

            #     generarArchivo(str(self.filename))

            # else:

            #     messagebox.showerror("Analisis completado",
            #                          "Analisis completado, Se encontraron algunos errores")

            #     # Elimina contenido del cuadro
            #     self.text2.delete(1.0, "end")

            #     # set contenido
            #     self.text2.insert(
            #         1.0, "Corrija los errores para poder traducir los comandos a MongoDB")

        except:
            messagebox.showerror(
                "Error", "No se ha seleccionado ningún archivo")
            return

    def tokens(self):

        ventana = Tk()
        ventana.title("Tokens | Proyecto 2")
        self.centrar(ventana, 800, 320)
        ventana.geometry("800x320")
        ventana.configure(bg="#343541")

        tv = ttk.Treeview(ventana, columns=("col1", "col2", "col3"))

        tv.column("#0", width=100, anchor=CENTER)
        tv.column("#1", width=200, anchor=CENTER)
        tv.column("#2", width=200, anchor=CENTER)
        tv.column("#3", width=200, anchor=CENTER)

        tv.heading("#0", text="No.", anchor=CENTER)
        tv.heading("#1", text="Token", anchor=CENTER)
        tv.heading("#2", text="No.Token", anchor=CENTER)
        tv.heading("#3", text="Lexema", anchor=CENTER)

        # Estilos de la tabla
        style = ttk.Style(tv)
        style.theme_use("clam")

        style.configure("Treeview", background="white",
                        fieldbackground="white", foreground="black", font=['Times New Roman', 14, 'normal'])

        style.configure('Treeview.Heading', background="orange", font=[
                        'Times New Roman', 14, 'normal'])

        # for i in range(len(lista_lexemas)):
        #     tv.insert("", END, text=i, values=(
        #         lista_lexemas[i].getToken(), i, lista_lexemas[i].operar(None)))

        tv.pack()

        ventana.mainloop()

    def errores(self):

        ventana = Tk()
        ventana.title("Tokens | Proyecto 2")
        self.centrar(ventana, 1100, 320)
        ventana.geometry("1100x320")
        ventana.configure(bg="#343541")

        tv = ttk.Treeview(ventana, columns=("col1", "col2", "col3", "col4"))

        tv.column("#0", width=150, anchor=CENTER)
        tv.column("#1", width=100, anchor=CENTER)
        tv.column("#2", width=100, anchor=CENTER)
        tv.column("#3", width=250, anchor=CENTER)
        tv.column("#4", width=500, anchor=CENTER)

        tv.heading("#0", text="Tipo", anchor=CENTER)
        tv.heading("#1", text="Fila", anchor=CENTER)
        tv.heading("#2", text="Columna", anchor=CENTER)
        tv.heading("#3", text="Token o Lexema", anchor=CENTER)
        tv.heading("#4", text="Descripcion", anchor=CENTER)

        # Estilos de la tabla
        style = ttk.Style(tv)
        style.theme_use("clam")

        style.configure("Treeview", background="white",
                        fieldbackground="white", foreground="black", font=['Times New Roman', 14, 'normal'])

        style.configure('Treeview.Heading', background="orange", font=[
                        'Times New Roman', 14, 'normal'])

        # for i in range(len(lista_errores)):
        #     tipo, fila, columna, lex, desc = lista_errores[i].operar(None)

        # tv.insert("", END, text=tipo, values=(
        #     fila, columna, lex, desc))

        tv.pack()

        ventana.mainloop()


# mostrar pantalla
r = Pantalla_principal()
