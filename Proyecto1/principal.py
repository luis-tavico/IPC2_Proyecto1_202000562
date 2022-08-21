from tkinter import Tk
from vistaInicio import Inicio
from listaEnlazadaPacientes import ListaEnlazadaPacientes

nuevaVentana = Inicio(Tk(), ListaEnlazadaPacientes())
nuevaVentana.ventana.mainloop()

#print("Cargar Archivo")