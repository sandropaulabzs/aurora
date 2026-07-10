from engine.terrain.noise import NoiseGenerator
from engine.terrain.world_seed import WorldSeed


def test_same_seed_same_coordinate_returns_same_value() -> None:
    seed = WorldSeed(12345)

    generator_a = NoiseGenerator(seed)
    generator_b = NoiseGenerator(seed)

    value_a = generator_a.value(10, 20)
    value_b = generator_b.value(10, 20)

    assert value_a == value_b


def test_different_coordinates_return_different_values() -> None:
    seed = WorldSeed(12345)

    generator = NoiseGenerator(seed)

    value_a = generator.value(10, 20)
    value_b = generator.value(11, 20)

    assert value_a != value_b


def test_different_seeds_return_different_values() -> None:
    generator_a = NoiseGenerator(WorldSeed(123))
    generator_b = NoiseGenerator(WorldSeed(456))

    value_a = generator_a.value(5, 5)
    value_b = generator_b.value(5, 5)

    assert value_a != value_b


def test_noise_value_is_between_zero_and_one() -> None:
    generator = NoiseGenerator(WorldSeed(999))

    value = generator.value(42, 42)

    assert 0.0 <= value <= 1.0