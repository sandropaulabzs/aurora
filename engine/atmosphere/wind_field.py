from engine.atmosphere.wind_model import WindModel
from engine.terrain.world_map import WorldMap


class WindField:
    """
    Applies the local wind model across the entire world map.
    """

    def __init__(self) -> None:
        self.model = WindModel()

    def apply(self, world_map: WorldMap) -> None:
        for y in range(world_map.height):
            for x in range(world_map.width):
                tile = world_map.get_tile(x, y)

                assert tile is not None

                wind = self.model.calculate(
                    world_map,
                    tile,
                )

                tile.wind_dx = wind.dx
                tile.wind_dy = wind.dy
                tile.wind_speed = wind.speed