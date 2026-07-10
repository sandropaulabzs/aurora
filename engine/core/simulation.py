from engine.systems.system_manager import SystemManager


class Simulation:
    """
    Loop principal da simulação.
    """

    def __init__(self, system_manager: SystemManager) -> None:
        self.system_manager = system_manager

    def update(self) -> None:
        self.system_manager.update()