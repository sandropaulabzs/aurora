from engine.terrain.planet_dna_factory import PlanetDNAFactory
from engine.terrain.world_seed import WorldSeed


def test_same_seed_generates_same_planet_dna() -> None:
    factory = PlanetDNAFactory()
    seed = WorldSeed(12345)

    dna_a = factory.create(seed)
    dna_b = factory.create(seed)

    assert dna_a == dna_b


def test_different_seeds_generate_different_planet_dna() -> None:
    factory = PlanetDNAFactory()

    dna_a = factory.create(WorldSeed(12345))
    dna_b = factory.create(WorldSeed(54321))

    assert dna_a != dna_b


def test_planet_dna_genes_are_between_zero_and_one() -> None:
    factory = PlanetDNAFactory()
    dna = factory.create(WorldSeed(999))

    genes = (
        dna.continentality,
        dna.relief,
        dna.volcanism,
        dna.humidity,
        dna.temperature,
        dna.erosion,
        dna.water_level,
        dna.stability,
    )

    assert all(0.0 <= gene <= 1.0 for gene in genes)