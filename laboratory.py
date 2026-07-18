from engine.analysis.hydrological_hotspot_analyzer import (
    HydrologicalHotspotAnalyzer,
)
from engine.core.world import World
from engine.experiments.aurora_laboratory import (
    AuroraLaboratory,
)
from engine.experiments.laboratory_result_formatter import (
    LaboratoryResultFormatter,
)
from engine.terrain.world_seed import WorldSeed


def main() -> None:
    world = World(
        name="Aurora Laboratory World",
        width=32,
        height=32,
        seed=WorldSeed(24680),
    )

    world.initialize()

    laboratory = AuroraLaboratory()

    result = laboratory.run(
        world=world,
        ticks=2000,
    )

    formatted_result = (
        LaboratoryResultFormatter().format(
            result
        )
    )

    print()
    print(formatted_result)
    print()

    hotspot_report = (
        HydrologicalHotspotAnalyzer().analyze(
            world.map
        )
    )

    print("=" * 40)
    print("HYDROLOGICAL HOTSPOT")
    print("=" * 40)
    print()

    print(f"Position: {hotspot_report.position}")
    print(f"Altitude: {hotspot_report.altitude:.6f}")

    print(
        f"Surface water: "
        f"{hotspot_report.surface_water:.6f}"
    )

    print(
        f"Ground moisture: "
        f"{hotspot_report.ground_moisture:.6f}"
    )

    print(
        f"Soil capacity: "
        f"{hotspot_report.soil_capacity:.6f}"
    )

    print(
        f"Soil saturated: "
        f"{hotspot_report.soil_is_saturated}"
    )

    print()

    print(
        f"Infiltration: "
        f"{hotspot_report.infiltration:.6f}"
    )

    print(
        f"Runoff: "
        f"{hotspot_report.runoff:.6f}"
    )

    print(
        f"Water passage: "
        f"{hotspot_report.water_passage:.6f}"
    )

    print()

    print(
        f"Lower neighbors: "
        f"{hotspot_report.lower_neighbors}"
    )

    print(
        "Lowest neighbor altitude: "
        f"{hotspot_report.lowest_neighbor_altitude}"
    )

    print(
        f"Local depression: "
        f"{hotspot_report.is_local_depression}"
    )

    print()


if __name__ == "__main__":
    main()