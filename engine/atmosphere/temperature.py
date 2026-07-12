from engine.atmosphere.atmosphere import Atmosphere
from engine.terrain.world_map import WorldMap


class TemperatureModel:
    """
    Calculates the initial temperature distribution of the planet.

    Temperature is influenced by:
    - solar radiation;
    - altitude;
    - atmospheric heat capacity.
    """

    def apply(
        self,
        world_map: WorldMap,
        atmosphere: Atmosphere,
    ) -> None:
        for row in world_map.tiles:
            for tile in row:
                solar_heating = tile.light

                altitude_cooling = tile.altitude * 0.45

                atmospheric_retention = (
                    atmosphere.heat_capacity * 0.25
                )

                normalized_temperature = (
                    solar_heating
                    - altitude_cooling
                    + atmospheric_retention
                )

                normalized_temperature = max(
                    0.0,
                    min(normalized_temperature, 1.0),
                )

                tile.temperature = (
                    -30.0
                    + normalized_temperature * 80.0
                )