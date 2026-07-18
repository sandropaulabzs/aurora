import pytest

from engine.core.world import World
from engine.experiments.experiment_runner import ExperimentRunner
from engine.terrain.world_seed import WorldSeed


def test_experiment_runner_executes_requested_ticks() -> None:
    world = World(
        width=8,
        height=8,
        seed=WorldSeed(12345),
    )

    world.initialize()

    result = ExperimentRunner().run(
        world=world,
        ticks=25,
    )

    assert result.ticks_executed == 25


def test_experiment_runner_returns_final_report() -> None:
    world = World(
        width=8,
        height=8,
        seed=WorldSeed(54321),
    )

    world.initialize()

    result = ExperimentRunner().run(
        world=world,
        ticks=10,
    )

    assert result.final_report.highest_temperature_position is not None
    assert result.final_report.lowest_pressure_position is not None


def test_zero_tick_experiment_is_valid() -> None:
    world = World(
        width=4,
        height=4,
        seed=WorldSeed(111),
    )

    world.initialize()

    result = ExperimentRunner().run(
        world=world,
        ticks=0,
    )

    assert result.ticks_executed == 0


def test_negative_ticks_raise_error() -> None:
    world = World(
        width=4,
        height=4,
        seed=WorldSeed(222),
    )

    world.initialize()

    with pytest.raises(ValueError):
        ExperimentRunner().run(
            world=world,
            ticks=-1,
        )