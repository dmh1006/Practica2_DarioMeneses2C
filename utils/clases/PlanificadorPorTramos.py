from utils.clases.ProblemaRuta import ProblemaRuta
from utils.clases.ResultadoBusqueda import ResultadoBusqueda


class PlanificadorPorTramos:
    """
    Planifica una ruta pasando por varios objetivos en orden.
    Cada tramo se resuelve como un problema independiente.
    """

    def __init__(self, mapa, penalizaciones):
        self.mapa = mapa
        self.penalizaciones = penalizaciones

    def planificar(self, inicio, objetivos, algoritmo_busqueda):
        """
        inicio: (fila, columna)
        objetivos: lista de estados [(f,c), (f,c), ...]
        algoritmo_busqueda: función de búsqueda (anchura, voraz o A*)
        """

        camino_total = []
        coste_total = 0

        nodos_expandidos_total = 0
        frontera_max_total = 0
        tiempo_total = 0

        actual = inicio

        for obj in objetivos:
            problema = ProblemaRuta(
                actual,
                obj,
                self.mapa,
                self.penalizaciones
            )

            resultado = algoritmo_busqueda(problema)

            # Acumulamos métricas
            nodos_expandidos_total += resultado.get_nodos_expandidos()
            frontera_max_total = max(frontera_max_total, resultado.get_frontera_max())
            tiempo_total += resultado.get_tiempo_ms()

            # Si no hay solución en algún tramo, se cancela todo
            if not resultado.hay_solucion():
                return ResultadoBusqueda(
                    False,
                    nodo_solucion=None,
                    nodos_expandidos=nodos_expandidos_total,
                    frontera_max=frontera_max_total,
                    tiempo_ms=tiempo_total
                )

            camino_tramo = resultado.get_camino()

            # Concatenar caminos evitando repetir el punto inicial del tramo
            if not camino_total:
                camino_total.extend(camino_tramo)
            else:
                camino_total.extend(camino_tramo[1:])

            coste_total += resultado.get_coste()
            actual = obj

        # Nodo final "artificial" para encapsular el camino completo
        nodo_final = _NodoFinal(camino_total, coste_total)

        return ResultadoBusqueda(
            True,
            nodo_solucion=nodo_final,
            nodos_expandidos=nodos_expandidos_total,
            frontera_max=frontera_max_total,
            tiempo_ms=tiempo_total
        )


class _NodoFinal:
    """
    Nodo mínimo para representar un camino completo ya concatenado.
    """
    def __init__(self, camino, coste):
        self._camino = camino
        self._coste = coste

    def camino(self):
        return self._camino

    def getG(self):
        return self._coste
