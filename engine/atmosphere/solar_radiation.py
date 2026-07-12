import math

from engine.terrain.world_map import WorldMap


class SolarRadiation:
    """
    Calcula a distribuição inicial de energia solar no planeta.

    O equador recebe mais energia.
    Os polos recebem menos energia.
    """

    def apply(self, world_map: WorldMap) -> None:
        if world_map.height <= 1:
            raise ValueError("world map height must be greater than one")

        for y in range(world_map.height):
            normalized_y = y / (world_map.height - 1)

            latitude = (normalized_y * 2.0) - 1.0

            radiation = math.cos(
                latitude * math.pi / 2.0
            )

            for x in range(world_map.width):
                tile = world_map.get_tile(x, y)

                assert tile is not None

                tile.light = radiation