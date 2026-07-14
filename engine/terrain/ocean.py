from engine.terrain.sea_level import SeaLevel
from engine.terrain.tile import Tile


def is_ocean(
    tile: Tile,
    sea_level: SeaLevel,
) -> bool:
    """
    Returns True if the tile lies below the planet sea level.
    """

    return tile.altitude <= sea_level.value