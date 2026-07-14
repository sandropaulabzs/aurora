from enum import Enum, auto


class WaterState(Enum):
    """
    Represents the physical state of water.
    """

    SOLID = auto()
    LIQUID = auto()
    VAPOR = auto()