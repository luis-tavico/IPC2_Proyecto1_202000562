class Nodo:
    def __init__(self, paciente=None, siguiente=None):
        self.paciente = paciente
        self.siguiente = siguiente

class ListaEnlazadaPacientes:
    def __init__(self):
        self.primero = None
        self.largo = 0

    def insertar(self, paciente):
        if self.primero == None:
            self.primero = Nodo(paciente=paciente)
            self.largo += 1
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(paciente=paciente)
        self.largo += 1

    def valores(self):
        valores = self.primero
        return valores

    def mostrar(self):
        actual = self.primero
        while actual != None:
            actual = actual.siguiente
    
    def longitud(self):
        return self.largo