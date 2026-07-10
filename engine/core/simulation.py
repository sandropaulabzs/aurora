from .clock import Clock

from engine.events.bus import EventBus
from engine.events.time_events import TimeAdvanced


class Simulation:

    def __init__(self, event_bus: EventBus):

        self.clock = Clock()
        self.event_bus = event_bus

    def update(self):

        self.clock.tick()

        event = TimeAdvanced(
            day=self.clock.day,
            hour=self.clock.hour,
            minute=self.clock.minute
        )

        self.event_bus.publish(event)