from engine.terrain.world_map import WorldMap


class VaporCapacityModel:
    """
    Computes how much water vapor the atmosphere
    can hold based on temperature.
    """

    def apply(
        self,
        world_map: WorldMap,
    ) -> None:
        for row in world_map.tiles:
            for tile in row:

                capacity = (
                    tile.temperature + 30.0
                ) / 80.0

                tile.vapor_capacity = max(
                    0.0,
                    min(capacity, 1.0),
                )