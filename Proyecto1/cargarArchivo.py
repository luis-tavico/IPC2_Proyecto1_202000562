import xml.etree.ElementTree as ET
from listaEnlazada import listaEnlazada

class CargarArchivo:
    def __init__(self, ruta):
        self.ruta = ruta

    def leerArchivo(self):
        self.archivo_xml = ET.parse(self.ruta)
        raiz = self.archivo_xml.getroot()
        for hijo in raiz:
            for datospersonales in hijo.findall('datospersonales'):
                for datos in datospersonales:
                    print(datos.text)

        for hijo in raiz:
            for rejilla in hijo.findall('rejilla'):
                for celda in rejilla:
                    print(celda.attrib['f'], end=" ")
                    print(celda.attrib['c'])

    