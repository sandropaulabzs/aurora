from engine.experiments.stability_report import (
    StabilityReport,
)


class StabilityReportFormatter:
    """
    Formats the chronological hydrological snapshots
    of a planetary stability experiment.
    """

    def format(
        self,
        report: StabilityReport,
    ) -> str:
        lines: list[str] = []

        lines.append("=" * 94)
        lines.append("AURORA PLANET STABILITY REPORT")
        lines.append("=" * 94)
        lines.append("")

        lines.append(
            "TICK | TOTAL WATER | CLOUD WATER | SURFACE WATER | "
            "RUNOFF | WATER PASSAGE | PRECIPITATING TILES"
        )

        lines.append("-" * 94)

        for snapshot in report.snapshots:
            lines.append(
                f"{snapshot.tick:>4} | "
                f"{snapshot.total_water:>11.6f} | "
                f"{snapshot.maximum_cloud_water:>11.6f} | "
                f"{snapshot.maximum_surface_water:>13.6f} | "
                f"{snapshot.maximum_runoff:>6.6f} | "
                f"{snapshot.maximum_water_passage:>13.6f} | "
                f"{snapshot.precipitating_tiles:>19}"
            )

        lines.append("")
        lines.append("=" * 94)

        return "\n".join(lines)