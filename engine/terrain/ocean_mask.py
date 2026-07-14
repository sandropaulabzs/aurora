from engine.terrain.ocean import is_ocean
from engine.terrain.sea_level import SeaLevel
from engine.terrain.world_map import WorldMap


class OceanMask:
    """
    Computes which tiles belong to the ocean.
    """

    def generate(
        self,
        world_map: WorldMap,
        sea_level: SeaLevel,
    ) -> list[list[bool]]:
        mask: list[list[bool]] = []

        for row in world_map.tiles:
            mask_row: list[bool] = []

            for tile in row:
                mask_row.append(
                    is_ocean(
                        tile,
                        sea_level,
                    )
                )

            mask.append(mask_row)

        return mask