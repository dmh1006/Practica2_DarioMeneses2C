from utils.clases.ProblemaRuta import ProblemaRuta
from utils.clases.ResultadoBusqueda import ResultadoBusqueda


class PlanificadorTramos:
    def __init__(self, mapa, penalizaciones):
        self.mapa = mapa
        self.penalizaciones = penalizaciones

    def planificar(self, inicio, objetivos, algoritmo_busqueda):
        camino_total = []
        coste_total = 0

        nodos_expandidos_total = 0
        frontera_max_total = 0
        tiempo_total = 0

        actual = inicio

        for obj in objetivos:
            problema = ProblemaRuta(actual, obj, self.mapa, self.penalizaciones)
            resultado = algoritmo_busqueda(problema)

            nodos_expandidos_total += resultado.get_nodos_expandidos()
            frontera_max_total = max(frontera_max_total, resultado.get_frontera_max())
            tiempo_total += resultado.get_tiempo_ms()

            if not resultado.hay_solucion():
                return ResultadoBusqueda(
                    False,
                    nodo_solucion=None,
                    nodos_expandidos=nodos_expandidos_total,
                    frontera_max=frontera_max_total,
                    tiempo_ms=tiempo_total
                )

            tramo = resultado.get_camino()
            if not camino_total:
                camino_total.extend(tramo)
            else:
                camino_total.extend(tramo[1:])

            coste_total += resultado.get_coste()
            actual = obj

        nodo_final = _NodoFinal(camino_total, coste_total)

        return ResultadoBusqueda(
            True,
            nodo_solucion=nodo_final,
            nodos_expandidos=nodos_expandidos_total,
            frontera_max=frontera_max_total,
            tiempo_ms=tiempo_total
        )


class _NodoFinal:
    def __init__(self, camino, coste):
        self._camino = camino
        self._coste = coste

    def camino(self):
        return self._camino

    def getG(self):
        return self._coste
