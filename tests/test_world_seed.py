from engine.terrain.world_seed import WorldSeed


def test_world_seed_can_be_created() -> None:

    seed = WorldSeed(12345)

    assert seed.value == 12345


def test_world_seed_random_generates_positive_integer() -> None:

    seed = WorldSeed.random()

    assert isinstance(seed.value, int)
    assert seed.value >= 0