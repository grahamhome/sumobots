import simpleio

from .searching import Searching
from .state import State
from ..melodies import note_frequencies


class Countdown(State):
    def start(self):
        super().start()
        self.bot.pixels.fill(0x00FF00)
        simpleio.tone(
            pin=self.bot.piezo,
            frequency=note_frequencies.get("C5"),
            duration=0.3,
        )
        self.bot.pixels.fill(0)
        self.switch(Searching)