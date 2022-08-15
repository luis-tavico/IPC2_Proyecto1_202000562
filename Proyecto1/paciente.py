class Paciente:
    def __init__(self, nombre = None, edad = None, periodo = None, m = None, n = None, rejilla = None, resultado = None):
        self.nombre = nombre
        self.edad = edad
        self.periodo = periodo
        self.m = m
        self.n = n
        self.rejilla = rejilla
        self.resultado = resultado
    
    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getPeriodo(self):
        return self.periodo
    
    def getM(self):
        return self.m

    def getM(self):
        return self.n

    def getRejilla(self):
        return self.rejilla

    def getRejilla(self):
        return self.resultado

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad

    def setPeriodo(self, periodo):
        self.periodo = periodo

    def setM(self, m):
        self.m = m
        
    def setM(self, n):
        self.n = n
    
    def setRejilla(self, rejilla):
        self.rejilla = rejilla

    def setRejilla(self, resultado):
        self.resultado = resultado