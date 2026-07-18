from engine.analysis.world_report import WorldReport
from engine.terrain.world_map import WorldMap


class WorldAnalyzer:
    """
    Produces a passive scientific summary
    of the current world state.
    """

    def analyze(
        self,
        world_map: WorldMap,
    ) -> WorldReport:
        tiles = [
            tile
            for row in world_map.tiles
            for tile in row
        ]

        if not tiles:
            raise ValueError(
                "world map must contain at least one tile"
            )

        highest_temperature_tile = max(
            tiles,
            key=lambda tile: tile.temperature,
        )

        lowest_pressure_tile = min(
            tiles,
            key=lambda tile: tile.pressure,
        )

        highest_cloud_water_tile = max(
            tiles,
            key=lambda tile: tile.cloud_water,
        )

        highest_surface_water_tile = max(
            tiles,
            key=lambda tile: tile.surface_water,
        )

        precipitating_tiles = sum(
            tile.precipitation > 0.0
            for tile in tiles
        )

        return WorldReport(
            highest_temperature=(
                highest_temperature_tile.temperature
            ),
            highest_temperature_position=(
                highest_temperature_tile.x,
                highest_temperature_tile.y,
            ),
            lowest_pressure=(
                lowest_pressure_tile.pressure
            ),
            lowest_pressure_position=(
                lowest_pressure_tile.x,
                lowest_pressure_tile.y,
            ),
            highest_cloud_water=(
                highest_cloud_water_tile.cloud_water
            ),
            highest_cloud_water_position=(
                highest_cloud_water_tile.x,
                highest_cloud_water_tile.y,
            ),
            highest_surface_water=(
                highest_surface_water_tile.surface_water
            ),
            highest_surface_water_position=(
                highest_surface_water_tile.x,
                highest_surface_water_tile.y,
            ),
            precipitating_tiles=precipitating_tiles,
        )