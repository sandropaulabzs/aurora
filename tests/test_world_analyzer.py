import pytest

from engine.analysis.world_analyzer import WorldAnalyzer
from engine.terrain.world_map import WorldMap


def test_world_analyzer_collects_expected_metrics() -> None:
    world_map = WorldMap(width=3, height=1)

    first = world_map.get_tile(0, 0)
    second = world_map.get_tile(1, 0)
    third = world_map.get_tile(2, 0)

    assert first is not None
    assert second is not None
    assert third is not None

    first.temperature = 10.0
    first.pressure = 0.70
    first.cloud_water = 0.10
    first.surface_water = 0.05
    first.precipitation = 0.00

    second.temperature = 35.0
    second.pressure = 0.40
    second.cloud_water = 0.30
    second.surface_water = 0.15
    second.precipitation = 0.04

    third.temperature = 20.0
    third.pressure = 0.20
    third.cloud_water = 0.25
    third.surface_water = 0.50
    third.precipitation = 0.02

    report = WorldAnalyzer().analyze(world_map)

    assert report.highest_temperature == pytest.approx(35.0)
    assert report.highest_temperature_position == (1, 0)

    assert report.lowest_pressure == pytest.approx(0.20)
    assert report.lowest_pressure_position == (2, 0)

    assert report.highest_cloud_water == pytest.approx(0.30)
    assert report.highest_cloud_water_position == (1, 0)

    assert report.highest_surface_water == pytest.approx(0.50)
    assert report.highest_surface_water_position == (2, 0)

    assert report.precipitating_tiles == 2


def test_world_analyzer_raises_error_for_empty_map() -> None:
    world_map = WorldMap(width=0, height=0)

    with pytest.raises(ValueError):
        WorldAnalyzer().analyze(world_map)