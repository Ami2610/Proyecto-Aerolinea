class Asiento:
    def __init__(self, fila: int, butaca: int, pasajero):
        self._fila = fila
        self._butaca = butaca
        self._pasajero = pasajero

    @property
    def fila(self):
        return self._fila

    @property
    def butaca(self):
        return self._butaca

    @property
    def pasajero(self):
        return self._pasajero

    def __str__(self):
        letra_butaca = {
            0: "A",
            1: "B",
            2: "C",
            3: "D"
        }.get(self.butaca, "")

        return f"{self.fila}{letra_butaca}"
