from engine.terrain.world_map import WorldMap


def test_world_map_returns_none_outside_bounds() -> None:

    world = WorldMap(10, 10)

    assert world.get_tile(-1, 0) is None
    assert world.get_tile(0, -1) is None
    assert world.get_tile(10, 0) is None
    assert world.get_tile(0, 10) is None


def test_world_map_returns_tile_inside_bounds() -> None:

    world = WorldMap(10, 10)

    tile = world.get_tile(5, 5)

    assert tile is not None
    assert tile.x == 5
    assert tile.y == 5