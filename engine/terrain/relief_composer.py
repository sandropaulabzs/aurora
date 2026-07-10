import math

from engine.terrain.interpolation import lerp, smoothstep
from engine.terrain.noise import NoiseGenerator
from engine.terrain.planet_dna import PlanetDNA
from engine.terrain.world_seed import WorldSeed


class ReliefComposer:
    """
    Produz altitudes suaves e determinísticas para o relevo.
    """

    def __init__(
        self,
        seed: WorldSeed,
        dna: PlanetDNA,
        scale: float = 8.0,
    ) -> None:
        if scale <= 0.0:
            raise ValueError("scale must be greater than zero")

        self.noise = NoiseGenerator(seed)
        self.dna = dna
        self.scale = scale

    def altitude_at(self, x: int, y: int) -> float:
        grid_x = x / self.scale
        grid_y = y / self.scale

        x0 = math.floor(grid_x)
        y0 = math.floor(grid_y)
        x1 = x0 + 1
        y1 = y0 + 1

        local_x = smoothstep(grid_x - x0)
        local_y = smoothstep(grid_y - y0)

        top_left = self.noise.value(x0, y0)
        top_right = self.noise.value(x1, y0)
        bottom_left = self.noise.value(x0, y1)
        bottom_right = self.noise.value(x1, y1)

        top = lerp(top_left, top_right, local_x)
        bottom = lerp(bottom_left, bottom_right, local_x)

        base_altitude = lerp(top, bottom, local_y)

        relief_strength = 0.25 + (self.dna.relief * 0.75)
        continental_bias = (self.dna.continentality - 0.5) * 0.30

        altitude = (
            0.5
            + ((base_altitude - 0.5) * relief_strength)
            + continental_bias
        )

        return max(0.0, min(altitude, 1.0))