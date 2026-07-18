from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class WorldReport:
    """
    Scientific summary of the current world state.
    """

    highest_temperature: float
    highest_temperature_position: tuple[int, int]

    lowest_pressure: float
    lowest_pressure_position: tuple[int, int]

    highest_cloud_water: float
    highest_cloud_water_position: tuple[int, int]

    highest_surface_water: float
    highest_surface_water_position: tuple[int, int]

    precipitating_tiles: int