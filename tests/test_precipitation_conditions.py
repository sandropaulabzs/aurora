from engine.core.world import World
from engine.systems.world_dynamics_system import (
    WorldDynamicsSystem,
)
from engine.terrain.world_seed import WorldSeed


def test_cloud_water_can_form_when_water_is_available() -> None:
    world = World(
        width=32,
        height=32,
        seed=WorldSeed(123456),
    )

    world.initialize()

    # Esta auditoria avalia o ciclo atmosférico.
    # A água inicial é fornecida explicitamente porque
    # esta seed pode gerar um planeta sem oceanos.
    for row in world.map.tiles:
        for tile in row:
            tile.ground_moisture = 1.0

    system = WorldDynamicsSystem(world)

    for _ in range(1000):
        system.update()

    maximum_cloud_water = max(
        tile.cloud_water
        for row in world.map.tiles
        for tile in row
    )

    minimum_threshold = min(
        tile.precipitation_threshold
        for row in world.map.tiles
        for tile in row
    )

    assert maximum_cloud_water > 0.0
    assert minimum_threshold > 0.0