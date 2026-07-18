from engine.terrain.world_map import WorldMap


class PrecipitationModel:
    """
    Transfers excess cloud water back to the planetary surface.

    Over land, precipitation becomes surface water.
    Over ocean, precipitation returns directly to the
    existing ocean-water reservoir.

    The precipitation field records how much water
    precipitated during the current update.
    """

    def apply(
        self,
        world_map: WorldMap,
    ) -> None:
        for row in world_map.tiles:
            for tile in row:
                tile.precipitation = 0.0

                excess = (
                    tile.cloud_water
                    - tile.precipitation_threshold
                )

                if excess <= 0.0:
                    continue

                tile.cloud_water -= excess

                if tile.is_ocean:
                    tile.ground_moisture += excess
                else:
                    tile.surface_water += excess

                tile.precipitation = excess