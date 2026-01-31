class ResultadoBusqueda:
    """
    Clase contenedora del resultado de una búsqueda.
    Sigue el estilo visto en clase: el algoritmo devuelve un resultado,
    y fuera se analizan métricas y camino.
    """

    def __init__(self, exito, nodo_solucion=None,
                 nodos_expandidos=0,
                 frontera_max=0,
                 tiempo_ms=0):
        self.exito = exito
        self.nodo_solucion = nodo_solucion
        self.nodos_expandidos = nodos_expandidos
        self.frontera_max = frontera_max
        self.tiempo_ms = tiempo_ms

    # -----------------------------
    # Getters
    # -----------------------------
    def hay_solucion(self):
        return self.exito

    def get_nodo_solucion(self):
        return self.nodo_solucion

    def get_camino(self):
        if not self.exito or self.nodo_solucion is None:
            return []
        return self.nodo_solucion.camino()

    def get_coste(self):
        if not self.exito or self.nodo_solucion is None:
            return float("inf")
        return self.nodo_solucion.getG()

    def get_nodos_expandidos(self):
        return self.nodos_expandidos

    def get_frontera_max(self):
        return self.frontera_max

    def get_tiempo_ms(self):
        return self.tiempo_ms

    # -----------------------------
    # Representación
    # -----------------------------
    def __repr__(self):
        if not self.exito:
            return "ResultadoBusqueda(SIN SOLUCIÓN)"
        return (
            "ResultadoBusqueda("
            + "coste=" + str(self.get_coste())
            + ", pasos=" + str(len(self.get_camino()))
            + ", nodos=" + str(self.nodos_expandidos)
            + ", frontera_max=" + str(self.frontera_max)
            + ", tiempo_ms=" + str(self.tiempo_ms)
            + ")"
        )
