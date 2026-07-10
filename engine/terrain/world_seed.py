from dataclasses import dataclass
import random


@dataclass(slots=True, frozen=True)
class WorldSeed:
    """
    Representa a semente de geração do mundo.
    """

    value: int

    @classmethod
    def random(cls) -> "WorldSeed":
        return cls(random.randint(0, 2**31 - 1))