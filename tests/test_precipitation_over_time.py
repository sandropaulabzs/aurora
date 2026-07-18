from engine.analysis.precipitation_report import (
    PrecipitationAnalyzer,
)
from engine.core.world import World
from engine.systems.world_dynamics_system import (
    WorldDynamicsSystem,
)
from engine.terrain.world_seed import WorldSeed


def test_precipitation_conditions_are_measured_over_time() -> None:
    world = World(
        width=32,
        height=32,
        seed=WorldSeed(123456),
    )

    world.initialize()

    # Esta auditoria avalia a dinâmica atmosférica
    # com uma fonte hídrica explicitamente disponível.
    for row in world.map.tiles:
        for tile in row:
            tile.ground_moisture = 1.0

    system = WorldDynamicsSystem(world)
    analyzer = PrecipitationAnalyzer()

    highest_cloud_water = 0.0
    lowest_threshold = 1.0
    highest_precipitation = 0.0
    maximum_precipitating_tiles = 0

    for _ in range(1000):
        system.update()

        report = analyzer.analyze(
            world.map
        )

        highest_cloud_water = max(
            highest_cloud_water,
            report.maximum_cloud_water,
        )

        lowest_threshold = min(
            lowest_threshold,
            report.minimum_threshold,
        )

        highest_precipitation = max(
            highest_precipitation,
            report.maximum_precipitation,
        )

        maximum_precipitating_tiles = max(
            maximum_precipitating_tiles,
            report.precipitating_tiles,
        )

    assert highest_cloud_water > 0.0
    assert lowest_threshold > 0.0
    assert highest_precipitation >= 0.0
    assert maximum_precipitating_tiles >= 0