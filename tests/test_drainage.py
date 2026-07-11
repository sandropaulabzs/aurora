from engine.terrain.drainage import find_lowest_neighbor
from engine.terrain.world_map import WorldMap


def test_returns_lowest_neighbor() -> None:
    world_map = WorldMap(width=3, height=3)

    origin = world_map.get_tile(1, 1)
    north = world_map.get_tile(1, 0)
    east = world_map.get_tile(2, 1)
    southwest = world_map.get_tile(0, 2)

    assert origin is not None
    assert north is not None
    assert east is not None
    assert southwest is not None

    origin.altitude = 0.8

    for neighbor in world_map.get_neighbors(origin.x, origin.y):
        neighbor.altitude = 0.7

    north.altitude = 0.5
    east.altitude = 0.3
    southwest.altitude = 0.1

    result = find_lowest_neighbor(world_map, origin)

    assert result is southwest


def test_returns_none_when_no_neighbor_is_lower() -> None:
    world_map = WorldMap(width=3, height=3)

    origin = world_map.get_tile(1, 1)

    assert origin is not None

    origin.altitude = 0.2

    for neighbor in world_map.get_neighbors(origin.x, origin.y):
        neighbor.altitude = 0.5

    result = find_lowest_neighbor(world_map, origin)

    assert result is None


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

    origin.altitude = 0.9
    east.altitude = 0.7
    south.altitude = 0.4
    southeast.altitude = 0.2

    result = find_lowest_neighbor(world_map, origin)

    assert result is southeast