from enum import Enum

class Clase(Enum):
    BUSINESS = 0
    TURISTA = 1

class Avion:
    def __init__(self, modelo, filas_business, filas_turista):
        self.modelo = modelo
        self.filas = {
            Clase.BUSINESS: filas_business,
            Clase.TURISTA: filas_turista
        }
        self.butacas_por_fila = 4  # A, B, C, D

        self.asientos = {
            Clase.BUSINESS: [[None for _ in range(self.butacas_por_fila)] for _ in range(filas_business)],
            Clase.TURISTA: [[None for _ in range(self.butacas_por_fila)] for _ in range(filas_turista)]
        }

    # --- Propiedades para GUI y compatibilidad ---
    @property
    def filas_business(self):
        return self.filas[Clase.BUSINESS]

    @filas_business.setter
    def filas_business(self, valor):
        self.filas[Clase.BUSINESS] = valor
        self.asientos[Clase.BUSINESS] = [[None for _ in range(self.butacas_por_fila)] for _ in range(valor)]

    @property
    def filas_turista(self):
        return self.filas[Clase.TURISTA]

    @filas_turista.setter
    def filas_turista(self, valor):
        self.filas[Clase.TURISTA] = valor
        self.asientos[Clase.TURISTA] = [[None for _ in range(self.butacas_por_fila)] for _ in range(valor)]

    # --- Métodos principales ---
    def get_numero_filas(self, clase: Clase) -> int:
        return self.filas[clase]

    def get_butacas_por_fila(self) -> int:
        return self.butacas_por_fila

    def get_pasajero(self, fila: int, asiento: int, clase: Clase):
        if 1 <= fila <= self.get_numero_filas(clase) and 1 <= asiento <= self.butacas_por_fila:
            return self.asientos[clase][fila - 1][asiento - 1]
        return None

    def reservar_asiento(self, fila: int, asiento: int, clase: Clase, pasajero):
        if not (1 <= fila <= self.get_numero_filas(clase) and 1 <= asiento <= self.butacas_por_fila):
            raise ValueError("Fila o asiento fuera de rango.")
        if self.asientos[clase][fila - 1][asiento - 1] is not None:
            raise Exception("El asiento ya está ocupado.")
        self.asientos[clase][fila - 1][asiento - 1] = pasajero

    def eliminar_pasajero(self, fila: int, asiento: int, clase: Clase):
        if not (1 <= fila <= self.get_numero_filas(clase) and 1 <= asiento <= self.butacas_por_fila):
            raise ValueError("Fila o asiento fuera de rango.")
        self.asientos[clase][fila - 1][asiento - 1] = None

    def __str__(self):
        return f"{self.modelo} ({self.filas[Clase.BUSINESS]}F Business, {self.filas[Clase.TURISTA]}F Turista)"
