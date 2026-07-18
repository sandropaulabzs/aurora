from engine.core.world import World
from engine.experiments.experiment_runner import (
    ExperimentRunner,
)
from engine.experiments.experiment_telemetry import (
    ExperimentTelemetry,
)
from engine.experiments.laboratory_result import (
    LaboratoryResult,
)
from engine.experiments.telemetry_collector import (
    TelemetryCollector,
)


class AuroraLaboratory:
    """
    Executes controlled Aurora experiments while
    collecting historical scientific telemetry.
    """

    def __init__(self) -> None:
        self.runner = ExperimentRunner()
        self.collector = TelemetryCollector()

    def run(
        self,
        world: World,
        ticks: int,
    ) -> LaboratoryResult:
        telemetry = ExperimentTelemetry()

        def collect_after_tick(
            observed_world: World,
        ) -> None:
            self.collector.collect(
                world_map=observed_world.map,
                telemetry=telemetry,
            )

        experiment_result = self.runner.run(
            world=world,
            ticks=ticks,
            after_tick=collect_after_tick,
        )

        return LaboratoryResult(
            ticks_executed=(
                experiment_result.ticks_executed
            ),
            final_report=(
                experiment_result.final_report
            ),
            telemetry=telemetry,
        )