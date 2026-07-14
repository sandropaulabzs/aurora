from engine.terrain.world_map import WorldMap


class PrecipitationThresholdModel:
    """
    Computes the local amount of cloud water required
    before precipitation can begin.

    This is a simplified atmospheric abstraction.
    Colder air requires a lower normalized threshold,
    while warmer air can sustain more cloud water.
    """

    MIN_THRESHOLD = 0.20
    MAX_THRESHOLD = 0.70

    def apply(
        self,
        world_map: WorldMap,
    ) -> None:
        threshold_range = (
            self.MAX_THRESHOLD
            - self.MIN_THRESHOLD
        )

        for row in world_map.tiles:
            for tile in row:
                normalized_temperature = (
                    tile.temperature + 30.0
                ) / 80.0

                normalized_temperature = max(
                    0.0,
                    min(normalized_temperature, 1.0),
                )

                tile.precipitation_threshold = (
                    self.MIN_THRESHOLD
                    + (
                        normalized_temperature
                        * threshold_range
                    )
                )