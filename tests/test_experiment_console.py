from engine.core.world import World
from engine.experiments.experiment_console import (
    ExperimentConsole,
)
from engine.terrain.world_seed import WorldSeed


def test_experiment_console_returns_formatted_result() -> None:
    world = World(
        width=8,
        height=8,
        seed=WorldSeed(24680),
    )

    world.initialize()

    result = ExperimentConsole().run(
        world=world,
        ticks=25,
    )

    assert "AURORA EXPERIMENT RESULT" in result
    assert "Ticks executed: 25" in result
    assert "WORLD SCIENTIFIC REPORT" in result
    assert "HIGHEST TEMPERATURE" in result
    assert "LOWEST PRESSURE" in result


def test_experiment_console_accepts_zero_ticks() -> None:
    world = World(
        width=4,
        height=4,
        seed=WorldSeed(13579),
    )

    world.initialize()

    result = ExperimentConsole().run(
        world=world,
        ticks=0,
    )

    assert "Ticks executed: 0" in result