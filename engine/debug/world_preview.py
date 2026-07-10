from engine.rendering.ascii_renderer import AsciiRenderer
from engine.terrain.world_map import WorldMap


class WorldPreview:
    """
    Ferramenta de depuração para visualizar o mapa no terminal.
    """

    def __init__(self) -> None:
        self.renderer = AsciiRenderer()

    def show(self, world_map: WorldMap) -> None:
        print()
        print("=== WORLD PREVIEW ===")
        print()
        print(self.renderer.render(world_map))
        print()