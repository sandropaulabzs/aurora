from engine.terrain.world_map import WorldMap


class RunoffVisualizer:
    """
    Renders surface runoff intensity in ASCII.

    Zero remains blank. Every positive runoff value
    leaves at least a faint visible trace.
    """

    SYMBOLS = " .:-=+*#%@"

    def render(
        self,
        world_map: WorldMap,
    ) -> str:
        lines: list[str] = []
        max_index = len(self.SYMBOLS) - 1

        for y in range(world_map.height):
            row: list[str] = []

            for x in range(world_map.width):
                tile = world_map.get_tile(x, y)

                assert tile is not None

                value = max(
                    0.0,
                    min(tile.runoff, 1.0),
                )

                if value == 0.0:
                    index = 0
                else:
                    index = max(
                        1,
                        int(value * max_index),
                    )

                row.append(
                    self.SYMBOLS[index]
                )

            lines.append(
                "".join(row)
            )

        return "\n".join(lines)