from engine.terrain.world_map import WorldMap


class PrecipitationThresholdVisualizer:
    """
    Renders the local precipitation threshold in ASCII.
    """

    SYMBOLS = " .:-=+*#%@"

    def render(
        self,
        world_map: WorldMap,
    ) -> str:
        lines: list[str] = []
        max_index = len(self.SYMBOLS) - 1

        minimum = 0.20
        maximum = 0.70
        threshold_range = maximum - minimum

        for y in range(world_map.height):
            row: list[str] = []

            for x in range(world_map.width):
                tile = world_map.get_tile(x, y)

                assert tile is not None

                normalized = (
                    tile.precipitation_threshold
                    - minimum
                ) / threshold_range

                normalized = max(
                    0.0,
                    min(normalized, 1.0),
                )

                index = int(
                    normalized * max_index
                )

                row.append(
                    self.SYMBOLS[index]
                )

            lines.append(
                "".join(row)
            )

        return "\n".join(lines)