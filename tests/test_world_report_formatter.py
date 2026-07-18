from engine.analysis.world_report import WorldReport
from engine.analysis.world_report_formatter import (
    WorldReportFormatter,
)


def test_world_report_formatter_contains_expected_sections() -> None:
    report = WorldReport(
        highest_temperature=42.5,
        highest_temperature_position=(10, 20),
        lowest_pressure=0.215,
        lowest_pressure_position=(3, 7),
        highest_cloud_water=0.125,
        highest_cloud_water_position=(8, 9),
        highest_surface_water=0.075,
        highest_surface_water_position=(4, 5),
        precipitating_tiles=12,
    )

    result = WorldReportFormatter().format(report)

    assert "WORLD SCIENTIFIC REPORT" in result

    assert "HIGHEST TEMPERATURE" in result
    assert "42.50 °C" in result
    assert "Position: (10, 20)" in result

    assert "LOWEST PRESSURE" in result
    assert "0.215" in result
    assert "Position: (3, 7)" in result

    assert "HIGHEST CLOUD WATER" in result
    assert "0.125000" in result
    assert "Position: (8, 9)" in result

    assert "HIGHEST SURFACE WATER" in result
    assert "0.075000" in result
    assert "Position: (4, 5)" in result

    assert "PRECIPITATING TILES" in result
    assert "12" in result