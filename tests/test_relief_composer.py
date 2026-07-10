from engine.terrain.planet_dna import PlanetDNA
from engine.terrain.relief_composer import ReliefComposer
from engine.terrain.world_seed import WorldSeed


def make_dna(
    relief: float = 0.5,
    continentality: float = 0.5,
) -> PlanetDNA:
    return PlanetDNA(
        continentality=continentality,
        relief=relief,
        volcanism=0.5,
        humidity=0.5,
        temperature=0.5,
        erosion=0.5,
        water_level=0.5,
        stability=0.5,
    )


def test_same_seed_and_position_return_same_altitude() -> None:
    seed = WorldSeed(12345)
    dna = make_dna()

    composer_a = ReliefComposer(seed, dna)
    composer_b = ReliefComposer(seed, dna)

    altitude_a = composer_a.altitude_at(10, 20)
    altitude_b = composer_b.altitude_at(10, 20)

    assert altitude_a == altitude_b


def test_altitude_stays_between_zero_and_one() -> None:
    composer = ReliefComposer(
        WorldSeed(999),
        make_dna(relief=1.0, continentality=1.0),
    )

    for y in range(16):
        for x in range(16):
            altitude = composer.altitude_at(x, y)

            assert 0.0 <= altitude <= 1.0


def test_invalid_scale_raises_value_error() -> None:
    try:
        ReliefComposer(
            WorldSeed(123),
            make_dna(),
            scale=0.0,
        )
    except ValueError as error:
        assert str(error) == "scale must be greater than zero"
    else:
        raise AssertionError("ValueError was not raised")