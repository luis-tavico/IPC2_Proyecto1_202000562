from tkinter import W, Button, Frame, Label, PhotoImage, Toplevel, filedialog, messagebox, CENTER
from leerPaciente import LeerPaciente
from cargarArchivo import CargarArchivo

class Inicio:

    def __init__(self, ventana, listaPacientes):
        self.listaPacientes = listaPacientes
        self.ventana = ventana
        ventanaAncho, ventanaAlto = 362,140
        pantallaAncho = self.ventana.winfo_screenwidth()
        pantallaAlto = self.ventana.winfo_screenheight()
        posicionX = int(pantallaAncho/2 - ventanaAncho/2)
        posicionY = int(pantallaAlto/2 - ventanaAlto/2)
        self.ventana.geometry(f'{ventanaAncho}x{ventanaAlto}+{posicionX}+{posicionY}')
        self.ventana.title("VirusApp")
        self.ventana.resizable(False, False)
        #self.ventana.protocol("WM_DELETE_WINDOW", self.salir)
        #self.ventana.iconbitmap(bitmap = "./imagenes/icono.ico")
        '''self.cargar = PhotoImage(file="/imagenes/folderC.png")
        self.leer = PhotoImage(file="/imagenes/id-card.png")
        self.generar = PhotoImage(file="/imagenes/folder.png")'''
        #self.ventana.iconbitmap(bitmap = "./imagenes/icono.ico")
        '''self.cargar = PhotoImage(file="folderC.png")
        self.leer = PhotoImage(file="id-card.png")
        self.generar = PhotoImage(file="folder.png")'''
        self.iniciarComponentes()
        

    def iniciarComponentes(self):
        self.agregarPanel()
        self.agregarEtiquetas()
        self.agregarBotones()

    def agregarPanel(self):
        self.panel = Frame(self.ventana)
        self.panel.config(bg="white")
        self.panel.pack(fill="both", expand="true")
    
    '''image=self.cargar'''

    def agregarBotones(self):
        self.botonCargarArchivos = Button(self.panel, bg="#154360", activebackground="#1F618D", cursor="hand2", bd=0, command=self.cargarArchivo)
        self.botonCargarArchivos.place(x=0, y=0, width=120, height=120)
        self.botonCargarArchivos.bind("<Enter>", self.cursorSobreBotonCargar)
        self.botonCargarArchivos.bind("<Leave>", self.cursorFueraBotonCargar)
        self.botonLeerPaciente = Button(self.panel, bg="#154360", activebackground="#1F618D",  cursor="hand2", bd=0, command=self.leerPaciente)
        self.botonLeerPaciente.place(x=121, y=0, width=120, height=120)
        self.botonLeerPaciente.bind("<Enter>", self.cursorSobreBotonLeer)
        self.botonLeerPaciente.bind("<Leave>", self.cursorFueraBotonLeer)
        self.botonGenerarArchivo = Button(self.panel, bg="#154360",  activebackground="#1F618D",  cursor="hand2", bd=0, command=self.generarArchivo)
        self.botonGenerarArchivo.place(x=242, y=0, width=120, height=120)
        self.botonGenerarArchivo.bind("<Enter>", self.cursorSobreBotonGenerar)
        self.botonGenerarArchivo.bind("<Leave>", self.cursorFueraBotonGenerar)

    def agregarEtiquetas(self):
        self.etiquetaInfo = Label(self.panel, font=("Segoe UI", 11, "normal"), bg="white", anchor=CENTER)
        self.etiquetaInfo.place(x=0, y=120, width=362, height=20)

    ############FUNCIONES PARA ESTILO BOTONES################
    def cursorSobreBotonCargar(self, e):
        self.botonCargarArchivos["bg"] = "red"
        self.etiquetaInfo.config(text="Cargar Archivo")

    def cursorSobreBotonLeer(self, e):
        self.botonLeerPaciente["bg"] = "red"
        self.etiquetaInfo.config(text="Leer Paciente")

    def cursorSobreBotonGenerar(self, e):
        self.botonGenerarArchivo["bg"] = "red"
        self.etiquetaInfo.config(text="Generar Archivo")

    def cursorFueraBotonCargar(self, e):
        self.botonCargarArchivos["bg"] = "#154360"
        self.etiquetaInfo.config(text="")

    def cursorFueraBotonLeer(self, e):
        self.botonLeerPaciente["bg"] = "#154360"
        self.etiquetaInfo.config(text="")

    def cursorFueraBotonGenerar(self, e):
        self.botonGenerarArchivo["bg"] = "#154360"
        self.etiquetaInfo.config(text="")
    ################################################33

    def cargarArchivo(self):
        ruta = filedialog.askopenfilename(title="Abrir")
        if ruta != "":
            #try:
            CargarArchivo(ruta, self.listaPacientes)
                #messagebox.showinfo("Informacion", "¡Archivo leido exitosamente!")
            #except:
                #messagebox.showerror("Error", "¡Ocurrio un error al leer el archivo!\nPuede que algunos datos no se \ncargaron correctamente.")
            #messagebox.showwarning("Advertencia", "¡Complete el campo vacio!")
 
        #self.ventana.withdraw()
        #nuevaVentana = SeleccionarArchivo(Toplevel(), self.db, self.ventana)
        #nuevaVentana.ventana.focus_force()
        #nuevaVentana.ventana.mainloop()
        
    def leerPaciente(self):
        self.ventana.destroy() 
        LeerPaciente(self.ventana, self.listaPacientes)

    def generarArchivo(self):
        print()
        
    def salir(self):
        respuesta = messagebox.askyesno("Confirmacion", "¿Seguro que desea salir?", default="no")
        if respuesta: self.ventana.destroy()
    