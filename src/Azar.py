import random
import string
from Pasajero import Pasajero
from Maleta import Maleta

class Azar:

    @staticmethod
    def genera_nombre():
        nombres = ["Miguel", "Maria", "Susana", "Octavio", "Soledad",
                   "Juan", "Javier", "Pilar", "Adolfo", "Victor", "Jose", "Rocio",
                   "Claudia", "Ana", "Sonia", "Francisco", "Esmeralda", "Jorge",
                   "Celia", "Tomas", "Ramon", "Violeta"]

        apellidos = ["Diaz", "Fernandez", "Lopez", "Delgado", "Hernandez",
                     "Perez", "Garcia", "Martinez", "Suarez", "Rodriguez",
                     "Gutierrez", "Sevilla", "Gomez", "Arroyo", "Toledo",
                     "Segovia", "Madrid", "Cuenca", "Lugo", "Cano", "Castillo", "Alameda"]

        nombre = random.choice(nombres)
        apellido1 = random.choice(apellidos)
        apellido2 = random.choice(apellidos)
        return f"{nombre} {apellido1} {apellido2}"

    @staticmethod
    def genera_num(longitud):
        return ''.join(random.choices("0123456789", k=longitud))

    @staticmethod
    def genera_pasaporte():
        letras = ''.join(random.choices(string.ascii_uppercase, k=3))
        numeros = Azar.genera_num(6)
        return letras + numeros

    @staticmethod
    def genera_telefono():
        return '6' + Azar.genera_num(8)

    @staticmethod
    def genera_edad():
        return random.randint(1, 99)

    @staticmethod
    def genera_maleta():
        peso = round(random.uniform(2, 32), 2)
        ancho = random.randint(30, 59)
        alto = random.randint(50, 79)
        fondo = random.randint(20, 39)
        return Maleta(peso, ancho, alto, fondo)

    @staticmethod
    def genera_pasajero():
        return Pasajero(
            nombre=Azar.genera_nombre(),
            pasaporte=Azar.genera_pasaporte(),
            telefono=Azar.genera_telefono(),
            edad=Azar.genera_edad(),
            maleta=Azar.genera_maleta()
        )
