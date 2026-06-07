import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from futbol import Futbol
from basquetbol import Basquetbol
from futbol_americano import FutbolAmericano


def main():
    futbol = Futbol("Fútbol", 11, 90, 100, 3)
    basquetbol = Basquetbol("Básquetbol", 5, 48, 200, 3.05)
    futbol_americano = FutbolAmericano("Fútbol Americano", 11, 60, 150, 4)

    deportes = [futbol, basquetbol, futbol_americano]

    for deporte in deportes:
        print("\n" + "=" * 40)
        deporte.mostrar_info()
        print(f"  Forma de anotar: {deporte.forma_de_anotar()}")

    print("\n" + "=" * 40)
    print("Prueba setter con valor inválido (-5):")
    futbol.set_puntuacion_maxima(-5)

    print("\nPrueba setter con valor válido (120):")
    futbol.set_puntuacion_maxima(120)
    print(f"  Puntuación máxima actualizada: {futbol.get_puntuacion_maxima()}")


if __name__ == "__main__":
    main()
