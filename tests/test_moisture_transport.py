import pytest

from engine.hydrology.moisture_transport import MoistureTransport
from engine.terrain.world_map import WorldMap


def test_moisture_moves_with_wind() -> None:
    world_map = WorldMap(width=2, height=1)

    origin = world_map.get_tile(0, 0)
    target = world_map.get_tile(1, 0)

    assert origin is not None
    assert target is not None

    origin.atmospheric_moisture = 1.0
    origin.wind_dx = 1
    origin.wind_dy = 0
    origin.wind_speed = 1.0

    MoistureTransport().apply(
        world_map,
        transport_rate=0.25,
    )

    assert origin.atmospheric_moisture == pytest.approx(0.75)
    assert target.atmospheric_moisture == pytest.approx(0.25)


def test_transport_conserves_total_water() -> None:
    world_map = WorldMap(width=2, height=1)

    left = world_map.get_tile(0, 0)
    right = world_map.get_tile(1, 0)

    assert left is not None
    assert right is not None

    left.atmospheric_moisture = 0.8
    left.wind_dx = 1
    left.wind_dy = 0
    left.wind_speed = 0.5

    total_before = (
        left.atmospheric_moisture
        + right.atmospheric_moisture
    )

    MoistureTransport().apply(
        world_map,
        transport_rate=0.20,
    )

    total_after = (
        left.atmospheric_moisture
        + right.atmospheric_moisture
    )

    assert total_after == pytest.approx(total_before)


def test_no_wind_means_no_transport() -> None:
    world_map = WorldMap(width=2, height=1)

    left = world_map.get_tile(0, 0)

    assert left is not None

    left.atmospheric_moisture = 0.9
    left.wind_speed = 0.0

    MoistureTransport().apply(world_map)

    assert left.atmospheric_moisture == pytest.approx(0.9)