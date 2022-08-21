class Paciente:
    def __init__(self, nombre = None, edad = None, periodos = None, listaPeriodos = None, tamañoRejilla = None, n = None, resultado = None):
        self.nombre = nombre
        self.edad = edad
        self.periodos = periodos
        self.listaPeriodos = listaPeriodos
        self.tamañoRejilla = tamañoRejilla
        self.n = n
        self.resultado = resultado
    
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

    def getResultado(self):
        return self.resultado

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

    def setResultado(self, resultado):
        self.resultado = resultado