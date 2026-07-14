from engine.terrain.ocean_mask import OceanMask
from engine.terrain.sea_level import SeaLevel
from engine.terrain.world_map import WorldMap


def test_ocean_mask_generates_expected_map() -> None:
    world_map = WorldMap(width=2, height=2)

    top_left = world_map.get_tile(0, 0)
    top_right = world_map.get_tile(1, 0)
    bottom_left = world_map.get_tile(0, 1)
    bottom_right = world_map.get_tile(1, 1)

    assert top_left is not None
    assert top_right is not None
    assert bottom_left is not None
    assert bottom_right is not None

    top_left.altitude = 0.2
    top_right.altitude = 0.8
    bottom_left.altitude = 0.4
    bottom_right.altitude = 0.6

    sea_level = SeaLevel(0.5)

    mask = OceanMask().generate(
        world_map,
        sea_level,
    )

    assert mask == [
        [True, False],
        [True, False],
    ]


def test_all_tiles_are_land_when_sea_level_is_zero() -> None:
    world_map = WorldMap(width=2, height=1)

    for row in world_map.tiles:
        for tile in row:
            tile.altitude = 0.5

    mask = OceanMask().generate(
        world_map,
        SeaLevel(0.0),
    )

    assert mask == [
        [False, False],
    ]


def test_all_tiles_are_ocean_when_sea_level_is_one() -> None:
    world_map = WorldMap(width=2, height=1)

    for row in world_map.tiles:
        for tile in row:
            tile.altitude = 0.5

    mask = OceanMask().generate(
        world_map,
        SeaLevel(1.0),
    )

    assert mask == [
        [True, True],
    ]