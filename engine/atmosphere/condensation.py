from engine.terrain.world_map import WorldMap


class CondensationModel:
    """
    Condenses excess atmospheric moisture into cloud water.

    Atmospheric moisture above the vapor capacity
    becomes condensed water.
    """

    def apply(
        self,
        world_map: WorldMap,
    ) -> None:

        for row in world_map.tiles:
            for tile in row:

                excess = (
                    tile.atmospheric_moisture
                    - tile.vapor_capacity
                )

                if excess <= 0.0:
                    continue

                tile.atmospheric_moisture -= excess
                tile.cloud_water += excess