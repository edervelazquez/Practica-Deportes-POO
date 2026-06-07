from deporte import Deporte


class FutbolAmericano(Deporte):
    def __init__(self, nombre, num_jugadores, duracion_min, puntuacion_maxima, num_cuartos):
        super().__init__(nombre, num_jugadores, duracion_min, puntuacion_maxima)
        self.num_cuartos = num_cuartos

    def forma_de_anotar(self):
        return "Touchdown: 6 puntos, gol de campo: 3 puntos, conversion: 1 o 2 puntos"
