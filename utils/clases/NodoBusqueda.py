class NodoBusqueda:
    """
    Nodo de búsqueda 
    Guarda:
      - estado: (fila, col)
      - padre: referencia a otro NodoBusqueda
      - g: coste acumulado
      - h: heurística
      - f: evaluación (por defecto f=g; en voraz será f=h; en A* f=g+h)
    """

    def __init__(self, estado, padre, g, h=None):
        self.estado = estado
        self.padre = padre
        self.g = g
        self.h = 0 if h is None else h
        self.f = g  # por defecto

    # Getters
    def getPadre(self):
        return self.padre

    def getEstado(self):
        return self.estado

    def getG(self):
        return self.g

    def getH(self):
        return self.h

    def getF(self):
        return self.f

    # Setter
    def setF(self, f):
        self.f = f

    # Reconstrucción de camino (lista de estados)
    def camino(self):
        x = self
        result = []
        while x:
            result.append(x.getEstado())
            x = x.getPadre()
        return list(reversed(result))

    def __repr__(self):
        return "NodoBusqueda " + str(self.estado) + "(f:" + str(self.f) + " g:" + str(self.g) + " h:" + str(self.h) + ")"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.getEstado() == other.getEstado()

    def __lt__(self, other):
        return self.f < other.f
