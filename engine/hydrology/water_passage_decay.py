from engine.terrain.world_map import WorldMap


class WaterPassageDecayModel:
    """
    Slowly fades hydrological memory.

    This prevents ancient channels from
    remaining forever after water stops flowing.
    """

    DEFAULT_DECAY = 0.9999

    def apply(
        self,
        world_map: WorldMap,
        decay: float = DEFAULT_DECAY,
    ) -> None:
        if not 0.0 <= decay <= 1.0:
            raise ValueError(
                "decay must be between zero and one"
            )

        for row in world_map.tiles:
            for tile in row:
                tile.water_passage *= decay