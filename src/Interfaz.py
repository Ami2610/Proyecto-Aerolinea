import tkinter as tk
from tkinter import messagebox, simpledialog
from GestionAerolinea import GestionAerolinea
from Avion import Clase

class InterfazAerolinea:
    def __init__(self):
        self.sistema = GestionAerolinea()
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Aerolínea")
        self.ventana.geometry("400x450")
        self.crear_botones()
        self.ventana.mainloop()

    def crear_botones(self):
        botones = [
            ("Inicializar aviones y vuelos", self.inicializar),
            ("Reservar asiento", self.reservar),
            ("Mostrar mapa de asientos", self.mostrar_mapa),
            ("Listar pasajeros", self.listar_pasajeros),
            ("Pasajeros menores de 15 años", self.mostrar_menores),
            ("Calcular ingresos", self.mostrar_ingresos),
            ("Salir", self.ventana.quit)
        ]
        for texto, comando in botones:
            tk.Button(self.ventana, text=texto, width=40, height=2, command=comando).pack(pady=5)

    def inicializar(self):
        self.sistema.inicializar_aviones_y_vuelos()
        messagebox.showinfo("Inicializado", "Aviones y vuelos inicializados.")

    def seleccionar_vuelo(self):
        vuelo = simpledialog.askinteger("Seleccionar vuelo", "0: La Habana\n1: Cancún\n2: Punta Cana", minvalue=0, maxvalue=2)
        if vuelo is None:
            raise ValueError("Selección cancelada")
        return vuelo

    def seleccionar_clase(self):
        clase_num = simpledialog.askinteger("Seleccionar clase", "0: Business\n1: Turista", minvalue=0, maxvalue=1)
        if clase_num is None:
            raise ValueError("Selección cancelada")
        return Clase.BUSINESS if clase_num == 0 else Clase.TURISTA

    def reservar(self):
        if not self.sistema.aviones_y_vuelos_inicializados:
            messagebox.showerror("Error", "Debe inicializar primero.")
            return
        try:
            vuelo = self.seleccionar_vuelo()
            clase = self.seleccionar_clase()
            self.sistema.reservar_asiento(self.sistema.vuelos[vuelo].avion, clase)
        except ValueError:
            messagebox.showinfo("Cancelado", "Operación cancelada.")

    def mostrar_mapa(self):
        if not self.sistema.aviones_y_vuelos_inicializados:
            messagebox.showerror("Error", "Debe inicializar primero.")
            return
        try:
            vuelo = self.seleccionar_vuelo()
            self.sistema.vuelos[vuelo].avion.mostrar_mapa_de_asientos()
        except ValueError:
            pass

    def listar_pasajeros(self):
        if not self.sistema.aviones_y_vuelos_inicializados:
            messagebox.showerror("Error", "Debe inicializar primero.")
            return
        try:
            vuelo = self.seleccionar_vuelo()
            self.sistema.mostrar_pasajeros(self.sistema.vuelos[vuelo].avion)
        except ValueError:
            pass

    def mostrar_menores(self):
        if not self.sistema.aviones_y_vuelos_inicializados:
            messagebox.showerror("Error", "Debe inicializar primero.")
            return
        try:
            vuelo = self.seleccionar_vuelo()
            self.sistema.mostrar_pasajeros_menores(self.sistema.vuelos[vuelo].avion, 15)
        except ValueError:
            pass

    def mostrar_ingresos(self):
        if not self.sistema.aviones_y_vuelos_inicializados:
            messagebox.showerror("Error", "Debe inicializar primero.")
            return
        try:
            vuelo = self.seleccionar_vuelo()
            self.sistema.mostrar_ingresos(self.sistema.vuelos[vuelo].avion)
        except ValueError:
            pass

if __name__ == "__main__":
    InterfazAerolinea()
