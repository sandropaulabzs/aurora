from engine.terrain.ocean import is_ocean
from engine.terrain.sea_level import SeaLevel
from engine.terrain.world_map import WorldMap


class OceanInitializer:
    """
    Initializes the world's oceans.
    """

    def apply(
        self,
        world_map: WorldMap,
        sea_level: SeaLevel,
    ) -> None:
        for row in world_map.tiles:
            for tile in row:

                tile.is_ocean = is_ocean(
                    tile,
                    sea_level,
                )

                if tile.is_ocean:
                    tile.ground_moisture = 1.0