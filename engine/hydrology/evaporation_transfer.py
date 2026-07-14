from engine.terrain.world_map import WorldMap


class EvaporationTransfer:
    """
    Transfers water from the ground to the atmosphere
    according to each tile's evaporation potential.
    """

    def apply(
        self,
        world_map: WorldMap,
        transfer_rate: float = 0.05,
    ) -> None:
        if not 0.0 <= transfer_rate <= 1.0:
            raise ValueError(
                "transfer_rate must be between zero and one"
            )

        for row in world_map.tiles:
            for tile in row:
                transferred_water = (
                    tile.evaporation
                    * tile.ground_moisture
                    * transfer_rate
                )

                transferred_water = min(
                    transferred_water,
                    tile.ground_moisture,
                )

                tile.ground_moisture -= transferred_water
                tile.atmospheric_moisture += transferred_water