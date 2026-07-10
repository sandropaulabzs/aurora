import random

from engine.terrain.world_seed import WorldSeed


class NoiseGenerator:
    """
    Gera valores pseudoaleatórios determinísticos por coordenada.
    """

    def __init__(self, seed: WorldSeed) -> None:
        self.seed = seed

    def value(self, x: int, y: int) -> float:
        coordinate_seed = (
            self.seed.value * 73_856_093
            ^ x * 19_349_663
            ^ y * 83_492_791
        )

        generator = random.Random(coordinate_seed)

        return generator.random()