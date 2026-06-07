from deporte import Deporte


class Basquetbol(Deporte):
    def __init__(self, nombre, num_jugadores, duracion_min, puntuacion_maxima, altura_canasta):
        super().__init__(nombre, num_jugadores, duracion_min, puntuacion_maxima)
        self.altura_canasta = altura_canasta

    def forma_de_anotar(self):
        return "Encestando: 3 puntos larga distancia, 2 puntos cerca, 1 punto tiro libre"
