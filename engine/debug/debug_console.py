from engine.events.time_events import TimeAdvanced


class DebugConsole:

    def on_time_advanced(self, event: TimeAdvanced):

        print(
            f"🕒 Day {event.day} - "
            f"{event.hour:02}:{event.minute:02}"
        )