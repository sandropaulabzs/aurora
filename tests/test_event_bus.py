from engine.core.clock import Clock


def test_clock_advances_one_minute() -> None:
    clock = Clock()

    clock.tick()

    assert clock.day == 1
    assert clock.hour == 6
    assert clock.minute == 1