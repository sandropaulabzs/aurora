import pytest

from engine.hydrology.evaporation import EvaporationModel
from engine.terrain.world_map import WorldMap


def test_hotter_tile_evaporates_more() -> None:
    world_map = WorldMap(width=2, height=1)

    cold = world_map.get_tile(0, 0)
    hot = world_map.get_tile(1, 0)

    assert cold is not None
    assert hot is not None

    cold.temperature = 0.0
    hot.temperature = 40.0

    cold.ground_moisture = 1.0
    hot.ground_moisture = 1.0

    EvaporationModel().apply(world_map)

    assert hot.evaporation > cold.evaporation


def test_dry_tile_does_not_evaporate() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.temperature = 50.0
    tile.ground_moisture = 0.0

    EvaporationModel().apply(world_map)

    assert tile.evaporation == pytest.approx(0.0)


def test_evaporation_is_normalized() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.temperature = 100.0
    tile.ground_moisture = 10.0

    EvaporationModel().apply(world_map)

    assert 0.0 <= tile.evaporation <= 1.0