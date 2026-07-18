from engine.analysis.world_report import WorldReport
from engine.experiments.experiment_telemetry import (
    ExperimentTelemetry,
)
from engine.experiments.laboratory_result import (
    LaboratoryResult,
)
from engine.experiments.laboratory_result_formatter import (
    LaboratoryResultFormatter,
)


def test_laboratory_result_formatter_contains_expected_data() -> None:
    report = WorldReport(
        highest_temperature=42.50,
        highest_temperature_position=(4, 7),
        lowest_pressure=0.215,
        lowest_pressure_position=(2, 3),
        highest_cloud_water=0.125,
        highest_cloud_water_position=(8, 9),
        highest_surface_water=0.075,
        highest_surface_water_position=(5, 6),
        precipitating_tiles=3,
    )

    telemetry = ExperimentTelemetry(
        maximum_cloud_water=0.325,
        maximum_precipitation=0.125,
        maximum_surface_water=0.090,
        maximum_infiltration=0.040,
        maximum_runoff=0.025,
        maximum_water_passage=2.500,
        maximum_precipitating_tiles=12,
    )

    result = LaboratoryResult(
        ticks_executed=5000,
        final_report=report,
        telemetry=telemetry,
    )

    formatted = LaboratoryResultFormatter().format(
        result
    )

    assert "AURORA LABORATORY RESULT" in formatted
    assert "Ticks executed: 5000" in formatted

    assert "HISTORICAL HYDROLOGY MAXIMUMS" in formatted

    assert "Maximum cloud water: 0.325000" in formatted
    assert "Maximum precipitation: 0.125000" in formatted
    assert "Maximum surface water: 0.090000" in formatted
    assert "Maximum infiltration: 0.040000" in formatted
    assert "Maximum runoff: 0.025000" in formatted
    assert "Maximum water passage: 2.500000" in formatted
    assert "Maximum precipitating tiles: 12" in formatted

    assert "WORLD SCIENTIFIC REPORT" in formatted
    assert "42.50 °C" in formatted
    assert "PRECIPITATING TILES" in formatted