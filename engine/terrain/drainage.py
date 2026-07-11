from engine.terrain.slope import calculate_slope
from engine.terrain.tile import Tile
from engine.terrain.world_map import WorldMap


def find_lowest_neighbor(
    world_map: WorldMap,
    origin: Tile,
) -> Tile | None:
    """
    Retorna a vizinha válida de menor altitude.

    Retorna None quando:
    - não existem vizinhas;
    - nenhuma vizinha está abaixo da origem.
    """

    neighbors = world_map.get_neighbors(
        origin.x,
        origin.y,
    )

    lower_neighbors = [
        neighbor
        for neighbor in neighbors
        if calculate_slope(origin, neighbor) > 0.0
    ]

    if not lower_neighbors:
        return None

    return min(
        lower_neighbors,
        key=lambda tile: tile.altitude,
    )