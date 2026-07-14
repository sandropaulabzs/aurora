from engine.terrain.world_map import WorldMap


class PrecipitationModel:
    """
    Transfers excess cloud water back to the ground.

    The precipitation field records how much water
    precipitated during the current update.
    """

    def apply(
        self,
        world_map: WorldMap,
    ) -> None:
        for row in world_map.tiles:
            for tile in row:
                # Every update begins with no precipitation.
                tile.precipitation = 0.0

                excess = (
                    tile.cloud_water
                    - tile.precipitation_threshold
                )

                if excess <= 0.0:
                    continue

                tile.cloud_water -= excess
                tile.ground_moisture += excess
                tile.precipitation = excess