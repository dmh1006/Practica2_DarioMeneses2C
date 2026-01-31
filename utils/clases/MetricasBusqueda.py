import time


class MetricasBusqueda:
    """
    Clase para almacenar métricas de una búsqueda:
    - nodos expandidos
    - tamaño máximo de la frontera
    - tiempo de ejecución
    """

    def __init__(self):
        self.nodos_expandidos = 0
        self.frontera_max = 0
        self._t_inicio = None
        self._t_fin = None

    # -----------------------------
    # Control de tiempo
    # -----------------------------
    def iniciar_tiempo(self):
        self._t_inicio = time.time()

    def finalizar_tiempo(self):
        self._t_fin = time.time()

    def tiempo_ms(self):
        if self._t_inicio is None or self._t_fin is None:
            return 0
        return (self._t_fin - self._t_inicio) * 1000

    # -----------------------------
    # Contadores
    # -----------------------------
    def incrementar_expandidos(self):
        self.nodos_expandidos += 1

    def actualizar_frontera(self, tam_frontera):
        if tam_frontera > self.frontera_max:
            self.frontera_max = tam_frontera
