from dataclasses import dataclass

from engine.terrain.world_map import WorldMap


@dataclass(slots=True, frozen=True)
class WaterPassageReport:
    """
    Scientific summary of accumulated hydrological memory.
    """

    maximum_passage: float
    maximum_position: tuple[int, int]
    active_tiles: int
    total_passage: float


class WaterPassageAnalyzer:
    """
    Measures accumulated hydrological memory
    without modifying the world.
    """

    def analyze(
        self,
        world_map: WorldMap,
    ) -> WaterPassageReport:
        tiles = [
            tile
            for row in world_map.tiles
            for tile in row
        ]

        if not tiles:
            raise ValueError(
                "world map must contain at least one tile"
            )

        maximum_tile = max(
            tiles,
            key=lambda tile: tile.water_passage,
        )

        return WaterPassageReport(
            maximum_passage=maximum_tile.water_passage,
            maximum_position=(
                maximum_tile.x,
                maximum_tile.y,
            ),
            active_tiles=sum(
                tile.water_passage > 0.0
                for tile in tiles
            ),
            total_passage=sum(
                tile.water_passage
                for tile in tiles
            ),
        )