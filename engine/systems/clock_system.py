from engine.core.clock import Clock
from engine.events.bus import EventBus
from engine.events.time_events import TimeAdvanced
from engine.systems.system import System


class ClockSystem(System):
    """
    Sistema responsável por avançar o tempo do mundo.
    """

    def __init__(self, event_bus: EventBus) -> None:
        self.clock = Clock()
        self.event_bus = event_bus

    def update(self) -> None:
        self.clock.tick()

        self.event_bus.publish(
            TimeAdvanced(
                day=self.clock.day,
                hour=self.clock.hour,
                minute=self.clock.minute,
            )
        )