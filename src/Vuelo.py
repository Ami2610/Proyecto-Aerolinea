class Vuelo:
    def __init__(self, origen, destino, fecha, avion):
        self.origen = origen              # string, ej: "Madrid"
        self.destino = destino            # string, ej: "París"
        self.fecha = fecha                # string, ej: "01/09/2025"
        self.avion = avion                # objeto Avion

    def __str__(self):
        return f"{self.origen} → {self.destino} ({self.fecha})"
