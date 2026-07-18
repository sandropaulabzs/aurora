import pytest

from engine.analysis.hydrological_hotspot_analyzer import (
    HydrologicalHotspotAnalyzer,
)
from engine.terrain.world_map import WorldMap


def test_hotspot_analyzer_finds_greatest_surface_water() -> None:
    world_map = WorldMap(width=3, height=1)

    first = world_map.get_tile(0, 0)
    second = world_map.get_tile(1, 0)
    third = world_map.get_tile(2, 0)

    assert first is not None
    assert second is not None
    assert third is not None

    first.surface_water = 0.50
    second.surface_water = 2.00
    third.surface_water = 1.25

    second.altitude = 0.40
    second.ground_moisture = 1.00
    second.soil_capacity = 1.00
    second.infiltration = 0.00
    second.runoff = 0.10
    second.water_passage = 4.50

    report = HydrologicalHotspotAnalyzer().analyze(
        world_map
    )

    assert report.position == (1, 0)
    assert report.surface_water == pytest.approx(2.00)
    assert report.altitude == pytest.approx(0.40)
    assert report.ground_moisture == pytest.approx(1.00)
    assert report.soil_capacity == pytest.approx(1.00)
    assert report.infiltration == pytest.approx(0.00)
    assert report.runoff == pytest.approx(0.10)
    assert report.water_passage == pytest.approx(4.50)
    assert report.soil_is_saturated is True


def test_hotspot_analyzer_detects_local_depression() -> None:
    world_map = WorldMap(width=3, height=1)

    left = world_map.get_tile(0, 0)
    center = world_map.get_tile(1, 0)
    right = world_map.get_tile(2, 0)

    assert left is not None
    assert center is not None
    assert right is not None

    left.altitude = 0.80
    center.altitude = 0.20
    right.altitude = 0.60

    center.surface_water = 3.00

    report = HydrologicalHotspotAnalyzer().analyze(
        world_map
    )

    assert report.position == (1, 0)
    assert report.lower_neighbors == 0
    assert report.lowest_neighbor_altitude == pytest.approx(
        0.60
    )
    assert report.is_local_depression is True


def test_hotspot_analyzer_detects_available_downhill_exit() -> None:
    world_map = WorldMap(width=3, height=1)

    left = world_map.get_tile(0, 0)
    center = world_map.get_tile(1, 0)
    right = world_map.get_tile(2, 0)

    assert left is not None
    assert center is not None
    assert right is not None

    left.altitude = 0.70
    center.altitude = 0.50
    right.altitude = 0.10

    center.surface_water = 3.00

    report = HydrologicalHotspotAnalyzer().analyze(
        world_map
    )

    assert report.lower_neighbors == 1
    assert report.lowest_neighbor_altitude == pytest.approx(
        0.10
    )
    assert report.is_local_depression is False


def test_empty_world_map_raises_error() -> None:
    world_map = WorldMap(width=0, height=0)

    with pytest.raises(ValueError):
        HydrologicalHotspotAnalyzer().analyze(
            world_map
        )