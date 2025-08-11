# ✈️ Sistema de Gestión de Aerolínea

Este proyecto implementa un sistema visual para gestionar reservas aéreas, asientos, vuelos y pasajeros, utilizando **Python** con **Tkinter** para la interfaz gráfica.

## 📌 Características principales

- Registro de pasajeros y asignación de asientos.
- Validación de datos de entrada (nombres, edad, pasaporte, etc.).
- Gestión de equipaje con verificación de peso y medidas.
- Visualización del mapa de asientos en diferentes clases.
- Cálculo de ingresos por vuelo.
- Agregado, edición y eliminación de vuelos.
- Interfaz organizada, con separación de acciones y visualización de resultados.

## 🖥 Requisitos

- Python 3.8 o superior
- Tkinter (incluido por defecto en la mayoría de instalaciones de Python)

## ⚙️ Estructura del proyecto

```
/proyecto_aerolinea
├── InterfazAerolinea.py       # Interfaz principal del sistema
├── GestionAerolinea.py        # Lógica principal y constantes del sistema
├── Avion.py                   # Definición del avión y sus clases
├── Vuelo.py                   # Lógica de vuelos
├── Pasajero.py                # Estructura de pasajeros
├── Maleta.py                  # Validaciones de maletas
├── Asiento.py                 # Gestión de asientos
├── main.py                    # Punto de entrada del sistema
```

## 🚀 Cómo ejecutar el sistema

1. Clona o descarga este repositorio en tu máquina.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el archivo principal:

```bash
python main.py
```

La interfaz gráfica se abrirá en el centro de la pantalla.

## ✅ Funcionalidades implementadas

- **Reservar asiento:** Captura los datos del pasajero y su maleta, valida el asiento y lo asigna si está disponible.
- **Mostrar mapa:** Presenta visualmente los asientos ocupados (`X`) y libres (`.`).
- **Listar pasajeros:** Muestra la lista completa de pasajeros por clase y asiento.
- **Pasajeros <18:** Filtra y presenta a los menores de edad.
- **Ingresos estimados:** Calcula el total recaudado por un vuelo.
- **Agregar vuelo:** Permite ingresar nuevos vuelos con sus respectivos aviones.
- **Eliminar vuelo:** Elimina el vuelo actualmente seleccionado.
- **Editar vuelo:** Modifica los datos de un vuelo ya existente.
- **Limpiar formulario:** Borra los datos ingresados en el formulario de manera segura.

## 💡 Posibles mejoras futuras

- Incorporar autenticación de usuarios.
- Mejorar la estética con iconografía moderna.
- Reorganizar la interfaz con pestañas o paneles dinámicos.
