from engine.terrain.drainage_map import DrainageMap
from engine.terrain.world_map import WorldMap


def test_generate_creates_flow_map() -> None:
    world_map = WorldMap(width=3, height=3)

    # Inicialmente todas as tiles ficam altas
    for y in range(world_map.height):
        for x in range(world_map.width):
            tile = world_map.get_tile(x, y)
            assert tile is not None
            tile.altitude = 1.0

    origin = world_map.get_tile(1, 1)
    destination = world_map.get_tile(2, 2)

    assert origin is not None
    assert destination is not None

    origin.altitude = 0.8
    destination.altitude = 0.2

    drainage = DrainageMap()

    drainage.generate(world_map)

    assert drainage.destination(1, 1) is destination


def test_destination_returns_none_for_local_minimum() -> None:
    world_map = WorldMap(width=3, height=3)

    for y in range(world_map.height):
        for x in range(world_map.width):
            tile = world_map.get_tile(x, y)
            assert tile is not None
            tile.altitude = 1.0

    center = world_map.get_tile(1, 1)

    assert center is not None

    center.altitude = 0.0

    drainage = DrainageMap()

    drainage.generate(world_map)

    assert drainage.destination(1, 1) is None