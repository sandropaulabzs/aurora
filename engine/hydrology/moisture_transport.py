from engine.terrain.world_map import WorldMap


class MoistureTransport:
    """
    Transports atmospheric moisture according to
    the local wind field.
    """

    def apply(
        self,
        world_map: WorldMap,
        transport_rate: float = 0.10,
    ) -> None:
        delta = [
            [0.0 for _ in range(world_map.width)]
            for _ in range(world_map.height)
        ]

        for row in world_map.tiles:
            for tile in row:

                if tile.wind_speed == 0.0:
                    continue

                target = world_map.get_tile(
                    tile.x + tile.wind_dx,
                    tile.y + tile.wind_dy,
                )

                if target is None:
                    continue

                transported = (
                    tile.atmospheric_moisture
                    * tile.wind_speed
                    * transport_rate
                )

                delta[tile.y][tile.x] -= transported
                delta[target.y][target.x] += transported

        for y in range(world_map.height):
            for x in range(world_map.width):

                tile = world_map.get_tile(x, y)

                assert tile is not None

                tile.atmospheric_moisture += delta[y][x]

                tile.atmospheric_moisture = max(
                    0.0,
                    min(
                        tile.atmospheric_moisture,
                        1.0,
                    ),
                )