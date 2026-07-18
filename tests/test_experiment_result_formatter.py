from engine.analysis.world_report import WorldReport
from engine.experiments.experiment_result import (
    ExperimentResult,
)
from engine.experiments.experiment_result_formatter import (
    ExperimentResultFormatter,
)


def test_experiment_result_formatter_contains_expected_data() -> None:
    report = WorldReport(
        highest_temperature=41.25,
        highest_temperature_position=(4, 7),
        lowest_pressure=0.215,
        lowest_pressure_position=(2, 3),
        highest_cloud_water=0.125,
        highest_cloud_water_position=(8, 9),
        highest_surface_water=0.075,
        highest_surface_water_position=(5, 6),
        precipitating_tiles=3,
    )

    result = ExperimentResult(
        ticks_executed=500,
        final_report=report,
    )

    formatted = ExperimentResultFormatter().format(
        result
    )

    assert "AURORA EXPERIMENT RESULT" in formatted
    assert "Ticks executed: 500" in formatted

    assert "WORLD SCIENTIFIC REPORT" in formatted
    assert "41.25 °C" in formatted
    assert "Position: (4, 7)" in formatted
    assert "0.215" in formatted
    assert "PRECIPITATING TILES" in formatted
    assert "3" in formatted