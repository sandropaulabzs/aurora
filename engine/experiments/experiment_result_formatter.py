from engine.analysis.world_report_formatter import (
    WorldReportFormatter,
)
from engine.experiments.experiment_result import (
    ExperimentResult,
)


class ExperimentResultFormatter:
    """
    Formats the final result of an Aurora experiment.

    This class presents data only. It does not execute
    experiments or modify the simulated world.
    """

    def __init__(self) -> None:
        self.world_report_formatter = WorldReportFormatter()

    def format(
        self,
        result: ExperimentResult,
    ) -> str:
        lines: list[str] = []

        lines.append("=" * 40)
        lines.append("AURORA EXPERIMENT RESULT")
        lines.append("=" * 40)
        lines.append("")

        lines.append(
            f"Ticks executed: {result.ticks_executed}"
        )

        lines.append("")
        lines.append(
            self.world_report_formatter.format(
                result.final_report,
            )
        )

        return "\n".join(lines)