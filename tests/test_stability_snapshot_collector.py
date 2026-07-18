import pytest

from engine.experiments.stability_snapshot_collector import (
    StabilitySnapshotCollector,
)
from engine.terrain.world_map import WorldMap


def test_snapshot_collector_captures_current_hydrology() -> None:
    world_map = WorldMap(width=3, height=1)

    first = world_map.get_tile(0, 0)
    second = world_map.get_tile(1, 0)
    third = world_map.get_tile(2, 0)

    assert first is not None
    assert second is not None
    assert third is not None

    first.cloud_water = 0.10
    first.surface_water = 0.20
    first.runoff = 0.01
    first.water_passage = 1.00
    first.precipitation = 0.00

    second.cloud_water = 0.40
    second.surface_water = 0.15
    second.runoff = 0.05
    second.water_passage = 2.50
    second.precipitation = 0.03

    third.cloud_water = 0.25
    third.surface_water = 0.60
    third.runoff = 0.02
    third.water_passage = 1.75
    third.precipitation = 0.01

    snapshot = StabilitySnapshotCollector().collect(
        world_map=world_map,
        tick=250,
    )

    assert snapshot.tick == 250
    assert snapshot.maximum_cloud_water == pytest.approx(0.40)
    assert snapshot.maximum_surface_water == pytest.approx(0.60)
    assert snapshot.maximum_runoff == pytest.approx(0.05)
    assert snapshot.maximum_water_passage == pytest.approx(2.50)
    assert snapshot.precipitating_tiles == 2


def test_snapshot_collector_rejects_negative_tick() -> None:
    world_map = WorldMap(width=1, height=1)

    with pytest.raises(ValueError):
        StabilitySnapshotCollector().collect(
            world_map=world_map,
            tick=-1,
        )


def test_snapshot_collector_rejects_empty_world_map() -> None:
    world_map = WorldMap(width=0, height=0)

    with pytest.raises(ValueError):
        StabilitySnapshotCollector().collect(
            world_map=world_map,
            tick=0,
        )