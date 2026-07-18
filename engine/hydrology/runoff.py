from engine.terrain.world_map import WorldMap


class RunoffModel:
    """
    Transfers surface water toward the lowest neighboring tile.

    Runoff reaching land becomes surface water.
    Runoff reaching ocean returns to the ocean-water reservoir.

    The runoff field records how much water left each tile
    during the current update.
    """

    DEFAULT_RATE = 0.10

    def apply(
        self,
        world_map: WorldMap,
        runoff_rate: float = DEFAULT_RATE,
    ) -> None:
        if not 0.0 <= runoff_rate <= 1.0:
            raise ValueError(
                "runoff_rate must be between zero and one"
            )

        surface_delta = [
            [0.0 for _ in range(world_map.width)]
            for _ in range(world_map.height)
        ]

        ocean_delta = [
            [0.0 for _ in range(world_map.width)]
            for _ in range(world_map.height)
        ]

        for row in world_map.tiles:
            for tile in row:
                tile.runoff = 0.0

        for y in range(world_map.height):
            for x in range(world_map.width):
                tile = world_map.get_tile(x, y)

                assert tile is not None

                if tile.surface_water <= 0.0:
                    continue

                neighbors = world_map.get_neighbors(
                    tile.x,
                    tile.y,
                )

                lower_neighbors = [
                    neighbor
                    for neighbor in neighbors
                    if neighbor.altitude < tile.altitude
                ]

                if not lower_neighbors:
                    continue

                target = min(
                    lower_neighbors,
                    key=lambda neighbor: neighbor.altitude,
                )

                transferred = (
                    tile.surface_water
                    * runoff_rate
                )

                surface_delta[tile.y][tile.x] -= transferred

                if target.is_ocean:
                    ocean_delta[target.y][target.x] += transferred
                else:
                    surface_delta[target.y][target.x] += transferred

                tile.runoff = transferred

        for y in range(world_map.height):
            for x in range(world_map.width):
                tile = world_map.get_tile(x, y)

                assert tile is not None

                tile.surface_water += surface_delta[y][x]
                tile.ground_moisture += ocean_delta[y][x]

                tile.surface_water = max(
                    0.0,
                    tile.surface_water,
                )