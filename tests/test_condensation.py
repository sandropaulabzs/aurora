import pytest

from engine.atmosphere.condensation import CondensationModel
from engine.terrain.world_map import WorldMap


def test_excess_vapor_becomes_cloud_water() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.atmospheric_moisture = 0.80
    tile.vapor_capacity = 0.50
    tile.cloud_water = 0.10

    CondensationModel().apply(world_map)

    assert tile.atmospheric_moisture == pytest.approx(0.50)
    assert tile.cloud_water == pytest.approx(0.40)


def test_condensation_conserves_total_atmospheric_water() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.atmospheric_moisture = 0.90
    tile.vapor_capacity = 0.35
    tile.cloud_water = 0.20

    total_before = (
        tile.atmospheric_moisture
        + tile.cloud_water
    )

    CondensationModel().apply(world_map)

    total_after = (
        tile.atmospheric_moisture
        + tile.cloud_water
    )

    assert total_after == pytest.approx(total_before)


def test_no_condensation_below_capacity() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.atmospheric_moisture = 0.30
    tile.vapor_capacity = 0.60
    tile.cloud_water = 0.10

    CondensationModel().apply(world_map)

    assert tile.atmospheric_moisture == pytest.approx(0.30)
    assert tile.cloud_water == pytest.approx(0.10)


def test_no_condensation_at_exact_capacity() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.atmospheric_moisture = 0.50
    tile.vapor_capacity = 0.50

    CondensationModel().apply(world_map)

    assert tile.atmospheric_moisture == pytest.approx(0.50)
    assert tile.cloud_water == pytest.approx(0.0)