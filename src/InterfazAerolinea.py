import tkinter as tk
from tkinter import ttk, messagebox
from GestionAerolinea import GestionAerolinea
from Avion import Clase
from Pasajero import Pasajero
from Maleta import Maleta
from Vuelo import Vuelo
from Avion import Avion

class InterfazAerolinea:
    def __init__(self):
        self.sistema = GestionAerolinea()
        self.ventana = tk.Tk()
        self.ventana.title("✈️ Sistema de Gestión de Aerolínea")
        self.ventana.geometry("900x775")
        self.centrar_ventana(900, 775)

        self.vuelo_seleccionado = tk.StringVar()
        self.sistema.crear_vuelo_predeterminado()
        self.vuelos = self.sistema.vuelos
        self.vuelo_seleccionado.set(str(self.vuelos[0]))

        self.estilos()
        self.crear_paneles()
        self.ventana.mainloop()

    def centrar_ventana(self, ancho, alto):
        screen_width = self.ventana.winfo_screenwidth()
        screen_height = self.ventana.winfo_screenheight()
        x = (screen_width // 2) - (ancho // 2)
        y = (screen_height // 2) - (alto // 2)
        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    def estilos(self):
        estilo = ttk.Style()
        estilo.configure("TButton", padding=6, relief="flat", background="#4472C4", foreground="black")
        estilo.configure("TLabel", padding=4)
        estilo.configure("TFrame", background="#f2f2f2")

    def crear_paneles(self):
        contenedor = ttk.Frame(self.ventana)
        contenedor.pack(fill="both", expand=True)

        # --- Scrollable panel izquierdo ---
        panel_scroll = ttk.Frame(contenedor)
        panel_scroll.pack(side="left", fill="y", padx=10, pady=10)

        canvas = tk.Canvas(panel_scroll, width=300, height=750)
        scrollbar = ttk.Scrollbar(panel_scroll, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Habilitar scroll con la rueda del ratón
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(-1 * int(event.delta / 120), "units"))

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.panel_izquierdo = self.scrollable_frame

        # --- Panel derecho permanece igual ---
        self.panel_derecho = ttk.Frame(contenedor)
        self.panel_derecho.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.crear_formulario()
        self.crear_botones()

        self.texto_salida = tk.Text(self.panel_derecho, wrap="word", font=("Consolas", 11), state="disabled")
        self.texto_salida.pack(fill="both", expand=True)

    def crear_formulario(self):
        self.campos_pasajero = {}
        frame_encabezado = ttk.Frame(self.panel_izquierdo)
        frame_encabezado.pack(fill="x", pady=(5, 0))

        label_titulo = ttk.Label(frame_encabezado, text="🧍 Datos del pasajero")
        label_titulo.pack(side="left")

        btn_limpiar = ttk.Button(frame_encabezado, text="🧹", width=2, command=self.limpiar_formulario)
        btn_limpiar.pack(side="right", padx=5)

        frame_datos = ttk.LabelFrame(self.panel_izquierdo)
        frame_datos.pack(fill="x", pady=(0, 5))

        self.crear_input(frame_datos, "Nombre", 30)
        self.crear_input(frame_datos, "Apellido", 30)
        self.crear_input(frame_datos, "Edad", 3)
        self.crear_input(frame_datos, "Pasaporte", 15)
        self.crear_input(frame_datos, "Teléfono", 15)

        frame_maleta = ttk.LabelFrame(frame_datos, text="📦 Maleta")
        frame_maleta.pack(fill="x", pady=5)
        for campo in ["Peso (kg)", "Ancho (cm)", "Alto (cm)", "Fondo (cm)"]:
            self.crear_input(frame_maleta, campo, 4)

        frame_asiento = ttk.LabelFrame(frame_datos, text="💺 Asiento")
        frame_asiento.pack(fill="x", pady=5)
        self.crear_input(frame_datos, "Clase (0: Business, 1: Turista)", 1)
        self.crear_input(frame_datos, "Fila", 2)
        self.crear_input(frame_datos, "Letra asiento (A-D)", 1)

        ttk.Label(self.panel_izquierdo, text="Vuelo:").pack(pady=(10, 2))
        self.selector_vuelo = ttk.Combobox(
            self.panel_izquierdo,
            textvariable=self.vuelo_seleccionado,
            values=[str(v) for v in self.vuelos],
            width=45,
            justify="center",
            state="readonly"
        )
        self.selector_vuelo.pack()

    def crear_input(self, contenedor, etiqueta, max_chars):
        frame = ttk.Frame(contenedor)
        frame.pack(fill="x", padx=5, pady=2)
        ttk.Label(frame, text=etiqueta, width=25).pack(side="left")

        def validar_input(P):
            if etiqueta == "Nombre" and any(char.isdigit() for char in P):
                return False
            return len(P) <= max_chars

        entry = ttk.Entry(frame, width=15, validate="key")
        entry['validatecommand'] = (self.ventana.register(validar_input), '%P')
        entry.pack(side="left")
        self.campos_pasajero[etiqueta] = entry

    def crear_botones(self):
        botones = [
            ("💺 Reservar", self.reservar),
            ("🗺 Mostrar mapa", self.mostrar_mapa),
            ("📄 Listar pasajeros", self.listar_pasajeros),
            ("👶 Pasajeros <18", self.pasajeros_menores),
            ("💰 Ingresos", self.mostrar_ingresos),
            ("🛬 Agregar vuelo", self.agregar_vuelo),
            ("✂ Eliminar vuelo", self.eliminar_vuelo),
            ("✏ Editar vuelo", self.editar_vuelo)
        ]
        for texto, comando in botones:
            ttk.Button(self.panel_izquierdo, text=texto, command=comando).pack(fill="x", pady=3)

    def leer_entrada(self, campo):
        valor = self.campos_pasajero[campo].get().strip()
        if not valor:
            raise ValueError(f"Campo vacío: {campo}")
        return valor

    def limpiar_formulario(self):
        for campo in self.campos_pasajero.values():
            campo.delete(0, 'end')
        self.mostrar_texto("Formulario limpiado correctamente.\n")

    def obtener_vuelo_actual(self):
        for vuelo in self.sistema.vuelos:
            if str(vuelo) == self.vuelo_seleccionado.get():
                return vuelo
        raise Exception("Vuelo no encontrado")

    def mostrar_texto(self, texto):
        self.texto_salida.config(state="normal")
        self.texto_salida.delete("1.0", "end")
        self.texto_salida.insert("end", texto)
        self.texto_salida.config(state="disabled")

    def reservar(self):
        try:
            nombre = self.leer_entrada("Nombre")
            apellido = self.leer_entrada("Apellido")
            edad = int(self.leer_entrada("Edad"))
            pasaporte = self.leer_entrada("Pasaporte")
            telefono = self.leer_entrada("Teléfono")
            peso = float(self.leer_entrada("Peso (kg)"))
            ancho = int(self.leer_entrada("Ancho (cm)"))
            alto = int(self.leer_entrada("Alto (cm)"))
            fondo = int(self.leer_entrada("Fondo (cm)"))
            clase = int(self.leer_entrada("Clase (0: Business, 1: Turista)"))
            fila = int(self.leer_entrada("Fila"))
            letra = self.leer_entrada("Letra asiento (A-D)").upper()

            if clase not in [0, 1] or letra not in "ABCD":
                raise ValueError("Clase o letra de asiento inválida")

            asiento = ord(letra) - ord("A") + 1
            clase_obj = Clase.BUSINESS if clase == 0 else Clase.TURISTA
            vuelo = self.obtener_vuelo_actual()
            avion = vuelo.avion

            if avion.get_pasajero(fila, asiento, clase_obj):
                raise Exception("Asiento ocupado")

            maleta = Maleta(peso, ancho, alto, fondo)
            pasajero = Pasajero(f"{nombre} {apellido}", pasaporte, telefono, edad, maleta)
            avion.reservar_asiento(fila, asiento, clase_obj, pasajero)

            mensaje = (
                f"✅ Reserva exitosa:\n"
                f"{nombre} {apellido}, edad {edad}, pasaporte {pasaporte}, asiento {fila}{letra}, clase {clase_obj.name}, vuelo {vuelo}\n"
            )
            if maleta.excede_de_medidas() or maleta.excede_de_peso():
                mensaje += "⚠ Exceso de equipaje. Se aplicarán cargos.\n"
            self.mostrar_texto(mensaje)
        except Exception as e:
            self.mostrar_texto(f"❌ Error: {str(e)}\n")

    def mostrar_mapa(self):
        avion = self.obtener_vuelo_actual().avion
        texto = ""
        for clase in [Clase.BUSINESS, Clase.TURISTA]:
            texto += f"\nClase {clase.name}:\n"
            for fila in range(1, avion.get_numero_filas(clase) + 1):
                estado = "".join("X" if avion.get_pasajero(fila, b, clase) else "." for b in range(1, avion.get_butacas_por_fila() + 1))
                texto += f"Fila {fila}: {estado}\n"
        self.mostrar_texto(texto)

    def listar_pasajeros(self):
        avion = self.obtener_vuelo_actual().avion
        texto = ""
        for clase in [Clase.BUSINESS, Clase.TURISTA]:
            texto += f"\nClase {clase.name}:\n"
            for fila in range(1, avion.get_numero_filas(clase) + 1):
                for b in range(1, avion.get_butacas_por_fila() + 1):
                    p = avion.get_pasajero(fila, b, clase)
                    if p:
                        letra = chr(ord("A") + b - 1)
                        texto += f"{fila}{letra}: {p.nombre}, Edad: {p.edad}\n"
        self.mostrar_texto(texto)

    def pasajeros_menores(self):
        avion = self.obtener_vuelo_actual().avion
        texto = "👶 Pasajeros <18 años:\n"
        for clase in [Clase.BUSINESS, Clase.TURISTA]:
            for fila in range(1, avion.get_numero_filas(clase) + 1):
                for b in range(1, avion.get_butacas_por_fila() + 1):
                    p = avion.get_pasajero(fila, b, clase)
                    if p and p.edad < 18:
                        letra = chr(ord("A") + b - 1)
                        texto += f"{fila}{letra}: {p.nombre}, Edad: {p.edad}\n"
        self.mostrar_texto(texto)

    def mostrar_ingresos(self):
        avion = self.obtener_vuelo_actual().avion
        ingresos = 0
        for clase, precio in [(Clase.BUSINESS, self.sistema.PRECIO_BILLETE_BUSINESS), (Clase.TURISTA, self.sistema.PRECIO_BILLETE_TURISTA)]:
            for fila in range(1, avion.get_numero_filas(clase) + 1):
                for b in range(1, avion.get_butacas_por_fila() + 1):
                    p = avion.get_pasajero(fila, b, clase)
                    if p:
                        descuento = self.sistema.DESCUENTO_INFANTIL if p.edad < 15 else 0
                        ingresos += precio * (1 - descuento / 100)
        self.mostrar_texto(f"💰 Ingresos estimados: €{ingresos:.2f}\n")

    def agregar_vuelo(self):
        nueva_ventana = tk.Toplevel(self.ventana)
        nueva_ventana.title("Agregar vuelo")
        entradas = {}
        for campo in ["Origen", "Destino", "Fecha (dd/mm/yyyy)", "Modelo avión", "Filas Business", "Filas Turista"]:
            fila = ttk.Frame(nueva_ventana)
            fila.pack(padx=5, pady=3)
            ttk.Label(fila, text=campo, width=25).pack(side="left")
            entrada = ttk.Entry(fila)
            entrada.pack(side="left")
            entradas[campo] = entrada

        def guardar():
            try:
                origen = entradas["Origen"].get()
                destino = entradas["Destino"].get()
                fecha = entradas["Fecha (dd/mm/yyyy)"].get()
                modelo = entradas["Modelo avión"].get()
                filas_b = int(entradas["Filas Business"].get())
                filas_t = int(entradas["Filas Turista"].get())
                avion = Avion(modelo, filas_b, filas_t)
                vuelo = Vuelo(origen, destino, fecha, avion)
                self.sistema.vuelos.append(vuelo)
                self.actualizar_selector_vuelos()
                self.vuelo_seleccionado.set(str(vuelo))
                nueva_ventana.destroy()
                self.mostrar_texto(f"🛫 Vuelo agregado: {vuelo}\n")
            except Exception as e:
                messagebox.showerror("Error", f"Datos inválidos: {str(e)}")

        ttk.Button(nueva_ventana, text="Guardar", command=guardar).pack(pady=10)

    def editar_vuelo(self):
        vuelo_actual = self.obtener_vuelo_actual()
        nueva_ventana = tk.Toplevel(self.ventana)
        nueva_ventana.title("Editar vuelo")

        # --- Contenedor principal ---
        contenedor = ttk.Frame(nueva_ventana)
        contenedor.pack(padx=20, pady=20, fill="both", expand=True)

        entradas = {}
        campos = ["Origen", "Destino", "Fecha (dd/mm/yyyy)", "Modelo avión", "Filas Business", "Filas Turista"]

        for campo in campos:
            fila = ttk.Frame(contenedor)
            fila.pack(fill="x", pady=5)

            ttk.Label(fila, text=campo, width=20).pack(side="left", padx=5)
            entrada = ttk.Entry(fila, width=30)
            entrada.pack(side="left", padx=5)

            # Insertar datos existentes según el campo
            if campo == "Origen":
                entrada.insert(0, vuelo_actual.origen)
            elif campo == "Destino":
                entrada.insert(0, vuelo_actual.destino)
            elif campo == "Fecha (dd/mm/yyyy)":
                entrada.insert(0, vuelo_actual.fecha)
            elif campo == "Modelo avión":
                entrada.insert(0, vuelo_actual.avion.modelo)
            elif campo == "Filas Business":
                entrada.insert(0, vuelo_actual.avion.filas_business)
            elif campo == "Filas Turista":
                entrada.insert(0, vuelo_actual.avion.filas_turista)

            entradas[campo] = entrada

        # Foco inicial
        entradas["Origen"].focus()

        # --- Botón guardar ---
        def guardar():
            try:
                origen = entradas["Origen"].get()
                destino = entradas["Destino"].get()
                fecha = entradas["Fecha (dd/mm/yyyy)"].get()
                modelo = entradas["Modelo avión"].get()
                filas_b = int(entradas["Filas Business"].get())
                filas_t = int(entradas["Filas Turista"].get())

                vuelo_actual.origen = origen
                vuelo_actual.destino = destino
                vuelo_actual.fecha = fecha
                vuelo_actual.avion.modelo = modelo
                vuelo_actual.avion.filas_business = filas_b
                vuelo_actual.avion.filas_turista = filas_t

                self.actualizar_selector_vuelos()
                self.vuelo_seleccionado.set(str(vuelo_actual))
                nueva_ventana.destroy()
                self.mostrar_texto(f"✏ Vuelo editado: {vuelo_actual}\n")
            except Exception as e:
                messagebox.showerror("Error", f"Datos inválidos: {str(e)}")

        ttk.Button(contenedor, text="Guardar", command=guardar).pack(pady=10)

        # --- Ajustar tamaño automáticamente al contenido ---
        nueva_ventana.update_idletasks()
        nueva_ventana.minsize(nueva_ventana.winfo_reqwidth(), nueva_ventana.winfo_reqheight())

        # --- Hacer la ventana modal (opcional) ---
        nueva_ventana.grab_set()

    def eliminar_vuelo(self):
        vuelo_actual = self.obtener_vuelo_actual()
        if len(self.sistema.vuelos) <= 1:
            messagebox.showwarning("Advertencia", "Debe haber al menos un vuelo.")
            return
        self.sistema.vuelos.remove(vuelo_actual)
        self.actualizar_selector_vuelos()
        self.vuelo_seleccionado.set(str(self.sistema.vuelos[0]))
        self.mostrar_texto("✂ Vuelo eliminado.\n")

    def actualizar_selector_vuelos(self):
        self.selector_vuelo["values"] = [str(v) for v in self.sistema.vuelos]

if __name__ == "__main__":
    InterfazAerolinea()
