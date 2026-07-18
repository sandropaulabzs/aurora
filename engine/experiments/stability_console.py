from engine.core.world import World
from engine.experiments.planet_stability_experiment import (
    PlanetStabilityExperiment,
)
from engine.experiments.stability_report_formatter import (
    StabilityReportFormatter,
)


class StabilityConsole:
    """
    Executes a planetary stability experiment and
    returns a formatted chronological report.
    """

    def __init__(self) -> None:
        self.experiment = (
            PlanetStabilityExperiment()
        )
        self.formatter = (
            StabilityReportFormatter()
        )

    def run(
        self,
        world: World,
        ticks: int,
        snapshot_interval: int,
    ) -> str:
        report = self.experiment.run(
            world=world,
            ticks=ticks,
            snapshot_interval=snapshot_interval,
        )

        return self.formatter.format(
            report,
        )