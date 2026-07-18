from engine.analysis.hydrological_hotspot_report import (
    HydrologicalHotspotReport,
)
from engine.terrain.world_map import WorldMap


class HydrologicalHotspotAnalyzer:
    """
    Locates and describes the tile with the greatest
    amount of surface water.

    The analyzer only reads the world state.
    """

    def analyze(
        self,
        world_map: WorldMap,
    ) -> HydrologicalHotspotReport:
        tiles = [
            tile
            for row in world_map.tiles
            for tile in row
        ]

        if not tiles:
            raise ValueError(
                "world map must contain at least one tile"
            )

        hotspot = max(
            tiles,
            key=lambda tile: tile.surface_water,
        )

        neighbors = world_map.get_neighbors(
            hotspot.x,
            hotspot.y,
        )

        lower_neighbors = [
            neighbor
            for neighbor in neighbors
            if neighbor.altitude < hotspot.altitude
        ]

        lowest_neighbor_altitude = None

        if neighbors:
            lowest_neighbor_altitude = min(
                neighbor.altitude
                for neighbor in neighbors
            )

        return HydrologicalHotspotReport(
            position=(
                hotspot.x,
                hotspot.y,
            ),
            altitude=hotspot.altitude,
            surface_water=hotspot.surface_water,
            ground_moisture=hotspot.ground_moisture,
            soil_capacity=hotspot.soil_capacity,
            infiltration=hotspot.infiltration,
            runoff=hotspot.runoff,
            water_passage=hotspot.water_passage,
            lowest_neighbor_altitude=(
                lowest_neighbor_altitude
            ),
            lower_neighbors=len(
                lower_neighbors
            ),
        )