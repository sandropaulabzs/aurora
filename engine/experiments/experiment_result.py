from dataclasses import dataclass

from engine.analysis.world_report import WorldReport


@dataclass(slots=True, frozen=True)
class ExperimentResult:
    """
    Immutable result of a completed Aurora experiment.
    """

    ticks_executed: int
    final_report: WorldReport