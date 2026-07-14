import pytest

from engine.atmosphere.wind_field import WindField
from engine.terrain.world_map import WorldMap


def test_wind_field_applies_wind_to_all_tiles() -> None:
    world_map = WorldMap(width=3, height=3)

    for row in world_map.tiles:
        for tile in row:
            tile.pressure = 0.8

    target = world_map.get_tile(2, 2)

    assert target is not None

    target.pressure = 0.2

    WindField().apply(world_map)

    origin = world_map.get_tile(1, 1)

    assert origin is not None

    assert origin.wind_dx == 1
    assert origin.wind_dy == 1
    assert origin.wind_speed == pytest.approx(0.6)


def test_wind_field_creates_calm_air_at_local_pressure_minimum() -> None:
    world_map = WorldMap(width=3, height=3)

    for row in world_map.tiles:
        for tile in row:
            tile.pressure = 0.8

    center = world_map.get_tile(1, 1)

    assert center is not None

    center.pressure = 0.1

    WindField().apply(world_map)

    assert center.wind_dx == 0
    assert center.wind_dy == 0
    assert center.wind_speed == pytest.approx(0.0)