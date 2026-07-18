from engine.terrain.world_map import WorldMap


class WaterPassageModel:
    """
    Accumulates the historical surface runoff of each tile.

    runoff records the flow of the current tick.
    water_passage preserves that flow as hydrological memory.
    """

    def apply(
        self,
        world_map: WorldMap,
    ) -> None:
        for row in world_map.tiles:
            for tile in row:
                if tile.runoff <= 0.0:
                    continue

                tile.water_passage += tile.runoff