import pytest

from engine.analysis.water_passage_report import (
    WaterPassageAnalyzer,
)
from engine.terrain.world_map import WorldMap


def test_water_passage_analyzer_collects_expected_metrics() -> None:
    world_map = WorldMap(width=3, height=1)

    first = world_map.get_tile(0, 0)
    second = world_map.get_tile(1, 0)
    third = world_map.get_tile(2, 0)

    assert first is not None
    assert second is not None
    assert third is not None

    first.water_passage = 0.0
    second.water_passage = 2.5
    third.water_passage = 1.0

    report = WaterPassageAnalyzer().analyze(
        world_map
    )

    assert report.maximum_passage == pytest.approx(2.5)
    assert report.maximum_position == (1, 0)
    assert report.active_tiles == 2
    assert report.total_passage == pytest.approx(3.5)


def test_empty_world_map_raises_error() -> None:
    world_map = WorldMap(width=0, height=0)

    with pytest.raises(ValueError):
        WaterPassageAnalyzer().analyze(
            world_map
        )