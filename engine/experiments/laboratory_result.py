from dataclasses import dataclass

from engine.analysis.world_report import WorldReport
from engine.experiments.experiment_telemetry import (
    ExperimentTelemetry,
)


@dataclass(slots=True, frozen=True)
class LaboratoryResult:
    """
    Immutable result of an Aurora laboratory run.

    It contains the final world state report and the
    historical maximums observed during the experiment.
    """

    ticks_executed: int
    final_report: WorldReport
    telemetry: ExperimentTelemetry