from engine.terrain.world_map import WorldMap


class GeologyStatistics:
    """
    Calcula estatísticas básicas do relevo.
    """

    def __init__(self, world_map: WorldMap) -> None:
        self.world_map = world_map

    def average_altitude(self) -> float:
        total = 0.0
        count = 0

        for row in self.world_map.tiles:
            for tile in row:
                total += tile.altitude
                count += 1

        return total / count

    def highest_altitude(self) -> float:
        return max(
            tile.altitude
            for row in self.world_map.tiles
            for tile in row
        )

    def lowest_altitude(self) -> float:
        return min(
            tile.altitude
            for row in self.world_map.tiles
            for tile in row
        )