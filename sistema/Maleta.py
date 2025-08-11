class Maleta:
    PESO_MAXIMO = 23
    MEDIDA_TOTAL_MAXIMA = 158

    def __init__(self, peso: float, ancho: int, alto: int, fondo: int):
        self._peso = peso
        self._ancho = ancho
        self._alto = alto
        self._fondo = fondo

    @property
    def peso(self):
        return self._peso

    @property
    def medida_total(self):
        return self._ancho + self._alto + self._fondo

    def excede_de_peso(self):
        return self._peso > self.PESO_MAXIMO

    def excede_de_medidas(self):
        return self.medida_total > self.MEDIDA_TOTAL_MAXIMA

    def __str__(self):
        estado_peso = "✔" if not self.excede_de_peso() else "✘ Exceso de peso"
        estado_medida = "✔" if not self.excede_de_medidas() else "✘ Exceso de tamaño"
        return f"Maleta: {self._peso:.2f} kg, {self.medida_total} cm totales [{estado_peso}, {estado_medida}]"
