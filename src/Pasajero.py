class Pasajero:
    def __init__(self, nombre: str, pasaporte: str, telefono: str, edad: int, maleta):
        self._nombre = nombre
        self._pasaporte = pasaporte
        self._telefono = telefono
        self._edad = edad
        self._maleta = maleta  # Se espera que sea una instancia de Maleta

    @property
    def nombre(self):
        return self._nombre

    @property
    def pasaporte(self):
        return self._pasaporte

    @property
    def telefono(self):
        return self._telefono

    @property
    def edad(self):
        return self._edad

    @property
    def maleta(self):
        return self._maleta

    def __str__(self):
        return f"{self.nombre} (Pasaporte: {self.pasaporte}, Edad: {self.edad})"
