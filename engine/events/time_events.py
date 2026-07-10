from dataclasses import dataclass

from .event import Event


@dataclass(slots=True, frozen=True)
class TimeAdvanced(Event):

    day: int
    hour: int
    minute: int