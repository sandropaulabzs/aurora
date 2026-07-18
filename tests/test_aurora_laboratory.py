from engine.core.world import World
from engine.experiments.aurora_laboratory import (
    AuroraLaboratory,
)
from engine.terrain.world_seed import WorldSeed


def test_laboratory_executes_requested_ticks() -> None:
    world = World(
        width=8,
        height=8,
        seed=WorldSeed(24680),
    )

    world.initialize()

    result = AuroraLaboratory().run(
        world=world,
        ticks=25,
    )

    assert result.ticks_executed == 25


def test_laboratory_collects_historical_telemetry() -> None:
    world = World(
        width=8,
        height=8,
        seed=WorldSeed(13579),
    )

    world.initialize()

    # Garante uma fonte hídrica para o experimento,
    # sem depender de a seed gerar oceanos.
    for row in world.map.tiles:
        for tile in row:
            tile.ground_moisture = 1.0

    result = AuroraLaboratory().run(
        world=world,
        ticks=100,
    )

    assert result.telemetry.maximum_cloud_water >= 0.0
    assert result.telemetry.maximum_precipitation >= 0.0
    assert result.telemetry.maximum_surface_water >= 0.0
    assert result.telemetry.maximum_infiltration >= 0.0
    assert result.telemetry.maximum_runoff >= 0.0
    assert result.telemetry.maximum_water_passage >= 0.0
    assert result.telemetry.maximum_precipitating_tiles >= 0


def test_zero_tick_laboratory_run_keeps_empty_telemetry() -> None:
    world = World(
        width=4,
        height=4,
        seed=WorldSeed(111),
    )

    world.initialize()

    result = AuroraLaboratory().run(
        world=world,
        ticks=0,
    )

    assert result.ticks_executed == 0

    assert result.telemetry.maximum_cloud_water == 0.0
    assert result.telemetry.maximum_precipitation == 0.0
    assert result.telemetry.maximum_surface_water == 0.0
    assert result.telemetry.maximum_infiltration == 0.0
    assert result.telemetry.maximum_runoff == 0.0
    assert result.telemetry.maximum_water_passage == 0.0
    assert result.telemetry.maximum_precipitating_tiles == 0