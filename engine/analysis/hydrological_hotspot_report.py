from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class HydrologicalHotspotReport:
    """
    Scientific description of the tile containing
    the greatest amount of surface water.
    """

    position: tuple[int, int]

    altitude: float
    surface_water: float
    ground_moisture: float
    soil_capacity: float

    infiltration: float
    runoff: float
    water_passage: float

    lowest_neighbor_altitude: float | None
    lower_neighbors: int

    @property
    def soil_is_saturated(self) -> bool:
        return (
            self.ground_moisture
            >= self.soil_capacity
        )

    @property
    def is_local_depression(self) -> bool:
        return self.lower_neighbors == 0