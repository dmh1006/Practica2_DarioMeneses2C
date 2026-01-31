from utils.clases.MetricasBusqueda import MetricasBusqueda
from utils.clases.ResultadoBusqueda import ResultadoBusqueda


def _extraer_min_f(abiertos):
    """
    Devuelve y elimina de 'abiertos' el nodo con menor f.
    Si hay empate, se queda con el primero que encuentre.
    """
    i_min = 0
    f_min = abiertos[0].getF()
    for i in range(1, len(abiertos)):
        f_i = abiertos[i].getF()
        if f_i < f_min:
            f_min = f_i
            i_min = i
    return abiertos.pop(i_min)


def busqueda_a_estrella(problema, traza=False):
    """
    Búsqueda A*:
        f(n) = g(n) + h(n)

    Estructuras:
    - ABIERTOS: lista de nodos pendientes
    - CERRADOS: diccionario estado -> mejor g encontrado (para podar caminos peores)

    Nota: Sin cola de prioridad; seleccionamos el mínimo f recorriendo la lista.
    """

    metricas = MetricasBusqueda()
    metricas.iniciar_tiempo()

    abiertos = []
    mejor_g = {}  # estado -> mejor g conocido

    n0 = problema.inicial
    n0.setF(n0.getG() + n0.getH())
    abiertos.append(n0)
    mejor_g[n0.getEstado()] = n0.getG()

    metricas.actualizar_frontera(len(abiertos))

    while abiertos:
        # Escogemos el nodo con menor f
        actual = _extraer_min_f(abiertos)
        metricas.incrementar_expandidos()

        # Objetivo
        if problema.es_objetivo(actual):
            metricas.finalizar_tiempo()
            return ResultadoBusqueda(
                True,
                nodo_solucion=actual,
                nodos_expandidos=metricas.nodos_expandidos,
                frontera_max=metricas.frontera_max,
                tiempo_ms=metricas.tiempo_ms(),
            )

        # Expandimos
        for suc in problema.sucesores(actual):
            est = suc.getEstado()
            g_suc = suc.getG()

            # Si es nuevo o mejora el mejor g para ese estado
            if (est not in mejor_g) or (g_suc < mejor_g[est]):
                mejor_g[est] = g_suc
                suc.setF(g_suc + suc.getH())

                # Si ya existe un nodo con ese estado en ABIERTOS, nos quedamos con el mejor f
                reemplazado = False
                for i in range(len(abiertos)):
                    if abiertos[i].getEstado() == est:
                        if abiertos[i].getF() > suc.getF():
                            abiertos[i] = suc
                        reemplazado = True
                        break

                if not reemplazado:
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
