from dataclasses import dataclass


@dataclass(slots=True)
class Tile:
    """
    Representa uma célula individual do mundo Aurora.
    """

    x: int
    y: int
    altitude: float = 0.0
    moisture: float = 0.0
    temperature: float = 20.0
    fertility: float = 0.5
    light: float = 1.0