class Persona:
    def __init__(self, nombre, edad, raza, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.nacionalidad = nacionalidad

    def imprimir_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Raza: {self.raza}")
        print(f"Nacionalidad: {self.nacionalidad}")

class Bruno(Persona):
    def __init__(self, nombre, edad, raza, nacionalidad, color_ojos, peso, profesion, juego_favorito, odio):
        super().__init__(nombre, edad, raza, nacionalidad)
        self.color_ojos = color_ojos
        self.peso = peso
        self.profesion = profesion
        self.juego_favorito = juego_favorito
        self.odio = odio

    def imprimir_informacion(self):
        super().imprimir_informacion()
        print(f"Color de ojos: {self.color_ojos}")
        print(f"Peso: {self.peso} kg")
        print(f"Profesión: {self.profesion}")
        print(f"Juego favorito: {self.juego_favorito}")
        print(f"Odio: {self.odio}")

bruno_info = Bruno("Lalista", 30, "Blanco", "Italiano", "Verdes", 130, "Videojugador profesional", "Elden Ring", "Leer y las matematicas")
bruno_info.imprimir_informacion()
