from engine.atmosphere.atmosphere import Atmosphere
from engine.terrain.world_map import WorldMap


class PressureModel:
    """
    Calculates the initial atmospheric pressure distribution.

    Pressure is influenced by:
    - atmospheric density;
    - temperature;
    - altitude.
    """

    def apply(
        self,
        world_map: WorldMap,
        atmosphere: Atmosphere,
    ) -> None:
        for row in world_map.tiles:
            for tile in row:
                normalized_temperature = (
                    tile.temperature + 30.0
                ) / 80.0

                altitude_loss = tile.altitude * 0.55
                temperature_effect = (
                    1.0 - normalized_temperature
                ) * 0.20

                normalized_pressure = (
                    atmosphere.density
                    + temperature_effect
                    - altitude_loss
                )

                normalized_pressure = max(
                    0.0,
                    min(normalized_pressure, 1.0),
                )

                tile.pressure = normalized_pressure