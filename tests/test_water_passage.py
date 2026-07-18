import pytest

from engine.hydrology.water_passage import WaterPassageModel
from engine.terrain.world_map import WorldMap


def test_water_passage_accumulates_runoff() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.runoff = 0.20
    tile.water_passage = 0.50

    WaterPassageModel().apply(world_map)

    assert tile.water_passage == pytest.approx(0.70)


def test_water_passage_preserves_history_across_ticks() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    model = WaterPassageModel()

    tile.runoff = 0.10
    model.apply(world_map)

    tile.runoff = 0.25
    model.apply(world_map)

    assert tile.water_passage == pytest.approx(0.35)


def test_no_runoff_does_not_change_water_passage() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.runoff = 0.0
    tile.water_passage = 0.40

    WaterPassageModel().apply(world_map)

    assert tile.water_passage == pytest.approx(0.40)