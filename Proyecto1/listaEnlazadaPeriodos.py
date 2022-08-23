class Nodo:
    def __init__(self, periodo=None, siguiente=None):
        self.periodo = periodo
        self.siguiente = siguiente

class ListaEnlazadaPeriodos:
    def __init__(self):
        self.primero = None
        self.nPeriodo = None

    def insertar(self, periodo):
        if self.primero == None:
            self.primero = Nodo(periodo=periodo)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(periodo=periodo)

    def buscarPeriodo(self, numPeriodo):
        actual = self.primero
        while actual != None:
            if actual.periodo.numeroPeriodo == numPeriodo:
                self.nPeriodo = actual
                if actual.periodo.posiciones != None:
                    return False
            actual = actual.siguiente
        return True

    def valores(self):
        valores = self.primero
        return valores

    def buscarCeldas(self, posX, posY):
        numeroX = self.nPeriodo.periodo.posicionX.valores()
        numeroY = self.nPeriodo.periodo.posicionY.valores()
        while numeroX != None and numeroY != None:
            if posX == numeroX.numero and posY == numeroY.numero:
                return True
            numeroX = numeroX.siguiente
            numeroY = numeroY.siguiente
        return False

    def generarPatron(self):
        actualPos = self.nPeriodo.periodo.posiciones.valores()
        patron = self.nPeriodo.periodo.patron

        for i in range(self.nPeriodo.periodo.posicionX.longitud()):
            auxPos = actualPos.numero
            avance = 0

            while (actualPos.anterior != None and actualPos.anterior.numero > auxPos):
                actualPos.numero = actualPos.anterior.numero
                actualPos.anterior.numero = auxPos
                avance += 1
                actualPos = actualPos.anterior

            while avance >= 0:
                if actualPos.siguiente != None:
                    actualPos = actualPos.siguiente
                avance -= 1

        while actualPos != None:
            if actualPos.anterior != None:
                actualPos = actualPos.anterior
            else:
                break

        actual = actualPos
        while actual != None:
            patron += str(actual.numero) + ", "
            actual = actual.siguiente
        self.nPeriodo.periodo.patron = patron

    def compararPatron(self):
        primero = self.primero
        actual = self.nPeriodo
        while primero.periodo.numeroPeriodo != actual.periodo.numeroPeriodo:   
            if primero.periodo.patron == actual.periodo.patron:
                return primero.periodo.numeroPeriodo
            primero = primero.siguiente