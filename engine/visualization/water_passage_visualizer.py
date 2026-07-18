from engine.terrain.world_map import WorldMap


class WaterPassageVisualizer:
    """
    Renders accumulated hydrological memory in ASCII.

    water_passage is cumulative and may exceed 1.0,
    so the values are normalized against the highest
    passage found in the current world map.
    """

    SYMBOLS = " .:-=+*#%@"

    def render(
        self,
        world_map: WorldMap,
    ) -> str:
        tiles = [
            tile
            for row in world_map.tiles
            for tile in row
        ]

        if not tiles:
            return ""

        maximum_passage = max(
            tile.water_passage
            for tile in tiles
        )

        lines: list[str] = []
        max_index = len(self.SYMBOLS) - 1

        for y in range(world_map.height):
            row: list[str] = []

            for x in range(world_map.width):
                tile = world_map.get_tile(x, y)

                assert tile is not None

                if (
                    tile.water_passage <= 0.0
                    or maximum_passage <= 0.0
                ):
                    index = 0
                else:
                    normalized = (
                        tile.water_passage
                        / maximum_passage
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