from engine.core.world import World
from engine.experiments.laboratory_console import (
    LaboratoryConsole,
)
from engine.terrain.world_seed import WorldSeed


def test_laboratory_console_returns_formatted_report() -> None:
    world = World(
        width=8,
        height=8,
        seed=WorldSeed(24680),
    )

    world.initialize()

    result = LaboratoryConsole().run(
        world=world,
        ticks=25,
    )

    assert "AURORA LABORATORY RESULT" in result
    assert "Ticks executed: 25" in result
    assert "HISTORICAL HYDROLOGY MAXIMUMS" in result
    assert "WORLD SCIENTIFIC REPORT" in result


def test_laboratory_console_accepts_zero_ticks() -> None:
    world = World(
        width=4,
        height=4,
        seed=WorldSeed(111),
    )

    world.initialize()

    result = LaboratoryConsole().run(
        world=world,
        ticks=0,
    )

    assert "Ticks executed: 0" in result