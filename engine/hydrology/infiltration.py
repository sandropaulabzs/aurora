from engine.terrain.world_map import WorldMap


class InfiltrationModel:
    """
    Transfers surface water into available terrestrial soil storage.

    Ocean tiles do not infiltrate because they do not use
    the terrestrial soil-water reservoir.

    The infiltration field records how much water
    entered the soil during the current update.
    """

    DEFAULT_RATE = 0.05

    def apply(
        self,
        world_map: WorldMap,
        infiltration_rate: float = DEFAULT_RATE,
    ) -> None:
        if not 0.0 <= infiltration_rate <= 1.0:
            raise ValueError(
                "infiltration_rate must be between zero and one"
            )

        for row in world_map.tiles:
            for tile in row:
                tile.infiltration = 0.0

                if tile.is_ocean:
                    continue

                available_capacity = max(
                    0.0,
                    tile.soil_capacity
                    - tile.ground_moisture,
                )

                potential_infiltration = (
                    tile.surface_water
                    * infiltration_rate
                )

                infiltrated = min(
                    potential_infiltration,
                    available_capacity,
                )

                tile.surface_water -= infiltrated
                tile.ground_moisture += infiltrated
                tile.infiltration = infiltrated