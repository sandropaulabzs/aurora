from engine.terrain.planet_dna import PlanetDNA
from engine.terrain.world_seed import WorldSeed


class PlanetReport:
    """
    Gera um relatório textual das características do planeta.
    """

    def generate(
        self,
        seed: WorldSeed,
        dna: PlanetDNA,
    ) -> str:

        lines = [
            "=" * 40,
            "PLANET REPORT",
            "=" * 40,
            "",
            f"Seed............. {seed.value}",
            "",
            f"Continentality.. {dna.continentality:.3f}",
            f"Relief.......... {dna.relief:.3f}",
            f"Volcanism....... {dna.volcanism:.3f}",
            f"Humidity........ {dna.humidity:.3f}",
            f"Temperature..... {dna.temperature:.3f}",
            f"Erosion......... {dna.erosion:.3f}",
            f"Water Level..... {dna.water_level:.3f}",
            f"Stability....... {dna.stability:.3f}",
            "",
            "=" * 40,
        ]

        return "\n".join(lines)