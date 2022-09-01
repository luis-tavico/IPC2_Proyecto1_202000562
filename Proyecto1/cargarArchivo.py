import xml.etree.ElementTree as ET
from modeloPaciente import Paciente
from listaDobleEnlazadaPeriodos import ListaDobleEnlazadaPeriodos
from modeloPeriodo import Periodo
from listaDobleEnlazadaNumeros import ListaDobleEnlazadaNumeros

class CargarArchivo:
    def __init__(self, ruta, listaPacientes):
        self.ruta = ruta
        self.listaPacientes = listaPacientes
        self.leerArchivo()

    def leerArchivo(self):
        self.archivo_xml = ET.parse(self.ruta)
        pacientes = self.archivo_xml.getroot() 

        for paciente in pacientes:
            columnas = ListaDobleEnlazadaNumeros()
            filas = ListaDobleEnlazadaNumeros()
            posiciones = ListaDobleEnlazadaNumeros()
            listaPeriodos = ListaDobleEnlazadaPeriodos()
            datosPersonales = paciente.find('datospersonales')
            nombre = datosPersonales.find('nombre').text
            edad = datosPersonales.find('edad').text
            _periodos = int(paciente.find('periodos').text)
            tamañoRejilla = int(paciente.find('m').text)   
            for rejilla in paciente.findall('rejilla'):
                for celda in rejilla:
                    columnas.insertar(int(celda.attrib['c']))
                    filas.insertar(int(celda.attrib['f']))
                    if (int(celda.attrib['f']) == 1):
                        _x = int(celda.attrib['c'])
                        _y = int(celda.attrib['f']) * 0
                        pos = _x + _y
                        posiciones.insertar(pos)
                    else:
                        _x = int(celda.attrib['c'])
                        _y = (int(celda.attrib['f']) - 1) * tamañoRejilla
                        pos = _x + _y
                        posiciones.insertar(pos)
            periodo = Periodo(0, columnas, filas, posiciones)
            listaPeriodos.insertar(periodo)
            listaPeriodos.buscarPeriodo(0)
            listaPeriodos.generarPatron()
            nuevoPaciente = Paciente(nombre=nombre, edad=edad, periodos=_periodos, listaPeriodos=listaPeriodos, tamañoRejilla=tamañoRejilla)
            self.listaPacientes.insertar(nuevoPaciente)