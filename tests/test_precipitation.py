import pytest

from engine.hydrology.precipitation import PrecipitationModel
from engine.terrain.world_map import WorldMap


def test_excess_cloud_water_becomes_surface_water() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.cloud_water = 0.80
    tile.precipitation_threshold = 0.50
    tile.surface_water = 0.20

    PrecipitationModel().apply(world_map)

    assert tile.cloud_water == pytest.approx(0.50)
    assert tile.surface_water == pytest.approx(0.50)


def test_precipitation_conserves_total_water() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.cloud_water = 0.90
    tile.surface_water = 0.10
    tile.precipitation_threshold = 0.40

    total_before = (
        tile.cloud_water
        + tile.surface_water
    )

    PrecipitationModel().apply(world_map)

    total_after = (
        tile.cloud_water
        + tile.surface_water
    )

    assert total_after == pytest.approx(total_before)


def test_precipitation_records_current_tick_amount() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.cloud_water = 0.85
    tile.precipitation_threshold = 0.55

    PrecipitationModel().apply(world_map)

    assert tile.precipitation == pytest.approx(0.30)


def test_no_precipitation_below_threshold() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.cloud_water = 0.30
    tile.precipitation_threshold = 0.60
    tile.surface_water = 0.10
    tile.precipitation = 0.25

    PrecipitationModel().apply(world_map)

    assert tile.cloud_water == pytest.approx(0.30)
    assert tile.surface_water == pytest.approx(0.10)
    assert tile.precipitation == pytest.approx(0.0)


def test_no_precipitation_at_exact_threshold() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.cloud_water = 0.50
    tile.precipitation_threshold = 0.50
    tile.surface_water = 0.25

    PrecipitationModel().apply(world_map)

    assert tile.cloud_water == pytest.approx(0.50)
    assert tile.surface_water == pytest.approx(0.25)
    assert tile.precipitation == pytest.approx(0.0)