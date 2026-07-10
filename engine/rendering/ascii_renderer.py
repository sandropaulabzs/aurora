from engine.terrain.world_map import WorldMap


class AsciiRenderer:
    """
    Renderiza o relevo do mundo em ASCII.
    """

    SYMBOLS = (
        " .:-=+*#%@"
    )

    def render(self, world_map: WorldMap) -> str:

        lines: list[str] = []

        max_index = len(self.SYMBOLS) - 1

        for y in range(world_map.height):

            row = []

            for x in range(world_map.width):

                tile = world_map.get_tile(x, y)

                assert tile is not None

                altitude = max(
                    0.0,
                    min(
                        tile.altitude,
                        1.0,
                    ),
                )

                index = int(
                    altitude * max_index
                )

                row.append(
                    self.SYMBOLS[index]
                )

            lines.append(
                "".join(row)
            )

        return "\n".join(lines)