import pytest

from engine.terrain.ocean_initializer import OceanInitializer
from engine.terrain.sea_level import SeaLevel
from engine.terrain.world_map import WorldMap


def test_ocean_tiles_receive_ground_water() -> None:
    world_map = WorldMap(width=2, height=1)

    ocean_tile = world_map.get_tile(0, 0)
    land_tile = world_map.get_tile(1, 0)

    assert ocean_tile is not None
    assert land_tile is not None

    ocean_tile.altitude = 0.2
    land_tile.altitude = 0.8

    OceanInitializer().apply(
        world_map,
        SeaLevel(0.5),
    )

    assert ocean_tile.ground_moisture == pytest.approx(1.0)
    assert land_tile.ground_moisture == pytest.approx(0.0)


def test_existing_land_moisture_is_preserved() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.altitude = 0.8
    tile.ground_moisture = 0.35

    OceanInitializer().apply(
        world_map,
        SeaLevel(0.5),
    )

    assert tile.ground_moisture == pytest.approx(0.35)


def test_ocean_initialization_is_idempotent() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.altitude = 0.2

    initializer = OceanInitializer()
    sea_level = SeaLevel(0.5)

    initializer.apply(world_map, sea_level)
    initializer.apply(world_map, sea_level)

    assert tile.ground_moisture == pytest.approx(1.0)