import pytest

from engine.hydrology.infiltration import InfiltrationModel
from engine.hydrology.precipitation import PrecipitationModel
from engine.terrain.world_map import WorldMap


def test_precipitation_over_ocean_returns_to_ocean_reservoir() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.is_ocean = True
    tile.ground_moisture = 1.0
    tile.cloud_water = 0.80
    tile.precipitation_threshold = 0.50

    PrecipitationModel().apply(world_map)

    assert tile.cloud_water == pytest.approx(0.50)
    assert tile.ground_moisture == pytest.approx(1.30)
    assert tile.surface_water == pytest.approx(0.0)
    assert tile.precipitation == pytest.approx(0.30)


def test_ocean_tile_does_not_infiltrate() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.is_ocean = True
    tile.surface_water = 0.50
    tile.ground_moisture = 1.0

    InfiltrationModel().apply(world_map)

    assert tile.surface_water == pytest.approx(0.50)
    assert tile.ground_moisture == pytest.approx(1.0)
    assert tile.infiltration == pytest.approx(0.0)