from utils.clases.NodoBusqueda import NodoBusqueda


class ProblemaRuta:
    """
    Problema de búsqueda de ruta en el hospital siguiendo el estilo visto en clase.

    - Estado: (fila, columna)
    - Nodo inicial: NodoBusqueda(inicio, None, g=0, h=heurística(inicio))
    - Sucesores: lista de NodoBusqueda con padre=EA, g actualizado y h calculada
    - Objetivo: estado (fila, columna)

    Coste del movimiento:
      penalización de la celda DESTINO según diccionario de penalizaciones.

    Heurística:
      Manhattan al objetivo (|df|+|dc|).
    """

    def __init__(self, inicio, objetivo, mapa_hospital, penalizaciones):
        self.mapa = mapa_hospital
        self.penalizaciones = penalizaciones
        self.objetivo = objetivo

        self.filas = len(self.mapa)
        self.cols = len(self.mapa[0]) if self.filas > 0 else 0

        # Nodo inicial al estilo clase
        h0 = self.heuristica_estado(inicio)
        self.inicial = NodoBusqueda(inicio, None, 0, h0)

    # -----------------------------
    # Helpers de dominio
    # -----------------------------
    def en_rango(self, estado):
        f, c = estado
        return 0 <= f < self.filas and 0 <= c < self.cols

    def celda(self, estado):
        f, c = estado
        return str(self.mapa[f][c])

    def es_transitable(self, estado):
        # "M" es muro
        return self.celda(estado) != "M"

    def coste_estado(self, estado):
        # coste por entrar a la celda destino
        tipo = self.celda(estado)
        return int(self.penalizaciones.get(tipo, 1))

    def heuristica_estado(self, estado):
        # Manhattan al objetivo
        f, c = estado
        fo, co = self.objetivo
        return abs(f - fo) + abs(c - co)

    # -----------------------------
    # API estilo clase (nodos)
    # -----------------------------
    def es_objetivo(self, nodo):
        return nodo.getEstado() == self.objetivo

    def sucesores(self, nodo):
        """
        Devuelve lista de NodoBusqueda sucesores, con:
          - padre = nodo actual
          - g = g_actual + coste(estado_destino)
          - h = heurística(estado_destino)
        """
        estado = nodo.getEstado()
        f, c = estado

        movimientos = [("N", -1, 0), ("S", 1, 0), ("O", 0, -1), ("E", 0, 1)]
        sucesores = []

        for nombre, df, dc in movimientos:
            nuevo_estado = (f + df, c + dc)

            if not self.en_rango(nuevo_estado):
                continue
            if not self.es_transitable(nuevo_estado):
                continue

            coste_paso = self.coste_estado(nuevo_estado)
            g_nuevo = nodo.getG() + coste_paso
            h_nuevo = self.heuristica_estado(nuevo_estado)

            sucesores.append(NodoBusqueda(nuevo_estado, nodo, g_nuevo, h_nuevo))

        return sucesores
