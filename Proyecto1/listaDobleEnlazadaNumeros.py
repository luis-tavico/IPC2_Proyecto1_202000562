class Nodo:
    def __init__(self, numero=None, siguiente=None, anterior=None):
        self.numero = numero
        self.siguiente = siguiente
        self.anterior = anterior

class ListaDobleEnlazadaNumeros:
    def __init__(self):
        self.primero = None
        self.primero_ = None
        self.largo = 0
    
    def insertar(self, numero):
        if self.primero == None:
            self.primero = Nodo(numero=numero)
            self.primero_ = self.primero
            self.largo += 1
        else:
            actual = Nodo(numero=numero, anterior=self.primero)
            self.primero.siguiente = actual
            self.primero = actual 
            self.largo += 1 

    def valores(self):
        valores = self.primero_
        return valores
    
    def longitud(self):
        return self.largo