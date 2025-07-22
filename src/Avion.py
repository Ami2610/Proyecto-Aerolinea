from enum import Enum
from Asiento import Asiento

class Clase(Enum):
    BUSINESS = "BUSINESS"
    TURISTA = "TURISTA"

class Avion:
    ASIENTOS_X_FILA = 4

    def __init__(self, modelo: str, business: int, turista: int):
        self._modelo = modelo
        self._numero_asientos_business = business
        self._numero_asientos_turista = turista

        filas_business = business // self.ASIENTOS_X_FILA
        filas_turista = turista // self.ASIENTOS_X_FILA

        self._asientos_business = [[None for _ in range(self.ASIENTOS_X_FILA)] for _ in range(filas_business)]
        self._asientos_turista = [[None for _ in range(self.ASIENTOS_X_FILA)] for _ in range(filas_turista)]

    @property
    def modelo(self):
        return self._modelo

    def get_numero_filas(self, clase: Clase):
        if clase == Clase.BUSINESS:
            return self._numero_asientos_business // self.ASIENTOS_X_FILA
        else:
            return self._numero_asientos_turista // self.ASIENTOS_X_FILA

    def get_butacas_por_fila(self):
        return self.ASIENTOS_X_FILA

    def get_pasajero(self, fila: int, butaca: int, clase: Clase):
        asiento = None
        if clase == Clase.BUSINESS:
            asiento = self._asientos_business[fila - 1][butaca - 1]
        else:
            asiento = self._asientos_turista[fila - 1][butaca - 1]

        return asiento.pasajero if asiento else None

    def reservar_asiento(self, fila: int, butaca: int, clase: Clase, pasajero):
        if clase == Clase.BUSINESS:
            if self._asientos_business[fila - 1][butaca - 1] is None:
                asiento = Asiento(fila, butaca, pasajero)
                self._asientos_business[fila - 1][butaca - 1] = asiento
                return asiento
        else:  # Clase.TURISTA
            if self._asientos_turista[fila - 1][butaca - 1] is None:
                asiento = Asiento(fila, butaca, pasajero)
                self._asientos_turista[fila - 1][butaca - 1] = asiento
                return asiento
        return None

    def mostrar_mapa_de_asientos(self):
        print(f"\nAvión {self._modelo}")
        for butaca in range(self.ASIENTOS_X_FILA):
            # Mostrar BUSINESS
            for fila in range(len(self._asientos_business)):
                print("B" if self._asientos_business[fila][butaca] else "·", end="")
            print(" ", end="")
            # Mostrar TURISTA
            for fila in range(len(self._asientos_turista)):
                print("T" if self._asientos_turista[fila][butaca] else "·", end="")
            print()
