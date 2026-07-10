from engine.debug.planet_report import PlanetReport
from engine.terrain.planet_dna import PlanetDNA
from engine.terrain.world_seed import WorldSeed


def test_planet_report_contains_seed_and_all_genes() -> None:
    report = PlanetReport()

    seed = WorldSeed(12345)

    dna = PlanetDNA(
        continentality=0.81,
        relief=0.72,
        volcanism=0.11,
        humidity=0.35,
        temperature=0.54,
        erosion=0.27,
        water_level=0.68,
        stability=0.94,
    )

    result = report.generate(seed, dna)

    assert "Seed............. 12345" in result
    assert "Continentality.. 0.810" in result
    assert "Relief.......... 0.720" in result
    assert "Volcanism....... 0.110" in result
    assert "Humidity........ 0.350" in result
    assert "Temperature..... 0.540" in result
    assert "Erosion......... 0.270" in result
    assert "Water Level..... 0.680" in result
    assert "Stability....... 0.940" in result