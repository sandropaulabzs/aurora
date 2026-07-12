from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Atmosphere:
    """
    Represents the planet's basic atmospheric state.
    """

    density: float
    heat_capacity: float
    pressure: float
    moisture_capacity: float