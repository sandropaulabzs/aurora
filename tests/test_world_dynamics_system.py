from engine.core.world import World
from engine.systems.world_dynamics_system import WorldDynamicsSystem
from engine.terrain.world_seed import WorldSeed


def test_world_dynamics_updates_atmospheric_moisture() -> None:
    world = World(
        width=8,
        height=8,
        seed=WorldSeed(12345),
    )

    world.initialize()

    # O teste fornece explicitamente água líquida,
    # pois esta seed pode gerar um mapa sem oceanos.
    for row in world.map.tiles:
        for tile in row:
            tile.ground_moisture = 1.0

    moisture_before = sum(
        tile.atmospheric_moisture
        for row in world.map.tiles
        for tile in row
    )

    WorldDynamicsSystem(world).update()

    moisture_after = sum(
        tile.atmospheric_moisture
        for row in world.map.tiles
        for tile in row
    )

    assert moisture_after > moisture_before


def test_world_dynamics_preserves_non_negative_water_states() -> None:
    world = World(
        width=8,
        height=8,
        seed=WorldSeed(54321),
    )

    world.initialize()

    system = WorldDynamicsSystem(world)

    for _ in range(10):
        system.update()

    for row in world.map.tiles:
        for tile in row:
            assert tile.ground_moisture >= 0.0
            assert tile.atmospheric_moisture >= 0.0