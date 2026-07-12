from engine.version import ENGINE_NAME, PROJECT_NAME, VERSION

from engine.core.simulation import Simulation
from engine.core.world import World
from engine.debug.debug_console import DebugConsole
from engine.events.bus import EventBus
from engine.events.time_events import TimeAdvanced
from engine.systems.clock_system import ClockSystem
from engine.systems.system_manager import SystemManager
from engine.visualization.observatory import AuroraObservatory


class SeedEngine:

    def __init__(self) -> None:

        # Infraestrutura
        self.event_bus = EventBus()
        self.system_manager = SystemManager()

        # Mundo
        self.world = World()

        # Sistemas
        self.clock_system = ClockSystem(self.event_bus)
        self.system_manager.register(self.clock_system)

        # Ferramentas
        self.debug_console = DebugConsole()
        self.observatory = AuroraObservatory()

        # Assinantes
        self.event_bus.subscribe(
            TimeAdvanced,
            self.debug_console.on_time_advanced,
        )

        # Simulação
        self.simulation = Simulation(self.system_manager)

    def start(self) -> None:

        print("=" * 40)
        print(PROJECT_NAME)
        print(ENGINE_NAME)
        print(VERSION)
        print("=" * 40)

        self.world.initialize()

        print()
        print(self.observatory.render(self.world.map))
        print()

        print("Simulation Started")
        print()

        for _ in range(20):
            self.simulation.update()