import pytest

from engine.analysis.precipitation_report import (
    PrecipitationAnalyzer,
)
from engine.terrain.world_map import WorldMap


def test_precipitation_analyzer_collects_expected_metrics() -> None:
    world_map = WorldMap(width=3, height=1)

    first = world_map.get_tile(0, 0)
    second = world_map.get_tile(1, 0)
    third = world_map.get_tile(2, 0)

    assert first is not None
    assert second is not None
    assert third is not None

    first.cloud_water = 0.10
    first.precipitation_threshold = 0.40
    first.precipitation = 0.00

    second.cloud_water = 0.35
    second.precipitation_threshold = 0.30
    second.precipitation = 0.05

    third.cloud_water = 0.25
    third.precipitation_threshold = 0.50
    third.precipitation = 0.02

    report = PrecipitationAnalyzer().analyze(
        world_map
    )

    assert report.maximum_cloud_water == pytest.approx(0.35)
    assert report.minimum_threshold == pytest.approx(0.30)
    assert report.maximum_precipitation == pytest.approx(0.05)
    assert report.precipitating_tiles == 2


def test_threshold_gap_is_calculated() -> None:
    world_map = WorldMap(width=2, height=1)

    first = world_map.get_tile(0, 0)
    second = world_map.get_tile(1, 0)

    assert first is not None
    assert second is not None

    first.cloud_water = 0.20
    first.precipitation_threshold = 0.50

    second.cloud_water = 0.40
    second.precipitation_threshold = 0.30

    report = PrecipitationAnalyzer().analyze(
        world_map
    )

    assert report.threshold_gap == pytest.approx(-0.10)


def test_empty_world_map_raises_error() -> None:
    world_map = WorldMap(width=0, height=0)

    with pytest.raises(ValueError):
        PrecipitationAnalyzer().analyze(
            world_map
        )