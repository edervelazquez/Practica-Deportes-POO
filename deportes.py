# Parte 1 — Clase base

class Deporte:
    def __init__(self, nombre, num_jugadores, duracion_min, puntuacion_maxima):
        self.nombre = nombre
        self.num_jugadores = num_jugadores
        self.duracion_min = duracion_min
        self.__puntuacion_maxima = puntuacion_maxima

    def mostrar_info(self):
        print(f"Deporte: {self.nombre}")
        print(f"  Jugadores: {self.num_jugadores}")
        print(f"  Duración (min): {self.duracion_min}")
        print(f"  Puntuación máxima: {self.__puntuacion_maxima}")

    def get_puntuacion_maxima(self):
        return self.__puntuacion_maxima

    def set_puntuacion_maxima(self, valor):
        if valor > 0:
            self.__puntuacion_maxima = valor
        else:
            print("Error: la puntuación máxima debe ser mayor que cero.")


# Parte 2 — Clases hijas: Futbol y Basquetbol

class Futbol(Deporte):
    def __init__(self, nombre, num_jugadores, duracion_min, puntuacion_maxima, num_arbitros):
        super().__init__(nombre, num_jugadores, duracion_min, puntuacion_maxima)
        self.num_arbitros = num_arbitros

    def forma_de_anotar(self):
        return "Metiendo el balón a la portería, vale 1 punto"


class Basquetbol(Deporte):
    def __init__(self, nombre, num_jugadores, duracion_min, puntuacion_maxima, altura_canasta):
        super().__init__(nombre, num_jugadores, duracion_min, puntuacion_maxima)
        self.altura_canasta = altura_canasta

    def forma_de_anotar(self):
        return "Encestando: 3 puntos larga distancia, 2 puntos cerca, 1 punto tiro libre"


# Parte 3 — Nueva clase: FutbolAmericano

class FutbolAmericano(Deporte):
    def __init__(self, nombre, num_jugadores, duracion_min, puntuacion_maxima, num_cuartos):
        super().__init__(nombre, num_jugadores, duracion_min, puntuacion_maxima)
        self.num_cuartos = num_cuartos

    def forma_de_anotar(self):
        return "Touchdown: 6 puntos, gol de campo: 3 puntos, conversion: 1 o 2 puntos"


# --- Pruebas ---

futbol = Futbol("Fútbol", 11, 90, 100, 3)
basquetbol = Basquetbol("Básquetbol", 5, 48, 200, 3.05)
futbol_americano = FutbolAmericano("Fútbol Americano", 11, 60, 150, 4)

deportes = [futbol, basquetbol, futbol_americano]

for deporte in deportes:
    print("\n" + "=" * 40)
    deporte.mostrar_info()
    print(f"  Forma de anotar: {deporte.forma_de_anotar()}")

# Prueba del setter con valor inválido
print("\n" + "=" * 40)
print("Prueba setter con valor inválido (-5):")
futbol.set_puntuacion_maxima(-5)

print("\nPrueba setter con valor válido (120):")
futbol.set_puntuacion_maxima(120)
print(f"  Puntuación máxima actualizada: {futbol.get_puntuacion_maxima()}")
