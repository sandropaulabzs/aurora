import pytest

from engine.experiments.experiment_telemetry import (
    ExperimentTelemetry,
)
from engine.experiments.telemetry_collector import (
    TelemetryCollector,
)
from engine.terrain.world_map import WorldMap


def test_telemetry_collector_records_current_maximum_values() -> None:
    world_map = WorldMap(width=2, height=1)

    first = world_map.get_tile(0, 0)
    second = world_map.get_tile(1, 0)

    assert first is not None
    assert second is not None

    first.cloud_water = 0.20
    first.precipitation = 0.05
    first.surface_water = 0.10
    first.infiltration = 0.03
    first.runoff = 0.02
    first.water_passage = 1.50

    second.cloud_water = 0.40
    second.precipitation = 0.08
    second.surface_water = 0.25
    second.infiltration = 0.06
    second.runoff = 0.04
    second.water_passage = 2.00

    telemetry = ExperimentTelemetry()

    TelemetryCollector().collect(
        world_map,
        telemetry,
    )

    assert telemetry.maximum_cloud_water == pytest.approx(0.40)
    assert telemetry.maximum_precipitation == pytest.approx(0.08)
    assert telemetry.maximum_surface_water == pytest.approx(0.25)
    assert telemetry.maximum_infiltration == pytest.approx(0.06)
    assert telemetry.maximum_runoff == pytest.approx(0.04)
    assert telemetry.maximum_water_passage == pytest.approx(2.00)


def test_telemetry_collector_preserves_historical_maximums() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    telemetry = ExperimentTelemetry(
        maximum_cloud_water=0.90,
        maximum_precipitation=0.70,
        maximum_surface_water=0.60,
        maximum_infiltration=0.50,
        maximum_runoff=0.40,
        maximum_water_passage=10.0,
        maximum_precipitating_tiles=3,
    )

    tile.cloud_water = 0.10
    tile.precipitation = 0.05
    tile.surface_water = 0.02
    tile.infiltration = 0.01
    tile.runoff = 0.005
    tile.water_passage = 1.0

    TelemetryCollector().collect(
        world_map,
        telemetry,
    )

    assert telemetry.maximum_cloud_water == pytest.approx(0.90)
    assert telemetry.maximum_precipitation == pytest.approx(0.70)
    assert telemetry.maximum_surface_water == pytest.approx(0.60)
    assert telemetry.maximum_infiltration == pytest.approx(0.50)
    assert telemetry.maximum_runoff == pytest.approx(0.40)
    assert telemetry.maximum_water_passage == pytest.approx(10.0)
    assert telemetry.maximum_precipitating_tiles == 3


def test_telemetry_collector_counts_precipitating_tiles() -> None:
    world_map = WorldMap(width=3, height=1)

    first = world_map.get_tile(0, 0)
    second = world_map.get_tile(1, 0)
    third = world_map.get_tile(2, 0)

    assert first is not None
    assert second is not None
    assert third is not None

    first.precipitation = 0.10
    second.precipitation = 0.00
    third.precipitation = 0.05

    telemetry = ExperimentTelemetry()

    TelemetryCollector().collect(
        world_map,
        telemetry,
    )

    assert telemetry.maximum_precipitating_tiles == 2


def test_telemetry_collector_rejects_empty_world_map() -> None:
    world_map = WorldMap(width=0, height=0)

    telemetry = ExperimentTelemetry()

    with pytest.raises(ValueError):
        TelemetryCollector().collect(
            world_map,
            telemetry,
        )