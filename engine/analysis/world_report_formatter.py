from engine.analysis.world_report import WorldReport


class WorldReportFormatter:
    """
    Formats a scientific world report for terminal output.
    """

    def format(
        self,
        report: WorldReport,
    ) -> str:
        lines: list[str] = []

        lines.append("=" * 40)
        lines.append("WORLD SCIENTIFIC REPORT")
        lines.append("=" * 40)
        lines.append("")

        lines.append("HIGHEST TEMPERATURE")
        lines.append(
            f"{report.highest_temperature:.2f} °C"
        )
        lines.append(
            f"Position: {report.highest_temperature_position}"
        )

        lines.append("")
        lines.append("-" * 40)
        lines.append("")

        lines.append("LOWEST PRESSURE")
        lines.append(
            f"{report.lowest_pressure:.3f}"
        )
        lines.append(
            f"Position: {report.lowest_pressure_position}"
        )

        lines.append("")
        lines.append("-" * 40)
        lines.append("")

        lines.append("HIGHEST CLOUD WATER")
        lines.append(
            f"{report.highest_cloud_water:.6f}"
        )
        lines.append(
            f"Position: {report.highest_cloud_water_position}"
        )

        lines.append("")
        lines.append("-" * 40)
        lines.append("")

        lines.append("HIGHEST SURFACE WATER")
        lines.append(
            f"{report.highest_surface_water:.6f}"
        )
        lines.append(
            f"Position: {report.highest_surface_water_position}"
        )

        lines.append("")
        lines.append("-" * 40)
        lines.append("")

        lines.append("PRECIPITATING TILES")
        lines.append(
            str(report.precipitating_tiles)
        )

        lines.append("")
        lines.append("=" * 40)

        return "\n".join(lines)