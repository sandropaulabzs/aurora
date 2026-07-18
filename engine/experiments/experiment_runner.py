from collections.abc import Callable

from engine.analysis.world_analyzer import WorldAnalyzer
from engine.core.world import World
from engine.experiments.experiment_result import ExperimentResult
from engine.systems.world_dynamics_system import WorldDynamicsSystem


TickObserver = Callable[[World], None]


class ExperimentRunner:
    """
    Executes a deterministic Aurora experiment
    for a fixed number of simulation ticks.

    An optional observer may inspect the world
    after each completed tick.
    """

    def __init__(self) -> None:
        self.analyzer = WorldAnalyzer()

    def run(
        self,
        world: World,
        ticks: int,
        after_tick: TickObserver | None = None,
    ) -> ExperimentResult:
        if ticks < 0:
            raise ValueError(
                "ticks must be zero or greater"
            )

        system = WorldDynamicsSystem(world)

        for _ in range(ticks):
            system.update()

            if after_tick is not None:
                after_tick(world)

        final_report = self.analyzer.analyze(
            world.map
        )

        return ExperimentResult(
            ticks_executed=ticks,
            final_report=final_report,
        )