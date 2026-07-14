from dataclasses import dataclass


@dataclass(slots=True)
class Tile:
    """
    Represents a single environmental cell of the Aurora world.
    """

    x: int
    y: int

    altitude: float = 0.0

    ground_moisture: float = 0.0
    evaporation: float = 0.0

    atmospheric_moisture: float = 0.0
    vapor_capacity: float = 0.0
    cloud_water: float = 0.0
    precipitation_threshold: float = 0.0
    precipitation: float = 0.0

    temperature: float = 20.0
    pressure: float = 0.0

    wind_dx: int = 0
    wind_dy: int = 0
    wind_speed: float = 0.0

    fertility: float = 0.5
    light: float = 1.0