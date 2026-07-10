from engine.systems.system import System


class SystemManager:
    """
    Gerencia a execução dos sistemas da SEED Engine.
    """

    def __init__(self) -> None:
        self._systems: list[System] = []

    def register(self, system: System) -> None:
        self._systems.append(system)

    def update(self) -> None:
        for system in self._systems:
            system.update()