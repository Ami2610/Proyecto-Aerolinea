class Vuelo:
    def __init__(self, pais_origen: str, pais_destino: str, fecha: str, avion):
        self._pais_origen = pais_origen
        self._pais_destino = pais_destino
        self._fecha = fecha
        self._avion = avion  # Se espera una instancia de la clase Avion

    @property
    def pais_origen(self):
        return self._pais_origen

    @property
    def pais_destino(self):
        return self._pais_destino

    @property
    def fecha(self):
        return self._fecha

    @property
    def avion(self):
        return self._avion

    def __str__(self):
        return f"{self._fecha} - {self._pais_origen} → {self._pais_destino} ({self._avion.modelo})"
