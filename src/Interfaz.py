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

    def centrar_ventana(self, ventana):
        ventana.update_idletasks()
        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()
        x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto // 2)
        ventana.geometry(f"+{x}+{y}")

    def inicializar(self):
        self.sistema.inicializar_aviones_y_vuelos()
        messagebox.showinfo("Inicializado", "Aviones y vuelos inicializados.")

    def seleccionar_vuelo(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Seleccionar vuelo")
        ventana.geometry("300x200")
        self.centrar_ventana(ventana)
        tk.Label(ventana, text="Seleccione destino:", font=("Arial", 12)).pack(pady=10)

        seleccion = tk.IntVar(value=-1)
        opciones = [("0: La Habana", 0), ("1: Cancún", 1), ("2: Punta Cana", 2)]

        for texto, valor in opciones:
            tk.Radiobutton(ventana, text=texto, variable=seleccion, value=valor).pack(anchor="w", padx=20)

        def confirmar():
            if seleccion.get() != -1:
                self.vuelo_seleccionado = seleccion.get()
                ventana.destroy()
            else:
                messagebox.showerror("Error", "Debe seleccionar una opción.")

        tk.Button(ventana, text="Aceptar", command=confirmar).pack(pady=10)
        ventana.transient(self.ventana)
        ventana.grab_set()
        self.ventana.wait_window(ventana)
        return getattr(self, 'vuelo_seleccionado', None)

    def seleccionar_clase(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Seleccionar clase")
        ventana.geometry("300x180")
        self.centrar_ventana(ventana)
        tk.Label(ventana, text="Seleccione clase:", font=("Arial", 12)).pack(pady=10)

        seleccion = tk.IntVar(value=-1)
        clases = [("0: Business", 0), ("1: Turista", 1)]

        for texto, valor in clases:
            tk.Radiobutton(ventana, text=texto, variable=seleccion, value=valor).pack(anchor="w", padx=20)

        def confirmar():
            if seleccion.get() != -1:
                self.clase_seleccionada = seleccion.get()
                ventana.destroy()
            else:
                messagebox.showerror("Error", "Debe seleccionar una opción.")

        tk.Button(ventana, text="Aceptar", command=confirmar).pack(pady=10)
        ventana.transient(self.ventana)
        ventana.grab_set()
        self.ventana.wait_window(ventana)

        if hasattr(self, 'clase_seleccionada'):
            return Clase.BUSINESS if self.clase_seleccionada == 0 else Clase.TURISTA
        else:
            raise ValueError("Selección cancelada")

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
            if vuelo not in [0, 1, 2]:
                raise ValueError("Número de vuelo inválido.")

            avion = self.sistema.vuelos[vuelo].avion
            menores = []

            for clase in [Clase.BUSINESS, Clase.TURISTA]:
                for fila in range(1, avion.get_numero_filas(clase) + 1):
                    for butaca in range(1, avion.get_butacas_por_fila() + 1):
                        pasajero = avion.get_pasajero(fila, butaca, clase)
                        if pasajero and hasattr(pasajero, "edad") and pasajero.edad < 15:
                            asiento = f"{fila}{chr(ord('A') + butaca - 1)}"
                            menores.append(f"{pasajero.nombre} ({pasajero.edad} años) - Clase {clase.name.title()}, Asiento {asiento}")

            mensaje = "\n".join(menores) if menores else "No hay pasajeros menores de 15 años."
            messagebox.showinfo("Pasajeros Menores de Edad", mensaje)

        except ValueError:
            messagebox.showwarning("Cancelado", "Operación cancelada o entrada inválida.")
        except Exception as e:
            messagebox.showerror("Error inesperado", str(e))

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