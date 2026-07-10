from engine.terrain.world_map import WorldMap


class TerrainGenerator:
    """
    Responsável pela geração inicial do relevo.
    """

    def generate(self, world_map: WorldMap) -> None:

        for y in range(world_map.height):

            altitude = y / (world_map.height - 1)

            for x in range(world_map.width):

                tile = world_map.get_tile(x, y)

                if tile is not None:
                    tile.altitude = altitude