import os
from modeloPeriodo import Periodo
from listaDobleEnlazadaNumeros import ListaDobleEnlazadaNumeros
import xml.etree.ElementTree as ET

class Paciente:

    def __init__(self, paciente, info):
        self.info = info
        self.paciente = paciente

    def ejecutar(self):
        listaPeriodos = self.paciente.getListaPeriodos()
        periodos = listaPeriodos.valores()
        periodoInicial = periodos.periodo
        valoresColumnaInicial = periodoInicial.posicionX
        valoresFilaInicial = periodoInicial.posicionY
        col = valoresColumnaInicial
        fil = valoresFilaInicial
        valorX = valoresColumnaInicial.valores()
        valorY = valoresFilaInicial.valores()
        tamañoRejilla = self.paciente.getTamañoRejilla()
        msj = ("¡No se obtuvo ningun resultado!")
    
        for i in range(self.paciente.getPeriodos()):
            nPeriodo = i+1 
            columnas = ListaDobleEnlazadaNumeros()
            filas = ListaDobleEnlazadaNumeros()
            posiciones = ListaDobleEnlazadaNumeros()

            #Verifica si el periodo a crear ya existe
            if (listaPeriodos.buscarPeriodo(nPeriodo)):      
                listaPeriodos.insertar(Periodo(nPeriodo, columnas, filas, posiciones))
                
                #Encontrar las celdas infectas que se mantendran igual
                while valorX != None and valorY != None:
                    celdasInfectadas = 0
                    valY = fil.valores()
                    valX = col.valores()
                    while valX != None:
                        #X
                        if (valorX.numero - 1 == valX.numero) and (valorY.numero == valY.numero):
                            celdasInfectadas += 1
                        if (valorX.numero + 1 == valX.numero) and (valorY.numero == valY.numero):
                            celdasInfectadas += 1
                        #Y
                        if (valorX.numero == valX.numero) and (valorY.numero - 1 == valY.numero):
                            celdasInfectadas += 1
                        if (valorX.numero == valX.numero) and (valorY.numero + 1 == valY.numero):
                            celdasInfectadas += 1
                        #X, Y por cada esquina
                        if (valorX.numero - 1 == valX.numero) and (valorY.numero - 1 == valY.numero):
                            celdasInfectadas += 1
                        if (valorX.numero - 1 == valX.numero) and (valorY.numero + 1 == valY.numero):
                            celdasInfectadas += 1
                        if (valorX.numero + 1 == valX.numero) and (valorY.numero - 1 == valY.numero):
                            celdasInfectadas += 1
                        if (valorX.numero + 1 == valX.numero) and (valorY.numero + 1 == valY.numero):
                            celdasInfectadas += 1
                        valX = valX.siguiente
                        valY = valY.siguiente
                    if celdasInfectadas == 2 or celdasInfectadas == 3:
                        if (valorX.numero > 0 and valorX.numero <= tamañoRejilla) and (valorY.numero > 0 and valorY.numero <= tamañoRejilla):
                            listaPeriodos.buscarPeriodo(nPeriodo)
                            if not(listaPeriodos.buscarCeldas(valorX.numero,valorY.numero)):
                                columnas.insertar(valorX.numero)
                                filas.insertar(valorY.numero)
                                if (valorY.numero == 1):
                                    val_x = valorX.numero
                                    val_y = valorY.numero * 0
                                else:
                                    val_x = valorX.numero
                                    val_y = (valorY.numero - 1) * tamañoRejilla
                                pos = val_x + val_y
                                posiciones.insertar(pos)
                    valorX = valorX.siguiente
                    valorY = valorY.siguiente

                #Econtrar las celdas que se infectaran
                valorY = fil.valores()
                valorX = col.valores()
                while valorX != None and valorY != None:
                    for i in range(8):
                        if i == 0:
                            x = valorX.numero - 1
                            y = valorY.numero
                        elif i == 1:
                            x = valorX.numero + 1
                            y = valorY.numero
                        elif i == 2:
                            x = valorX.numero
                            y = valorY.numero - 1
                        elif i == 3:
                            x = valorX.numero
                            y = valorY.numero + 1
                        elif i == 4:
                            x = valorX.numero - 1
                            y = valorY.numero - 1
                        elif i == 5:
                            x = valorX.numero + 1
                            y = valorY.numero - 1
                        elif i == 6:
                            x = valorX.numero + 1
                            y = valorY.numero + 1
                        elif i == 7:
                            x = valorX.numero - 1
                            y = valorY.numero + 1
                        celdasInfectadas = 0
                        valY = fil.valores()
                        valX = col.valores()
                        while valX != None:
                            #X
                            if (x - 1 == valX.numero) and (y == valY.numero):
                                celdasInfectadas += 1
                            if (x + 1 == valX.numero) and (y == valY.numero):
                                celdasInfectadas += 1
                            #Y
                            if (x == valX.numero) and (y - 1 == valY.numero):
                                celdasInfectadas += 1
                            if (x == valX.numero) and (y + 1 == valY.numero):
                                celdasInfectadas += 1
                            #X, Y por cada esquina
                            if (x - 1 == valX.numero) and (y - 1 == valY.numero):
                                celdasInfectadas += 1
                            if (x - 1 == valX.numero) and (y + 1 == valY.numero):
                                celdasInfectadas += 1
                            if (x + 1 == valX.numero) and (y - 1 == valY.numero):
                                celdasInfectadas += 1
                            if (x+ 1 == valX.numero) and (y + 1 == valY.numero):
                                celdasInfectadas += 1
                            valX = valX.siguiente
                            valY = valY.siguiente
                        if celdasInfectadas == 3:
                            if (x > 0 and x <= tamañoRejilla) and (y > 0 and y <= tamañoRejilla):
                                listaPeriodos.buscarPeriodo(nPeriodo)
                                if not(listaPeriodos.buscarCeldas(x,y)):                 
                                    columnas.insertar(x)
                                    filas.insertar(y)
                                    if (y == 1):
                                        val_x = x
                                        val_y = y * 0
                                    else:
                                        val_x = x
                                        val_y = (y - 1) * tamañoRejilla
                                    pos = val_x + val_y
                                    posiciones.insertar(pos)
                    valorX = valorX.siguiente
                    valorY = valorY.siguiente

                #Buscar periodo actual
                listaPeriodos.buscarPeriodo(nPeriodo)
                listaPeriodos.generarPatron()

            #Asignar valores 
            periodos = periodos.siguiente
            col = periodos.periodo.posicionX
            fil = periodos.periodo.posicionY
            valorX = periodos.periodo.posicionX.valores()
            valorY = periodos.periodo.posicionY.valores()      

            self.graficar(periodos.periodo.posiciones.valores(), tamañoRejilla, self.paciente.getNombre(), nPeriodo)

            if self.paciente.getPeriodos() < 10000 and self.info:
                print("Se ha ejecuta el periodo No.", str(nPeriodo), "¿Desea continuar?", "\n(Si=Presione Enter, No=Presione cualquier tecla)")
                respuesta = input()
                if respuesta != "":
                    break
            elif self.paciente.getPeriodos() >= 10000 and self.info:
                print("Se ha ejecuta el periodo No.", str(nPeriodo))
                

            nPeriodoPatronIgual = listaPeriodos.compararPatron()
            if nPeriodoPatronIgual != None:
                self.paciente.setN(nPeriodoPatronIgual)
                self.paciente.setN1(nPeriodo - nPeriodoPatronIgual)
                if nPeriodoPatronIgual == 0:
                    msj = "El patron del periodo " + str(nPeriodo) + " se repite con el del periodo inicial"
                else:
                    msj = "El patron del periodo " + str(nPeriodo) + " se repite con el del periodo " + str(nPeriodoPatronIgual)

                if (nPeriodo - nPeriodoPatronIgual) == 1:
                    self.paciente.setResultado("Mortal")
                else:
                    self.paciente.setResultado("Grave")
                self.paciente.setMensaje(msj)   
                if self.info:            
                    print("\nCaso:",self.paciente.getResultado())
                break
        
        if self.info:
            print(msj)
            print("")


    def graficar(self, posi, tamañoRejilla, nombrePaciente, periodoPaciente): 
        posicion = 0
        graphviz = 'digraph G {\n  rejilla[shape=box label=<\n<TABLE border="0" cellspacing="0" cellpadding="40"  bgcolor="white">'
        for i in range(tamañoRejilla):
            graphviz += '\n<TR>'
            for j in range(tamañoRejilla):
                posicion += 1
                if posi != None:
                    if posicion == posi.numero:
                        graphviz += '\n<TD border="1"  width="5.0" height="5.0" bgcolor="blue"></TD>'
                        posi = posi.siguiente
                    else:
                        graphviz += '\n<TD border="1"  width="5.0" height="5.0" bgcolor="white"></TD>'
                else:
                    graphviz += '\n<TD border="1"  width="5.0" height="5.0" bgcolor="white"></TD>'
            graphviz += "\n</TR>"
        graphviz += '\n</TABLE>>];\n}'
        txt = 'grafica.txt'
        with open(txt, 'w') as grafica:
            grafica.write(graphviz)
        pdf = nombrePaciente + 'Periodo' + str(periodoPaciente) + '.pdf'
        os.system("dot.exe -Tpdf " + txt + " -o " + pdf )
        #webbrowser.open(pdf)

    def reportar(self):
        archivo_xml = ET.parse("./ArchivoSalida.xml")
        pacientes = archivo_xml.getroot() 

        nombrePaciente = self.paciente.getNombre()
        edadPaciente = str(self.paciente.getEdad())
        periodosPaciente = str(self.paciente.getPeriodos())
        tamañoRejillaPaciente = str(self.paciente.getTamañoRejilla())
        resultadoPaciente = self.paciente.getResultado()
        nPaciente = str(self.paciente.getN())
        n1Paciente = str(self.paciente.getN1())
        paciente = ET.Element('paciente')
        datospersonales = ET.SubElement(paciente, 'datospersonales')
        nombre = ET.SubElement(datospersonales, 'nombre')
        nombre.text = nombrePaciente
        edad = ET.SubElement(datospersonales, 'edad')
        edad.text = edadPaciente
        periodos = ET.SubElement(paciente, 'periodos')
        periodos.text = periodosPaciente
        m = ET.SubElement(paciente, 'm')
        m.text = tamañoRejillaPaciente
        resultado = ET.SubElement(paciente, 'resultado')
        resultado.text = resultadoPaciente
        n = ET.SubElement(paciente, 'n')
        n.text = nPaciente
        n1 = ET.SubElement(paciente, 'n1')
        n1.text = n1Paciente
        asdf = ET.SubElement(paciente, 'asdf')
        asdf.text = None

        pacientes.append(paciente)
        archivo_xml.write("./ArchivoSalida.xml")