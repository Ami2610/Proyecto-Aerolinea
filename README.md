# Proyecto Final – Sistema de Gestión de Aerolínea en Python ✈️

Este proyecto simula un sistema básico de gestión de vuelos, pasajeros y reservas para una aerolínea. Se basa en una versión original en Java, adaptada y mejorada utilizando **Python** con **POO**, modularización e interfaz gráfica.

---

## 🎯 Objetivos del Proyecto

- Aplicar conceptos de programación estructurada y orientada a objetos.
- Utilizar listas, diccionarios y clases para organizar datos.
- Implementar una interfaz gráfica opcional con `tkinter`.
- Simular reservas de vuelos, cálculo de ingresos y listado de pasajeros.

---

## 🗂️ Estructura del Proyecto

```
proyecto_aerolinea/
│
├── main.py                      # Menú para elegir modo consola o interfaz
├── gestion_aerolinea.py        # Lógica principal del sistema (clase GestionAerolinea)
├── interfaz.py                 # Interfaz gráfica con tkinter
│
├── asiento.py                  # Clase Asiento
├── avion.py                    # Clase Avion + Enum Clase (BUSINESS, TURISTA)
├── vuelo.py                    # Clase Vuelo
├── pasajero.py                 # Clase Pasajero
├── maleta.py                   # Clase Maleta
├── azar.py                     # Generador aleatorio de pasajeros y maletas
```

---

## 🧪 Ejecución del Proyecto

### ▶️ Desde consola (menú texto):
```bash
python main.py
```
Y selecciona la opción 1 (modo consola).

### 🖱️ Desde interfaz gráfica:
```bash
python main.py
```
Y selecciona la opción 2 (modo gráfico).

---

## ✅ Funcionalidades

- Inicializar vuelos y aviones.
- Reservar asiento aleatorio para pasajeros generados automáticamente.
- Ver mapa de ocupación de asientos.
- Listar pasajeros por clase y vuelo.
- Mostrar pasajeros menores de 15 años.
- Calcular ingresos estimados del vuelo (considerando descuentos).

---

## 📚 Tecnologías utilizadas

- Python 3
- `tkinter` para la GUI
- POO: clases, herencia, propiedades
- Simulación de entrada con `random`

---

## 👨‍💻 Autor

Proyecto adaptado por [Tu Nombre Aquí] para el curso de **Programación Estructurada y Fundamentos**.