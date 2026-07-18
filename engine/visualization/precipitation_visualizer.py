from engine.terrain.world_map import WorldMap


class PrecipitationVisualizer:
    """
    Renders precipitation from the current simulation tick.

    Zero precipitation remains blank. Every positive value
    leaves at least a faint visible trace.
    """

    SYMBOLS = " .:-=+*#%@"

    def render(
        self,
        world_map: WorldMap,
    ) -> str:
        lines: list[str] = []
        max_index = len(self.SYMBOLS) - 1

        maximum_precipitation = max(
            (
                tile.precipitation
                for row in world_map.tiles
                for tile in row
            ),
            default=0.0,
        )

        for y in range(world_map.height):
            row: list[str] = []

            for x in range(world_map.width):
                tile = world_map.get_tile(x, y)

                assert tile is not None

                if (
                    tile.precipitation <= 0.0
                    or maximum_precipitation <= 0.0
                ):
                    index = 0
                else:
                    normalized = (
                        tile.precipitation
                        / maximum_precipitation
                    )

                    index = max(
                        1,
                        int(normalized * max_index),
                    )

                row.append(
                    self.SYMBOLS[index]
                )

            lines.append(
                "".join(row)
            )

        return "\n".join(lines)