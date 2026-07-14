from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SeaLevel:
    """
    Represents the normalized sea level of a planet.

    Values are expected between 0.0 and 1.0.
    """

    value: float

    def __post_init__(self) -> None:
        if not 0.0 <= self.value <= 1.0:
            raise ValueError(
                "Sea level must be between 0.0 and 1.0."
            )