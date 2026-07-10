from engine.events.bus import EventBus
from engine.events.time_events import TimeAdvanced
from engine.systems.clock_system import ClockSystem


def test_clock_system_publishes_time_advanced_event() -> None:
    bus = EventBus()
    received_events: list[TimeAdvanced] = []

    def listener(event: TimeAdvanced) -> None:
        received_events.append(event)

    bus.subscribe(TimeAdvanced, listener)

    system = ClockSystem(bus)
    system.update()

    assert len(received_events) == 1
    assert received_events[0].day == 1
    assert received_events[0].hour == 6
    assert received_events[0].minute == 1