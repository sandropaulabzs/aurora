from dataclasses import dataclass


@dataclass
class Clock:

    day: int = 1
    hour: int = 6
    minute: int = 0

    def tick(self, minutes: int = 1):

        self.minute += minutes

        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1

        while self.hour >= 24:
            self.hour -= 24
            self.day += 1

    @property
    def formatted_time(self):

        return f"Day {self.day} - {self.hour:02}:{self.minute:02}"