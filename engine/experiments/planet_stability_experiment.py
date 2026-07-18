from engine.core.world import World
from engine.experiments.experiment_runner import (
    ExperimentRunner,
)
from engine.experiments.stability_report import (
    StabilityReport,
)
from engine.experiments.stability_snapshot import (
    StabilitySnapshot,
)
from engine.experiments.stability_snapshot_collector import (
    StabilitySnapshotCollector,
)


class PlanetStabilityExperiment:
    """
    Executes a long-running planetary experiment
    and records hydrological snapshots over time.
    """

    def __init__(self) -> None:
        self.runner = ExperimentRunner()
        self.collector = StabilitySnapshotCollector()

    def run(
        self,
        world: World,
        ticks: int,
        snapshot_interval: int,
    ) -> StabilityReport:
        if snapshot_interval <= 0:
            raise ValueError(
                "snapshot_interval must be greater than zero"
            )

        snapshots: list[StabilitySnapshot] = []

        snapshots.append(
            self.collector.collect(
                world_map=world.map,
                tick=0,
            )
        )

        current_tick = 0

        def collect_after_tick(
            observed_world: World,
        ) -> None:
            nonlocal current_tick

            current_tick += 1

            should_collect = (
                current_tick % snapshot_interval == 0
                or current_tick == ticks
            )

            if not should_collect:
                return

            snapshots.append(
                self.collector.collect(
                    world_map=observed_world.map,
                    tick=current_tick,
                )
            )

        self.runner.run(
            world=world,
            ticks=ticks,
            after_tick=collect_after_tick,
        )

        return StabilityReport(
            snapshots=tuple(snapshots),
        )