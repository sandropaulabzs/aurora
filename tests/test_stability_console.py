from engine.core.world import World
from engine.experiments.stability_console import (
    StabilityConsole,
)
from engine.terrain.world_seed import WorldSeed


def test_stability_console_returns_formatted_report() -> None:
    world = World(
        width=4,
        height=4,
        seed=WorldSeed(12345),
    )

    world.initialize()

    result = StabilityConsole().run(
        world=world,
        ticks=250,
        snapshot_interval=100,
    )

    assert "AURORA PLANET STABILITY REPORT" in result
    assert "TICK | TOTAL WATER" in result
    assert "100" in result
    assert "200" in result
    assert "250" in result


def test_stability_console_accepts_zero_ticks() -> None:
    world = World(
        width=4,
        height=4,
        seed=WorldSeed(111),
    )

    world.initialize()

    result = StabilityConsole().run(
        world=world,
        ticks=0,
        snapshot_interval=100,
    )

    assert "AURORA PLANET STABILITY REPORT" in result
    assert "0" in result