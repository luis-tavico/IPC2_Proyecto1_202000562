from tkinter import W, Button, Frame, Label, PhotoImage, Tk, filedialog, messagebox, CENTER
from cargarArchivo import CargarArchivo

class Inicio:

    def __init__(self, ventana):
        self.ventana = ventana
        ventanaAncho, ventanaAlto = 362,262
        pantallaAncho = self.ventana.winfo_screenwidth()
        pantallaAlto = self.ventana.winfo_screenheight()
        posicionX = int(pantallaAncho/2 - ventanaAncho/2)
        posicionY = int(pantallaAlto/2 - ventanaAlto/2)
        self.ventana.geometry(f'{ventanaAncho}x{ventanaAlto}+{posicionX}+{posicionY}')
        self.ventana.title("VirusApp")
        self.ventana.resizable(False, False)
        #self.ventana.protocol("WM_DELETE_WINDOW", self.salir)
        #self.ventana.iconbitmap(bitmap = "./imagenes/icono.ico")
        self.cargar = PhotoImage(file="imagenes/folderC.png")
        self.agregar = PhotoImage(file="imagenes/verified.png")
        self.editar = PhotoImage(file="imagenes/edit.png")
        self.eliminar = PhotoImage(file="imagenes/delete.png")
        self.leer = PhotoImage(file="imagenes/id-card.png")
        self.generar = PhotoImage(file="imagenes/folder.png")
        self.iniciarComponentes()
        

    def iniciarComponentes(self):
        self.agregarPanel()
        self.agregarEtiquetas()
        self.agregarBotones()

    def agregarPanel(self):
        self.panel = Frame(self.ventana)
        self.panel.config(bg="white")
        self.panel.pack(fill="both", expand="true")

    def agregarBotones(self):
        self.botonCargarArchivos = Button(self.panel, image=self.cargar, bg="#154360", activebackground="#1F618D", cursor="hand2", bd=0, command=self.cargarArchivo)
        self.botonCargarArchivos.place(x=0, y=0, width=120, height=120)
        self.botonCargarArchivos.bind("<Enter>", self.cursorSobreBotonCargar)
        self.botonCargarArchivos.bind("<Leave>", self.cursorFueraBotonCargar)
        self.botonAgregarPaciente = Button(self.panel, image=self.agregar, bg="#154360",  activebackground="#1F618D",  cursor="hand2", bd=0, command=self.gestionarCurso)
        self.botonAgregarPaciente.place(x=121, y=0, width=120, height=120)
        self.botonAgregarPaciente.bind("<Enter>", self.cursorSobreBotonAgregar)
        self.botonAgregarPaciente.bind("<Leave>", self.cursorFueraBotonAgregar)
        self.botonActualizarPaciente = Button(self.panel, image=self.editar, bg="#154360",  activebackground="#1F618D",  cursor="hand2", bd=0, command=self.gestionarCurso)
        self.botonActualizarPaciente.place(x=242, y=0, width=120, height=120)
        self.botonActualizarPaciente.bind("<Enter>", self.cursorSobreBotonEditar)
        self.botonActualizarPaciente.bind("<Leave>", self.cursorFueraBotonEditar)
        self.botonEliminarPaciente = Button(self.panel, image=self.eliminar, bg="#154360", fg="white", activebackground="#1F618D",  cursor="hand2", bd=0, command=self.gestionarCurso)
        self.botonEliminarPaciente.place(x=0, y=121, width=120, height=120)
        self.botonEliminarPaciente.bind("<Enter>", self.cursorSobreBotonEliminar)
        self.botonEliminarPaciente.bind("<Leave>", self.cursorFueraBotonEliminar)
        self.botonLeerPaciente = Button(self.panel, image=self.leer, bg="#154360", activebackground="#1F618D",  cursor="hand2", bd=0, command=self.gestionarCurso)
        self.botonLeerPaciente.place(x=121, y=121, width=120, height=120)
        self.botonLeerPaciente.bind("<Enter>", self.cursorSobreBotonLeer)
        self.botonLeerPaciente.bind("<Leave>", self.cursorFueraBotonLeer)
        self.botonGenerarArchivo = Button(self.panel, image=self.generar, bg="#154360",  activebackground="#1F618D",  cursor="hand2", bd=0, command=self.gestionarCurso)
        self.botonGenerarArchivo.place(x=242, y=121, width=120, height=120)
        self.botonGenerarArchivo.bind("<Enter>", self.cursorSobreBotonGenerar)
        self.botonGenerarArchivo.bind("<Leave>", self.cursorFueraBotonGenerar)

    def agregarEtiquetas(self):
        self.etiquetaInfo = Label(self.panel, font=("Segoe UI", 11, "normal"), bg="white", anchor=CENTER)
        self.etiquetaInfo.place(x=0, y=241, width=362, height=20)

    def cursorSobreBotonCargar(self, e):
        self.botonCargarArchivos["bg"] = "red"
        self.etiquetaInfo.config(text="Cargar Archivos")

    def cursorSobreBotonAgregar(self, e):
        self.botonAgregarPaciente["bg"] = "red"
        self.etiquetaInfo.config(text="Agregar Paciente")

    def cursorSobreBotonEditar(self, e):
        self.botonActualizarPaciente["bg"] = "red"
        self.etiquetaInfo.config(text="Editar Paciente")

    def cursorSobreBotonEliminar(self, e):
        self.botonEliminarPaciente["bg"] = "red"
        self.etiquetaInfo.config(text="Eliminar Paciente")

    def cursorSobreBotonLeer(self, e):
        self.botonLeerPaciente["bg"] = "red"
        self.etiquetaInfo.config(text="Leer Paciente")

    def cursorSobreBotonGenerar(self, e):
        self.botonGenerarArchivo["bg"] = "red"
        self.etiquetaInfo.config(text="Generar Archivo")

    def cursorFueraBotonCargar(self, e):
        self.botonCargarArchivos["bg"] = "#154360"
        self.etiquetaInfo.config(text="")

    def cursorFueraBotonAgregar(self, e):
        self.botonAgregarPaciente["bg"] = "#154360"
        self.etiquetaInfo.config(text="")

    def cursorFueraBotonEditar(self, e):
        self.botonActualizarPaciente["bg"] = "#154360"
        self.etiquetaInfo.config(text="")

    def cursorFueraBotonEliminar(self, e):
        self.botonEliminarPaciente["bg"] = "#154360"
        self.etiquetaInfo.config(text="")

    def cursorFueraBotonLeer(self, e):
        self.botonLeerPaciente["bg"] = "#154360"
        self.etiquetaInfo.config(text="")

    def cursorFueraBotonGenerar(self, e):
        self.botonGenerarArchivo["bg"] = "#154360"
        self.etiquetaInfo.config(text="")

    def cargarArchivo(self):
        ruta = filedialog.askopenfilename(title="Abrir")
        if ruta != "":
            l = CargarArchivo(ruta)
            l.leerArchivo()
            messagebox.showinfo("Informacion", "Archivo leido exitosamente")
        #self.ventana.withdraw()
        #nuevaVentana = SeleccionarArchivo(Toplevel(), self.db, self.ventana)
        #nuevaVentana.ventana.focus_force()
        #nuevaVentana.ventana.mainloop()
        
    def gestionarCurso(self): 
        print()
        #self.ventana.withdraw()
        #nuevaVentana = GestionarCurso(Toplevel(), self.db, self.ventana) 
        #nuevaVentana.ventana.focus_force() 
        #nuevaVentana.ventana.mainloop()

    def salir(self):
        respuesta = messagebox.askyesno("Confirmacion", "¿Seguro que desea salir?", default="no")
        if respuesta: self.ventana.destroy()
    