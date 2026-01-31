from utils.clases.MetricasBusqueda import MetricasBusqueda
from utils.clases.ResultadoBusqueda import ResultadoBusqueda


def _extraer_min_f(abiertos):
    """
    Devuelve y elimina de 'abiertos' el nodo con menor f.
    """
    i_min = 0
    f_min = abiertos[0].getF()
    for i in range(1, len(abiertos)):
        f_i = abiertos[i].getF()
        if f_i < f_min:
            f_min = f_i
            i_min = i
    return abiertos.pop(i_min)


def busqueda_voraz(problema, traza=False):
    """
    Búsqueda voraz (primero el mejor):
        f(n) = h(n)

    Estructuras:
    - ABIERTOS: lista de nodos pendientes
    - CERRADOS: conjunto de estados ya explorados
    """

    metricas = MetricasBusqueda()
    metricas.iniciar_tiempo()

    abiertos = []
    cerrados = set()

    n0 = problema.inicial
    n0.setF(n0.getH())   # voraz: prioriza solo heurística
    abiertos.append(n0)

    metricas.actualizar_frontera(len(abiertos))

    while abiertos:
        actual = _extraer_min_f(abiertos)
        est_actual = actual.getEstado()

        if est_actual in cerrados:
            continue

        cerrados.add(est_actual)
        metricas.incrementar_expandidos()

        if problema.es_objetivo(actual):
            metricas.finalizar_tiempo()
            return ResultadoBusqueda(
                True,
                nodo_solucion=actual,
                nodos_expandidos=metricas.nodos_expandidos,
                frontera_max=metricas.frontera_max,
                tiempo_ms=metricas.tiempo_ms(),
            )

        for suc in problema.sucesores(actual):
            est = suc.getEstado()
            if est in cerrados:
                continue

            suc.setF(suc.getH())

            # Evitar duplicados en abiertos (si ya está, nos quedamos con el que tenga menor f)
            encontrado = False
            for i in range(len(abiertos)):
                if abiertos[i].getEstado() == est:
                    if abiertos[i].getF() > suc.getF():
                        abiertos[i] = suc
                    encontrado = True
                    break

            if not encontrado:
                abiertos.append(suc)

        metricas.actualizar_frontera(len(abiertos))

    metricas.finalizar_tiempo()
    return ResultadoBusqueda(
        False,
        nodo_solucion=None,
        nodos_expandidos=metricas.nodos_expandidos,
        frontera_max=metricas.frontera_max,
        tiempo_ms=metricas.tiempo_ms(),
    )
