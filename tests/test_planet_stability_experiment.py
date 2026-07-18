import pytest

from engine.core.world import World
from engine.experiments.planet_stability_experiment import (
    PlanetStabilityExperiment,
)
from engine.terrain.world_seed import WorldSeed


def test_stability_experiment_collects_expected_ticks() -> None:
    world = World(
        width=4,
        height=4,
        seed=WorldSeed(12345),
    )

    world.initialize()

    report = PlanetStabilityExperiment().run(
        world=world,
        ticks=250,
        snapshot_interval=100,
    )

    collected_ticks = tuple(
        snapshot.tick
        for snapshot in report.snapshots
    )

    assert collected_ticks == (
        0,
        100,
        200,
        250,
    )


def test_stability_experiment_collects_final_tick_once() -> None:
    world = World(
        width=4,
        height=4,
        seed=WorldSeed(54321),
    )

    world.initialize()

    report = PlanetStabilityExperiment().run(
        world=world,
        ticks=200,
        snapshot_interval=100,
    )

    collected_ticks = tuple(
        snapshot.tick
        for snapshot in report.snapshots
    )

    assert collected_ticks == (
        0,
        100,
        200,
    )


def test_zero_tick_experiment_contains_only_initial_snapshot() -> None:
    world = World(
        width=4,
        height=4,
        seed=WorldSeed(111),
    )

    world.initialize()

    report = PlanetStabilityExperiment().run(
        world=world,
        ticks=0,
        snapshot_interval=100,
    )

    assert len(report.snapshots) == 1
    assert report.snapshots[0].tick == 0


@pytest.mark.parametrize(
    "invalid_interval",
    [0, -1],
)
def test_invalid_snapshot_interval_raises_error(
    invalid_interval: int,
) -> None:
    world = World(
        width=4,
        height=4,
        seed=WorldSeed(222),
    )

    world.initialize()

    with pytest.raises(ValueError):
        PlanetStabilityExperiment().run(
            world=world,
            ticks=100,
            snapshot_interval=invalid_interval,
        )