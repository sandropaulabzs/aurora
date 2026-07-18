from engine.experiments.experiment_telemetry import (
    ExperimentTelemetry,
)
from engine.terrain.world_map import WorldMap


class TelemetryCollector:
    """
    Updates experiment telemetry using the current world state.

    The collector is passive: it reads the world,
    but never modifies any tile.
    """

    def collect(
        self,
        world_map: WorldMap,
        telemetry: ExperimentTelemetry,
    ) -> None:
        tiles = [
            tile
            for row in world_map.tiles
            for tile in row
        ]

        if not tiles:
            raise ValueError(
                "world map must contain at least one tile"
            )

        telemetry.maximum_cloud_water = max(
            telemetry.maximum_cloud_water,
            max(
                tile.cloud_water
                for tile in tiles
            ),
        )

        telemetry.maximum_precipitation = max(
            telemetry.maximum_precipitation,
            max(
                tile.precipitation
                for tile in tiles
            ),
        )

        telemetry.maximum_surface_water = max(
            telemetry.maximum_surface_water,
            max(
                tile.surface_water
                for tile in tiles
            ),
        )

        telemetry.maximum_infiltration = max(
            telemetry.maximum_infiltration,
            max(
                tile.infiltration
                for tile in tiles
            ),
        )

        telemetry.maximum_runoff = max(
            telemetry.maximum_runoff,
            max(
                tile.runoff
                for tile in tiles
            ),
        )

        telemetry.maximum_water_passage = max(
            telemetry.maximum_water_passage,
            max(
                tile.water_passage
                for tile in tiles
            ),
        )

        precipitating_tiles = sum(
            tile.precipitation > 0.0
            for tile in tiles
        )

        telemetry.maximum_precipitating_tiles = max(
            telemetry.maximum_precipitating_tiles,
            precipitating_tiles,
        )