import pytest

from engine.atmosphere.wind_model import WindModel
from engine.terrain.world_map import WorldMap


def test_wind_moves_toward_lower_pressure() -> None:
    world_map = WorldMap(width=3, height=3)

    origin = world_map.get_tile(1, 1)
    target = world_map.get_tile(2, 0)

    assert origin is not None
    assert target is not None

    origin.pressure = 0.8

    for neighbor in world_map.get_neighbors(
        origin.x,
        origin.y,
    ):
        neighbor.pressure = 0.7

    target.pressure = 0.2

    wind = WindModel().calculate(
        world_map,
        origin,
    )

    assert wind.dx == 1
    assert wind.dy == -1
    assert wind.speed == pytest.approx(0.6)


def test_wind_is_calm_when_no_neighbor_has_lower_pressure() -> None:
    world_map = WorldMap(width=3, height=3)

    origin = world_map.get_tile(1, 1)

    assert origin is not None

    origin.pressure = 0.2

    for neighbor in world_map.get_neighbors(
        origin.x,
        origin.y,
    ):
        neighbor.pressure = 0.5

    wind = WindModel().calculate(
        world_map,
        origin,
    )

    assert wind.dx == 0
    assert wind.dy == 0
    assert wind.speed == pytest.approx(0.0)


def test_wind_speed_is_limited_to_one() -> None:
    world_map = WorldMap(width=2, height=1)

    origin = world_map.get_tile(0, 0)
    target = world_map.get_tile(1, 0)

    assert origin is not None
    assert target is not None

    origin.pressure = 2.0
    target.pressure = 0.0

    wind = WindModel().calculate(
        world_map,
        origin,
    )

    assert wind.speed == pytest.approx(1.0)