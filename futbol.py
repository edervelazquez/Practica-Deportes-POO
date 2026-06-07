from deporte import Deporte


class Futbol(Deporte):
    def __init__(self, nombre, num_jugadores, duracion_min, puntuacion_maxima, num_arbitros):
        super().__init__(nombre, num_jugadores, duracion_min, puntuacion_maxima)
        self.num_arbitros = num_arbitros

    def forma_de_anotar(self):
        return "Metiendo el balón a la portería, vale 1 punto"
