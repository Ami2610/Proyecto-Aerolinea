from Avion import Avion, Clase
from Vuelo import Vuelo
from Azar import Azar

class GestionAerolinea:
    PRECIO_BILLETE_TURISTA = 350
    PRECIO_BILLETE_BUSINESS = 1500
    DESCUENTO_INFANTIL = 15
    NUM_AVIONES = 3

    def __init__(self):
        self.aviones = []
        self.vuelos = []
        self.aviones_y_vuelos_inicializados = False

    def iniciar(self):
        while True:
            opcion = self.menu()
            if opcion == 0:
                print("Fin de la ejecución.")
                break
            self.ejecutar_opcion(opcion)

    def menu(self):
        print("\n--- MENÚ ---")
        print("1. Inicializar aviones y vuelos")
        print("2. Reservar asiento en un vuelo")
        print("3. Mostrar el mapa de asientos")
        print("4. Mostrar la lista de pasajeros")
        print("5. Mostrar pasajeros menores de 15 años")
        print("6. Mostrar ingresos del vuelo")
        print("0. Finalizar")
        return self.leer_numero(0, 6, "Seleccione una opción: ")

    def leer_numero(self, minimo, maximo, mensaje):
        while True:
            try:
                numero = int(input(mensaje))
                if minimo <= numero <= maximo:
                    return numero
            except ValueError:
                pass
            print(f"Debe ingresar un número entre {minimo} y {maximo}.")

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.inicializar_aviones_y_vuelos()
        elif not self.aviones_y_vuelos_inicializados:
            print("Error. Aviones y vuelos no inicializados.")
        elif opcion == 2:
            vuelo = self.preguntar_vuelo()
            clase = self.preguntar_clase()
            self.reservar_asiento(self.vuelos[vuelo].avion, clase)
        elif opcion == 3:
            vuelo = self.preguntar_vuelo()
            self.vuelos[vuelo].avion.mostrar_mapa_de_asientos()
        elif opcion == 4:
            vuelo = self.preguntar_vuelo()
            self.mostrar_pasajeros(self.vuelos[vuelo].avion)
        elif opcion == 5:
            vuelo = self.preguntar_vuelo()
            self.mostrar_pasajeros_menores(self.vuelos[vuelo].avion, 15)
        elif opcion == 6:
            vuelo = self.preguntar_vuelo()
            self.mostrar_ingresos(self.vuelos[vuelo].avion)

    def inicializar_aviones_y_vuelos(self):
        self.aviones = [
            Avion("Airbus A330", 40, 120),
            Avion("Airbus A310", 20, 100),
            Avion("Airbus A350", 48, 180)
        ]
        self.vuelos = [
            Vuelo("Madrid", "La Habana", "01/12/2024", self.aviones[0]),
            Vuelo("Madrid", "Cancún", "01/12/2024", self.aviones[1]),
            Vuelo("Madrid", "Punta Cana", "01/12/2024", self.aviones[2])
        ]
        self.aviones_y_vuelos_inicializados = True
        print("Aviones y vuelos inicializados.")

    def preguntar_vuelo(self):
        return self.leer_numero(0, 2, "Elija el vuelo (0: La Habana, 1: Cancún, 2: Punta Cana): ")

    def preguntar_clase(self):
        opcion = self.leer_numero(0, 1, "Elija la clase (0: Business, 1: Turista): ")
        return Clase.BUSINESS if opcion == 0 else Clase.TURISTA

    def reservar_asiento(self, avion, clase):
        for fila in range(1, avion.get_numero_filas(clase) + 1):
            for butaca in range(1, avion.get_butacas_por_fila() + 1):
                if avion.get_pasajero(fila, butaca, clase) is None:
                    pasajero = Azar.genera_pasajero()
                    asiento = avion.reservar_asiento(fila, butaca, clase, pasajero)
                    if asiento:
                        letra = chr(ord('A') + butaca - 1)
                        print(f"Reservado el asiento {fila}{letra} en clase {clase.name.lower()} para {pasajero.nombre}")
                        return
        print(f"No hay asientos disponibles en clase {clase.name.lower()}.")

    def mostrar_pasajeros(self, avion):
        print(f"Avión {avion.modelo}")
        for clase in [Clase.BUSINESS, Clase.TURISTA]:
            print(f"Pasajeros en clase {clase.name}:")
            for fila in range(1, avion.get_numero_filas(clase) + 1):
                for butaca in range(1, avion.get_butacas_por_fila() + 1):
                    pasajero = avion.get_pasajero(fila, butaca, clase)
                    if pasajero:
                        print(f"{fila}{chr(ord('A') + butaca - 1)} - {pasajero.nombre}, {pasajero.pasaporte}, {pasajero.edad} años")

    def mostrar_pasajeros_menores(self, avion, edad_maxima):
        print(f"Pasajeros menores de {edad_maxima} años:")
        for clase in [Clase.BUSINESS, Clase.TURISTA]:
            for fila in range(1, avion.get_numero_filas(clase) + 1):
                for butaca in range(1, avion.get_butacas_por_fila() + 1):
                    pasajero = avion.get_pasajero(fila, butaca, clase)
                    if pasajero and pasajero.edad < edad_maxima:
                        print(f"{pasajero.nombre} - {pasajero.edad} años")

    def mostrar_ingresos(self, avion):
        ingresos = 0
        for clase, precio in [(Clase.BUSINESS, self.PRECIO_BILLETE_BUSINESS), (Clase.TURISTA, self.PRECIO_BILLETE_TURISTA)]:
            for fila in range(1, avion.get_numero_filas(clase) + 1):
                for butaca in range(1, avion.get_butacas_por_fila() + 1):
                    pasajero = avion.get_pasajero(fila, butaca, clase)
                    if pasajero:
                        descuento = self.DESCUENTO_INFANTIL if pasajero.edad < 15 else 0
                        ingresos += precio * (1 - descuento / 100)
        print(f"Ingresos estimados del avión {avion.modelo}: {ingresos:.2f} €")

# Solo para consola
if __name__ == "__main__":
    app = GestionAerolinea()
    app.iniciar()
