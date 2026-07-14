from engine.terrain.tile import Tile


def calculate_pressure_gradient(
    origin: Tile,
    target: Tile,
) -> float:
    """
    Returns the pressure gradient between two tiles.

    Positive values indicate movement toward the target.

    Negative values indicate movement toward the origin.
    """

    return round(
        origin.pressure - target.pressure,
        6,
    )