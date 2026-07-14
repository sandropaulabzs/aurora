from engine.terrain.tile import Tile
from engine.terrain.world_map import WorldMap


def find_lowest_pressure_neighbor(
    world_map: WorldMap,
    tile: Tile,
) -> Tile:
    """
    Returns the neighboring tile with the lowest pressure.
    """

    neighbors = world_map.get_neighbors(
        tile.x,
        tile.y,
    )

    return min(
        neighbors,
        key=lambda neighbor: neighbor.pressure,
    )