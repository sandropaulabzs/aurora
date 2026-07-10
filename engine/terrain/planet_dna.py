from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class PlanetDNA:
    """
    Características permanentes de um planeta.
    """

    continentality: float
    relief: float
    volcanism: float
    humidity: float
    temperature: float
    erosion: float
    water_level: float
    stability: float