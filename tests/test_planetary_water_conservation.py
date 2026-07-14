import pytest

from engine.core.world import World
from engine.systems.world_dynamics_system import (
    WorldDynamicsSystem,
)
from engine.terrain.world_seed import WorldSeed


def total_water(world: World) -> float:
    total = 0.0

    for row in world.map.tiles:
        for tile in row:
            total += tile.ground_moisture
            total += tile.atmospheric_moisture
            total += tile.cloud_water

    return total


def test_planetary_water_is_conserved() -> None:

    world = World(
        width=32,
        height=32,
        seed=WorldSeed(123456),
    )

    world.initialize()

    system = WorldDynamicsSystem(world)

    initial_total = total_water(world)

    for _ in range(1000):
        system.update()

    final_total = total_water(world)

    assert final_total == pytest.approx(
        initial_total,
        abs=1e-9,
    )