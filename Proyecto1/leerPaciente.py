import os
from modeloPeriodo import Periodo
from listaDobleEnlazadaNumeros import ListaDobleEnlazadaNumeros
import xml.etree.ElementTree as ET

class LeerPaciente:

    def __init__(self, ventanaAnterior, listaPacientes):
        self.ventanaAnterior = ventanaAnterior
        self.listaPacientes = listaPacientes
        self.ejecutar()

    def ejecutar(self):
        pacientes = self.listaPacientes.valores() #Este me da el primer paciente
        paciente = pacientes.paciente 
        listaPeriodos = paciente.getListaPeriodos()
        #periodo = listaPeriodos.valores().periodo
        listaPeriodos.buscarPeriodo(1)
        periodo = listaPeriodos.valores().periodo
        columnas_ = periodo.posicionX
        filas_ = periodo.posicionY

        tamañoRejilla = paciente.getTamañoRejilla()

        #######################3

        nPeriodo = 1

        col = columnas_
        fil = filas_
        valorX = columnas_.valores()
        valorY = filas_.valores()

        listaPeriodos.buscarPeriodo(nPeriodo)
        listaPeriodos.generarPatron()

        for i in range(15):
            nPeriodo += 1

            columnas = ListaDobleEnlazadaNumeros()
            filas = ListaDobleEnlazadaNumeros()
            posiciones = ListaDobleEnlazadaNumeros()
            listaPeriodos.insertar(Periodo(nPeriodo, columnas, filas, posiciones))

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
                    #
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
                            ##################
                            if (valorY.numero == 1):
                                _x = valorX.numero
                                _y = valorY.numero * 0
                                pos = _x + _y
                            else:
                                _x = valorX.numero
                                _y = (valorY.numero - 1) * tamañoRejilla
                                pos = _x + _y
                            posiciones.insertar(pos)
                            ################
                valorX = valorX.siguiente
                valorY = valorY.siguiente

            valorY = fil.valores()
            valorX = col.valores()
            while valorX != None and valorY != None:
                for i in range(4):
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
                        #
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
                                ##################
                                if (x == 1):
                                    _x = x
                                    _y = y * 0
                                    pos = _x + _y
                                else:
                                    _x = x
                                    _y = (y - 1) * tamañoRejilla
                                    pos = _x + _y
                                posiciones.insertar(pos)
                                ################
                valorX = valorX.siguiente
                valorY = valorY.siguiente
          
            col = columnas
            fil = filas
            valorX = columnas.valores()
            valorY = filas.valores()

            listaPeriodos.buscarPeriodo(nPeriodo)
            listaPeriodos.generarPatron()
            nPeriodoPatronIgual = listaPeriodos.compararPatron()
            if nPeriodoPatronIgual != None:
                msj = "El patron del periodo " + str(nPeriodo) + " se repite con el del periodo " + str(nPeriodoPatronIgual) + "\n"
                if nPeriodoPatronIgual == 1:
                    if (nPeriodo - nPeriodoPatronIgual) == 1:
                        msj += "VAS A MORIR XD"
                    else: 
                        msj += "CASO GRAVE"
                else:
                    if (nPeriodo - nPeriodoPatronIgual) == 1:
                        msj += "VAS A MORIR XD"
                    else:
                        msj += "CASO GRAVE"
                print(msj)
                #print(nPeriodo - n)
                nombrePaciente = paciente.getNombre()
                edadPaciente = str(paciente.getEdad())
                periodosPaciente = str(paciente.getPeriodos())
                tamañoRejillaPaciente = str(paciente.getTamañoRejilla())
                pacientes = ET.Element('pacientes')
                paciente = ET.SubElement(pacientes, 'paciente')
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
                resultado.text = "grave"
                n = ET.SubElement(paciente, 'n')
                n.text = "3"

                myData = ET.tostring(pacientes)
                file = open("./datos.xml", "wb")
                file.write(myData)

                posi = periodo.posiciones.valores()
                posicion = 0
                grafica = 'digraph G {\n  rejilla[shape=box label=<\n<TABLE border="0" cellspacing="0" cellpadding="40"  bgcolor="white">'
                for i in range(tamañoRejilla):
                    grafica += '\n<TR>'
                    for j in range(tamañoRejilla):
                        posicion += 1
                        if posi != None:
                            if posicion == posi.numero:
                                grafica += '\n<TD border="1"  width="5.0" height="5.0" bgcolor="blue"></TD>'
                                posi = posi.siguiente
                            else:
                                grafica += '\n<TD border="1"  width="5.0" height="5.0" bgcolor="white"></TD>'
                        else:
                            grafica += '\n<TD border="1"  width="5.0" height="5.0" bgcolor="white"></TD>'
                    grafica += "\n</TR>"
                grafica += '\n</TABLE>>];\n}'
                print(grafica)
                file = open("./nodo.dot", "w+")
                file.write(grafica)
                file.close()
                os.system('dot -Tpng nodo.dot -o imagen.png')
                #self.graficar()
                break

    def graficar(self):
        posicion = 0
        grafica = 'digraph G {\n  rejilla[shape=box label=<\n<TABLE border="0" cellspacing="0" cellpadding="40"  bgcolor="white">'
        for i in range(10):
            grafica += '\n<TR>'
            for j in range(10):
                posicion += 1
                #if posicion == pos..
                grafica += '\n<TD border="1"  width="5.0" height="5.0" bgcolor="white"></TD>'
            grafica += "\n</TR>"
        grafica += '\n</TABLE>>];\n}'
        print(grafica)
        file = open("./nodo.dot", "w+")
        file.write(grafica)
        file.close()
        os.system('dot -Tpng nodo.dot -o imagen.png')