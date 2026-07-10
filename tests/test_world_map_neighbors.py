from engine.terrain.world_map import WorldMap


def test_center_tile_has_eight_neighbors() -> None:
    world = WorldMap(3, 3)

    neighbors = world.get_neighbors(1, 1)

    assert len(neighbors) == 8


def test_corner_tile_has_three_neighbors() -> None:
    world = WorldMap(3, 3)

    neighbors = world.get_neighbors(0, 0)

    assert len(neighbors) == 3


def test_neighbors_have_expected_coordinates() -> None:
    world = WorldMap(3, 3)

    neighbors = world.get_neighbors(1, 1)

    coordinates = {
        (tile.x, tile.y)
        for tile in neighbors
    }

    assert coordinates == {
        (0, 0),
        (1, 0),
        (2, 0),
        (0, 1),
        (2, 1),
        (0, 2),
        (1, 2),
        (2, 2),
    }