from Vuelo import Vuelo
from Avion import Avion
from Avion import Clase
from Pasajero import Pasajero
from Maleta import Maleta

class GestionAerolinea:
    PRECIO_BILLETE_TURISTA = 350
    PRECIO_BILLETE_BUSINESS = 1500
    DESCUENTO_INFANTIL = 15

    def __init__(self):
        self.vuelos = []

    def crear_vuelo_predeterminado(self):
        avion = Avion("Airbus A330", 4, 6)
        vuelo = Vuelo("Quito", "Guayaquil", "01/12/2024", avion)
        self.vuelos.append(vuelo)

    def agregar_vuelo(self, origen, destino, fecha, modelo, filas_business, filas_turista):
        avion = Avion(modelo, filas_business, filas_turista)
        vuelo = Vuelo(origen, destino, fecha, avion)
        self.vuelos.append(vuelo)
        return vuelo

    def eliminar_vuelo(self, vuelo):
        if vuelo in self.vuelos:
            self.vuelos.remove(vuelo)

    def reservar_asiento(self, avion, fila, asiento, clase, pasajero):
        return avion.reservar_asiento(fila, asiento, clase, pasajero)

    def calcular_ingresos(self, avion):
        ingresos = 0
        for clase, precio in [(Clase.BUSINESS, self.PRECIO_BILLETE_BUSINESS), (Clase.TURISTA, self.PRECIO_BILLETE_TURISTA)]:
            for fila in range(1, avion.get_numero_filas(clase) + 1):
                for butaca in range(1, avion.get_butacas_por_fila() + 1):
                    pasajero = avion.get_pasajero(fila, butaca, clase)
                    if pasajero:
                        descuento = self.DESCUENTO_INFANTIL if pasajero.edad < 15 else 0
                        ingresos += precio * (1 - descuento / 100)
        return ingresos

    def obtener_pasajeros(self, avion):
        lista = []
        for clase in [Clase.BUSINESS, Clase.TURISTA]:
            for fila in range(1, avion.get_numero_filas(clase) + 1):
                for butaca in range(1, avion.get_butacas_por_fila() + 1):
                    pasajero = avion.get_pasajero(fila, butaca, clase)
                    if pasajero:
                        lista.append((fila, butaca, clase, pasajero))
        return lista

    def obtener_pasajeros_menores(self, avion, edad_max):
        menores = []
        for clase in [Clase.BUSINESS, Clase.TURISTA]:
            for fila in range(1, avion.get_numero_filas(clase) + 1):
                for butaca in range(1, avion.get_butacas_por_fila() + 1):
                    pasajero = avion.get_pasajero(fila, butaca, clase)
                    if pasajero and pasajero.edad < edad_max:
                        menores.append((fila, butaca, clase, pasajero))
        return menores

    def lista_pasajeros(self, vuelo):
        lista = []
        for clase in [Clase.BUSINESS, Clase.TURISTA]:
            for fila in range(1, vuelo.avion.get_numero_filas(clase) + 1):
                for butaca in range(1, vuelo.avion.get_butacas_por_fila() + 1):
                    pasajero = vuelo.avion.get_pasajero(fila, butaca, clase)
                    if pasajero:
                        asiento = f"{fila}{chr(ord('A') + butaca - 1)}"
                        lista.append(f"{pasajero.nombre} ({pasajero.pasaporte}) - Edad: {pasajero.edad} - {clase.name.title()} - Asiento: {asiento}")
        return lista