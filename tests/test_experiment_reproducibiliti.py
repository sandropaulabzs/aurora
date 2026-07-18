from engine.core.world import World
from engine.experiments.experiment_runner import ExperimentRunner
from engine.terrain.world_seed import WorldSeed


def test_same_seed_and_ticks_produce_same_result() -> None:
    first_world = World(
        width=8,
        height=8,
        seed=WorldSeed(987654),
    )

    second_world = World(
        width=8,
        height=8,
        seed=WorldSeed(987654),
    )

    first_world.initialize()
    second_world.initialize()

    runner = ExperimentRunner()

    first_result = runner.run(
        world=first_world,
        ticks=50,
    )

    second_result = runner.run(
        world=second_world,
        ticks=50,
    )

    assert first_result == second_result