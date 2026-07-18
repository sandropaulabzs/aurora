from engine.experiments.stability_snapshot import (
    StabilitySnapshot,
)
from engine.terrain.world_map import WorldMap


class StabilitySnapshotCollector:
    """
    Captures a compact hydrological snapshot
    of the world at a specific simulation tick.
    """

    def collect(
        self,
        world_map: WorldMap,
        tick: int,
    ) -> StabilitySnapshot:
        if tick < 0:
            raise ValueError(
                "tick must be zero or greater"
            )

        tiles = [
            tile
            for row in world_map.tiles
            for tile in row
        ]

        if not tiles:
            raise ValueError(
                "world map must contain at least one tile"
            )

        total_water = sum(
            tile.ground_moisture
            + tile.surface_water
            + tile.atmospheric_moisture
            + tile.cloud_water
            for tile in tiles
        )

        return StabilitySnapshot(
            tick=tick,
            total_water=total_water,
            maximum_cloud_water=max(
                tile.cloud_water
                for tile in tiles
            ),
            maximum_surface_water=max(
                tile.surface_water
                for tile in tiles
            ),
            maximum_runoff=max(
                tile.runoff
                for tile in tiles
            ),
            maximum_water_passage=max(
                tile.water_passage
                for tile in tiles
            ),
            precipitating_tiles=sum(
                tile.precipitation > 0.0
                for tile in tiles
            ),
        )