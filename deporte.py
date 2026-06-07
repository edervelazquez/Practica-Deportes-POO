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
