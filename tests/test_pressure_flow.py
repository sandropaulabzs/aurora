from engine.atmosphere.pressure_flow import (
    find_lowest_pressure_neighbor,
)
from engine.terrain.world_map import WorldMap


def test_returns_neighbor_with_lowest_pressure() -> None:
    world_map = WorldMap(width=3, height=3)

    origin = world_map.get_tile(1, 1)

    assert origin is not None

    for neighbor in world_map.get_neighbors(
        origin.x,
        origin.y,
    ):
        neighbor.pressure = 0.8

    lowest = world_map.get_tile(2, 2)

    assert lowest is not None

    lowest.pressure = 0.2

    result = find_lowest_pressure_neighbor(
        world_map,
        origin,
    )

    assert result is lowest


def test_works_on_map_corner() -> None:
    world_map = WorldMap(width=2, height=2)

    origin = world_map.get_tile(0, 0)
    east = world_map.get_tile(1, 0)
    south = world_map.get_tile(0, 1)
    southeast = world_map.get_tile(1, 1)

    assert origin is not None
    assert east is not None
    assert south is not None
    assert southeast is not None

    east.pressure = 0.7
    south.pressure = 0.4
    southeast.pressure = 0.1

    result = find_lowest_pressure_neighbor(
        world_map,
        origin,
    )

    assert result is southeast