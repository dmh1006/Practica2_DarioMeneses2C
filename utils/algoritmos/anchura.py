from collections import deque

from utils.clases.MetricasBusqueda import MetricasBusqueda
from utils.clases.ResultadoBusqueda import ResultadoBusqueda


def busqueda_anchura(problema, traza=False):
    """
    Búsqueda en anchura (BFS).
    Devuelve un ResultadoBusqueda con nodo solución y métricas.
    """
    m = MetricasBusqueda()
    m.iniciar_tiempo()

    abiertos = deque()
    cerrados = set()  # guardamos estados

    n0 = problema.inicial
    abiertos.append(n0)
    m.actualizar_frontera(len(abiertos))

    while abiertos:
        ea = abiertos.popleft()
        m.incrementar_expandidos()

        if problema.es_objetivo(ea):
            m.finalizar_tiempo()
            return ResultadoBusqueda(
                True,
                nodo_solucion=ea,
                nodos_expandidos=m.nodos_expandidos,
                frontera_max=m.frontera_max,
                tiempo_ms=m.tiempo_ms(),
            )

        cerrados.add(ea.getEstado())

        sucesores = problema.sucesores(ea)

        # Filtrar: no repetir estados ya explorados o ya en frontera
        estados_en_frontera = {n.getEstado() for n in abiertos}
        nuevos = []
        for s in sucesores:
            est = s.getEstado()
            if est in cerrados:
                continue
            if est in estados_en_frontera:
                continue
            nuevos.append(s)

        abiertos.extend(nuevos)
        m.actualizar_frontera(len(abiertos))

    m.finalizar_tiempo()
    return ResultadoBusqueda(
        False,
        nodo_solucion=None,
        nodos_expandidos=m.nodos_expandidos,
        frontera_max=m.frontera_max,
        tiempo_ms=m.tiempo_ms(),
    )
