from GestionAerolinea import GestionAerolinea
from Interfaz import InterfazAerolinea

def main():
    print("Bienvenido al Sistema de Gestión de Aerolínea")
    print("Seleccione el modo de ejecución:")
    print("1. Modo consola")
    print("2. Modo gráfico (interfaz tkinter)")

    while True:
        opcion = input("Ingrese 1 o 2: ")
        if opcion == '1':
            app = GestionAerolinea()
            app.iniciar()
            break
        elif opcion == '2':
            InterfazAerolinea()
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
