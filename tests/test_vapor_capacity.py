import pytest

from engine.atmosphere.vapor_capacity import VaporCapacityModel
from engine.terrain.world_map import WorldMap


def test_hot_air_holds_more_vapor() -> None:
    world_map = WorldMap(width=2, height=1)

    cold = world_map.get_tile(0, 0)
    hot = world_map.get_tile(1, 0)

    assert cold is not None
    assert hot is not None

    cold.temperature = 0.0
    hot.temperature = 40.0

    VaporCapacityModel().apply(world_map)

    assert hot.vapor_capacity > cold.vapor_capacity


def test_capacity_is_normalized() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.temperature = 150.0

    VaporCapacityModel().apply(world_map)

    assert tile.vapor_capacity == pytest.approx(1.0)


def test_negative_temperature_is_clamped() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.temperature = -100.0

    VaporCapacityModel().apply(world_map)

    assert tile.vapor_capacity == pytest.approx(0.0)