from engine.core.world import World
from engine.terrain.world_seed import WorldSeed


def test_world_uses_provided_seed() -> None:
    seed = WorldSeed(12345)

    world = World(seed=seed)

    assert world.seed is seed
    assert world.seed.value == 12345


def test_world_generates_seed_when_none_is_provided() -> None:
    world = World()

    assert isinstance(world.seed, WorldSeed)
    assert world.seed.value >= 0