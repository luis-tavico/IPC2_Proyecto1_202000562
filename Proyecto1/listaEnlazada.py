class Nodo:
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class listaEnlazada:
    def __init__(self):
        self.primero = None

    def insertar(self, dato):
        if self.primero == None:
            self.primero = Nodo(dato=dato)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(dato=dato)

    def mostrar(self):
        actual = self.primero
        while actual != None:
            print("asdf")
            actual = actual.siguiente