from engine.terrain.world_map import WorldMap


class OceanVisualizer:
    """
    Renders the permanent ocean mask in ASCII.

    Ocean tiles are represented by water symbols.
    Land tiles remain blank.
    """

    OCEAN_SYMBOL = "~"
    LAND_SYMBOL = " "

    def render(
        self,
        world_map: WorldMap,
    ) -> str:
        lines: list[str] = []

        for y in range(world_map.height):
            row: list[str] = []

            for x in range(world_map.width):
                tile = world_map.get_tile(x, y)

                assert tile is not None

                if tile.is_ocean:
                    row.append(self.OCEAN_SYMBOL)
                else:
                    row.append(self.LAND_SYMBOL)

            lines.append(
                "".join(row)
            )

        return "\n".join(lines)