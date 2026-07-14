from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class WindVector:
    """
    Represents local atmospheric movement.

    dx and dy define direction.
    speed defines normalized wind intensity.
    """

    dx: int
    dy: int
    speed: float