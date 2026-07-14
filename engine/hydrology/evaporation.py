from engine.terrain.world_map import WorldMap


class EvaporationModel:
    """
    Calculates the evaporation potential for each tile.

    This does not move water into the atmosphere yet.
    It only determines how strongly each tile tends to evaporate.
    """

    def apply(
        self,
        world_map: WorldMap,
    ) -> None:
        for row in world_map.tiles:
            for tile in row:
                evaporation = (
                    tile.temperature + 30.0
                ) / 80.0

                evaporation *= tile.ground_moisture

                evaporation = max(
                    0.0,
                    min(evaporation, 1.0),
                )

                tile.evaporation = evaporation