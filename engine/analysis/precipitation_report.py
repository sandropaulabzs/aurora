from dataclasses import dataclass

from engine.terrain.world_map import WorldMap


@dataclass(slots=True, frozen=True)
class PrecipitationReport:
    maximum_cloud_water: float
    minimum_threshold: float
    maximum_precipitation: float
    precipitating_tiles: int

    @property
    def threshold_gap(self) -> float:
        return (
            self.minimum_threshold
            - self.maximum_cloud_water
        )


class PrecipitationAnalyzer:
    """
    Measures whether the simulated atmosphere is approaching
    or producing precipitation.
    """

    def analyze(
        self,
        world_map: WorldMap,
    ) -> PrecipitationReport:
        tiles = [
            tile
            for row in world_map.tiles
            for tile in row
        ]

        if not tiles:
            raise ValueError(
                "world map must contain at least one tile"
            )

        return PrecipitationReport(
            maximum_cloud_water=max(
                tile.cloud_water
                for tile in tiles
            ),
            minimum_threshold=min(
                tile.precipitation_threshold
                for tile in tiles
            ),
            maximum_precipitation=max(
                tile.precipitation
                for tile in tiles
            ),
            precipitating_tiles=sum(
                tile.precipitation > 0.0
                for tile in tiles
            ),
        )