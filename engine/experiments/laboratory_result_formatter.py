from engine.analysis.world_report_formatter import (
    WorldReportFormatter,
)
from engine.experiments.laboratory_result import (
    LaboratoryResult,
)


class LaboratoryResultFormatter:
    """
    Formats the final state and historical telemetry
    of an Aurora laboratory run.
    """

    def __init__(self) -> None:
        self.world_report_formatter = WorldReportFormatter()

    def format(
        self,
        result: LaboratoryResult,
    ) -> str:
        telemetry = result.telemetry

        lines: list[str] = []

        lines.append("=" * 40)
        lines.append("AURORA LABORATORY RESULT")
        lines.append("=" * 40)
        lines.append("")

        lines.append(
            f"Ticks executed: {result.ticks_executed}"
        )

        lines.append("")
        lines.append("-" * 40)
        lines.append("")

        lines.append("HISTORICAL HYDROLOGY MAXIMUMS")
        lines.append("")

        lines.append(
            "Maximum cloud water: "
            f"{telemetry.maximum_cloud_water:.6f}"
        )

        lines.append(
            "Maximum precipitation: "
            f"{telemetry.maximum_precipitation:.6f}"
        )

        lines.append(
            "Maximum surface water: "
            f"{telemetry.maximum_surface_water:.6f}"
        )

        lines.append(
            "Maximum infiltration: "
            f"{telemetry.maximum_infiltration:.6f}"
        )

        lines.append(
            "Maximum runoff: "
            f"{telemetry.maximum_runoff:.6f}"
        )

        lines.append(
            "Maximum water passage: "
            f"{telemetry.maximum_water_passage:.6f}"
        )

        lines.append(
            "Maximum precipitating tiles: "
            f"{telemetry.maximum_precipitating_tiles}"
        )

        lines.append("")
        lines.append(
            self.world_report_formatter.format(
                result.final_report,
            )
        )

        return "\n".join(lines)