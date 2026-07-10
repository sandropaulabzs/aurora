from engine.systems.system import System
from engine.systems.system_manager import SystemManager


class FakeSystem(System):

    def __init__(self) -> None:
        self.updated = False

    def update(self) -> None:
        self.updated = True


def test_system_manager_updates_registered_systems() -> None:

    manager = SystemManager()

    system = FakeSystem()

    manager.register(system)

    manager.update()

    assert system.updated is True