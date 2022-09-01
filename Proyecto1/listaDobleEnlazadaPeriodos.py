class Nodo:
    def __init__(self, periodo=None, siguiente=None, anterior=None):
        self.periodo = periodo
        self.siguiente = siguiente
        self.anterior = anterior

class ListaDobleEnlazadaPeriodos:
    def __init__(self):
        self.primero = None
        self.primero_ = None
        self.nPeriodo = None

    def insertar(self, periodo):
        if self.primero == None:
            self.primero = Nodo(periodo=periodo)
            self.primero_ = self.primero
        else:
            actual = Nodo(periodo=periodo, anterior=self.primero)
            self.primero.siguiente = actual
            self.primero = actual 

    def buscarPeriodo(self, numPeriodo):
        actual = self.primero_
        while actual != None:
            if actual.periodo.numeroPeriodo == numPeriodo:
                self.nPeriodo = actual
                if actual.periodo.posiciones != None:
                    return False
            actual = actual.siguiente
        return True

    def valores(self):
        valores = self.primero_
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

    def compararPatron(self):
        actual = self.nPeriodo
        anterior = actual.anterior
        while anterior != None:
            posicionesAnteriorPeriodo = anterior.periodo.posiciones.valores()
            posicionesActualPeriodo = actual.periodo.posiciones.valores()   
            if (posicionesAnteriorPeriodo and posicionesActualPeriodo) != None:     
                while posicionesAnteriorPeriodo.numero == posicionesActualPeriodo.numero:
                    posicionesAnteriorPeriodo = posicionesAnteriorPeriodo.siguiente
                    posicionesActualPeriodo = posicionesActualPeriodo.siguiente
                    if posicionesAnteriorPeriodo == None and posicionesActualPeriodo == None:
                        return anterior.periodo.numeroPeriodo
                    elif posicionesAnteriorPeriodo == None or posicionesActualPeriodo == None:
                        break
            anterior = anterior.anterior
        return None