from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class StabilitySnapshot:
    """
    Represents the hydrological state of the planet
    at a specific simulation tick.
    """

    tick: int

    total_water: float

    maximum_cloud_water: float
    maximum_surface_water: float
    maximum_runoff: float
    maximum_water_passage: float

    precipitating_tiles: int