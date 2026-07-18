from engine.analysis.observatory_console import (
    ObservatoryConsole,
)
from engine.core.world import World
from engine.terrain.world_seed import WorldSeed


def test_observatory_console_renders_world_report() -> None:
    world = World(
        width=2,
        height=2,
        seed=WorldSeed(123),
    )

    world.initialize()

    result = ObservatoryConsole().render(
        world
    )

    assert "WORLD SCIENTIFIC REPORT" in result
    assert "HIGHEST TEMPERATURE" in result
    assert "LOWEST PRESSURE" in result
    assert "HIGHEST CLOUD WATER" in result
    assert "HIGHEST SURFACE WATER" in result
    assert "PRECIPITATING TILES" in result