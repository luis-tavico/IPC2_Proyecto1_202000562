class Paciente:
    def __init__(self, nombre=None, edad=None, periodos=None, listaPeriodos=None, tamañoRejilla=None, n=None, n1=None, resultado=None, mensaje=None):
        self.nombre = nombre
        self.edad = edad
        self.periodos = periodos
        self.listaPeriodos = listaPeriodos
        self.tamañoRejilla = tamañoRejilla
        self.n = n
        self.n1 = n1
        self.resultado = resultado
        self.mensaje = mensaje
    
    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getPeriodos(self):
        return self.periodos

    def getListaPeriodos(self):
        return self.listaPeriodos
    
    def getTamañoRejilla(self):
        return self.tamañoRejilla

    def getN(self):
        return self.n

    def getN1(self):
        return self.n1

    def getResultado(self):
        return self.resultado

    def getMensaje(self):
        return self.mensaje

    ######################################

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad

    def setPeriodos(self, periodos):
        self.periodos = periodos

    def setListaPeriodos(self, listaPeriodos):
        self.listaPeriodos = listaPeriodos

    def setTamañoRejilla(self, tamañoRejilla):
        self.tamañoRejilla = tamañoRejilla
        
    def setN(self, n):
        self.n = n

    def setN1(self, n1):
        self.n1 = n1

    def setResultado(self, resultado):
        self.resultado = resultado

    def setMensaje(self, mensaje):
        self.mensaje = mensaje