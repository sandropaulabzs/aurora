from engine.experiments.stability_report import (
    StabilityReport,
)
from engine.experiments.stability_report_formatter import (
    StabilityReportFormatter,
)
from engine.experiments.stability_snapshot import (
    StabilitySnapshot,
)


def test_stability_report_formatter_contains_expected_data() -> None:
    report = StabilityReport(
        snapshots=(
            StabilitySnapshot(
                tick=0,
                total_water=100.0,
                maximum_cloud_water=0.0,
                maximum_surface_water=0.0,
                maximum_runoff=0.0,
                maximum_water_passage=0.0,
                precipitating_tiles=0,
            ),
            StabilitySnapshot(
                tick=100,
                total_water=100.0,
                maximum_cloud_water=0.425,
                maximum_surface_water=0.075,
                maximum_runoff=0.020,
                maximum_water_passage=1.500,
                precipitating_tiles=12,
            ),
        )
    )

    formatted = StabilityReportFormatter().format(
        report
    )

    assert "AURORA PLANET STABILITY REPORT" in formatted

    assert (
        "TICK | TOTAL WATER | CLOUD WATER | SURFACE WATER | "
        "RUNOFF | WATER PASSAGE | PRECIPITATING TILES"
        in formatted
    )

    assert "100.000000" in formatted
    assert "0.425000" in formatted
    assert "0.075000" in formatted
    assert "0.020000" in formatted
    assert "1.500000" in formatted
    assert "12" in formatted


def test_empty_stability_report_still_formats() -> None:
    report = StabilityReport(
        snapshots=()
    )

    formatted = StabilityReportFormatter().format(
        report
    )

    assert "AURORA PLANET STABILITY REPORT" in formatted
    assert "TICK | TOTAL WATER" in formatted